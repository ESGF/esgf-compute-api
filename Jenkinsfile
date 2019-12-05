pipeline {
  agent {
    node {
      label 'jenkins-buildkit'
    }

  }
  stages {
    stage('Build') {
      steps {
        container(name: 'buildkit', shell: '/bin/sh') {
          sh '''buildctl-daemonless.sh build \\
	--frontend dockerfile.v0 \\
	--local context=. \\
	--local dockerfile=. \\
        --opt target=production \\
	--output type=image,name=${OUTPUT_REGISTRY}/compute-api:${GIT_COMMIT:0:8},push=true \\
	--export-cache type=registry,ref=${OUTPUT_REGISTRY}/compute-api:cache \\
	--import-cache type=registry,ref=${OUTPUT_REGISTRY}/compute-api:cache'''
        }

      }
    }

    stage('Testing') {
      steps {
        container(name: 'buildkit', shell: '/bin/sh') {
          sh '''buildctl-daemonless.sh build \\
	--frontend dockerfile.v0 \\
	--local context=. \\
	--local dockerfile=. \\
	--opt target=testresult \\
	--output type=local,dest=output \\
	--import-cache type=registry,ref=${OUTPUT_REGISTRY}/compute-api:cache'''
          sh 'chown -R 10000:10000 output/'
        }

        cobertura(autoUpdateHealth: true, autoUpdateStability: true, failNoReports: true, failUnhealthy: true, failUnstable: true, maxNumberOfBuilds: 2, coberturaReportFile: 'output/coverage.xml')
        junit 'output/unittest.xml'
      }
    }

    stage('Publish Conda') {
      environment {
        CONDA = credentials('conda')
      }
      steps {
        container(name: 'buildkit', shell: '/bin/sh') {
          sh '''buildctl-daemonless.sh build \\
	--frontend dockerfile.v0 \\
	--local context=. \\
	--local dockerfile=. \\
	--opt target=publish \\
	--opt build-arg:CONDA_USERNAME=${CONDA_USR} \\
	--opt build-arg:CONDA_PASSWORD=${CONDA_PSW} \\
	--import-cache type=registry,ref=${OUTPUT_REGISTRY}/compute-api:cache'''
        }

      }
    }

  }
}