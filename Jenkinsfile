pipeline {
    agent any;

    stages {
        stage('Test API') {
            steps {
                git branch: 'devel', changelog: false, poll: false, url: 'https://github.com/ESGF/esgf-compute-api'
                
                sh 'conda env remove -n api || exit 1'
                
                sh 'conda create --name api --yes python=2.7'

                sh '''#! /bin/bash
                    source activate api

                    pip install -r requirements.txt

                    pip install -r cwt/tests/requirements.txt

                    nose2 --plugin nose2.plugins.junitxml --junit-xml --with-coverage --coverage-report xml cwt.tests || exit 1
                '''
            }
        }
    }

    post {
        always {
            xunit testTimeMargin: '3000', thresholdMode: 2, thresholds: [], tools: [JUnit(deleteOutputFiles: true, failIfNotNew: true, pattern: 'nose2-junit.xml', skipNoTestFiles: false, stopProcessingIfError: true)]

            cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'coverage.xml', conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
        } 
    }
}
