pipeline {
  agent {
    node {
      label 'jenkins-buildkit'
    }

  }
  stages {
    stage('Unittest') {
      environment {
        CACHE_PATH = "${env.CACHE_PATH}"
      }
      steps {
        container(name: 'buildkit', shell: '/bin/sh') {
          sh 'make build TARGET=testresult'

          sh 'chmod -R 755 output/'

          sh 'chown -R 1000:1000 output/'

          sh '''sed -i"" 's/timestamp="[^"]*"//' output/unittest.xml'''
        }

        archiveArtifacts 'output/*'

        cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'output/coverage.xml', conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
        junit 'output/unittest.xml'
      }
    }
    stage('Publish') {
      environment {
        CONDA_TOKEN = credentials('conda-token')
      }
      when {
        branch pattern: 'v\\d+\\.\\d+\\.\\d+', comparator: 'REGEXP'
      }
      steps {
        container(name: 'buildkit', shell: '/bin/sh') {
          sh 'make build TARGET=publish'
        }
      }
    }
  }
}
