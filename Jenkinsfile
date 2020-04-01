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

    stage('Publish') {
      parallel {
        stage('Conda') {
          when {
            branch 'master'
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
            branch 'master'
          }
          steps {
            container(name: 'buildkit', shell: '/bin/sh') {
              sh '''#! /bin/sh

make TARGET=production'''
            }

          }
        }

      }
    }

  }
}