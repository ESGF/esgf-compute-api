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

        sh 'ls -la output/'
      }
    }

  }
}