pipeline {
  agent none
  stages {
    stage('Build') {
      agent {
        node {
          label 'jenkins-buildkit'
        }

      }
      steps {
        container(name: 'buildkit', shell: '/bin/sh') {
          sh '''#! /bin/sh

make TARGET=testresult'''
          sh 'chown -R 10000:10000 output/'
        }

        cobertura(autoUpdateHealth: true, autoUpdateStability: true, failNoReports: true, failUnhealthy: true, failUnstable: true, maxNumberOfBuilds: 2, coberturaReportFile: 'output/coverage.xml')
        junit 'output/unittest.xml'
        container(name: 'buildkit', shell: '/bin/sh') {
          sh '''#! /bin/sh

if [[ ${GIT_BRANCH} == "master" ]]
the
  make TARGET=publish
fi'''
        }

      }
    }

  }
}