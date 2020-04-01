pipeline {
  agent {
    node {
      label 'jenkins-buildkit'
    }

  }
  stages {
    stage('Testing') {
      steps {
        container(name: 'buildkit', shell: '/bin/sh') {
          sh '''#! /bin/sh

make TARGET=testresult'''
          sh 'chown -R 10000:10000 output/'
        }

        cobertura(autoUpdateHealth: true, autoUpdateStability: true, failNoReports: true, failUnhealthy: true, failUnstable: true, maxNumberOfBuilds: 2, coberturaReportFile: 'output/coverage.xml')
        junit 'output/unittest.xml'
      }
    }

    stage('Conda') {
      when {
        anyOf {
          branch 'master'
          expression {
            return params.FORCE_CONDA
          }

        }

      }
      environment {
        CONDA_TOKEN = credentials('conda-token')
      }
      steps {
        container(name: 'buildkit', shell: '/bin/sh') {
          sh '''#! /bin/sh

make TARGET=publish'''
        }

      }
    }

    stage('Container') {
      when {
        anyOf {
          branch 'master'
          expression {
            return params.FORCE_CONTAINER
          }

        }

      }
      steps {
        container(name: 'buildkit', shell: '/bin/sh') {
          sh '''#! /bin/sh

make TARGET=production REGISTRY=${OUTPUT_REGISTRY}

make TARGET=production REGISTRY=${OUTPUT_REGISTRY} VERSION=latest'''
        }

      }
    }

  }
  parameters {
    booleanParam(name: 'FORCE_CONDA', defaultValue: false, description: 'Force pushing conda package.')
    booleanParam(name: 'FORCE_CONTAINER', defaultValue: false, description: 'Force pushing production container image.')
  }
}