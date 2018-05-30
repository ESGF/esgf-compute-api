pipeline {
    agent none

    stages {
        stage('Test API') {
            agent {
                docker {
                    image 'conda-agent'
                    args '--network outside -v /opt/docker/jenkins/conda/pkgs:/opt/conda/pkgs'
                }
            }

            steps {
                checkout scm

                sh 'conda create --name api --yes python=2.7'

                sh '''#! /bin/bash
                    source activate api

                    pip install -r requirements.txt

                    pip install -r cwt/tests/requirements.txt

                    nose2 --plugin nose2.plugins.junitxml --junit-xml --with-coverage --coverage-report xml cwt.tests || exit 1
                '''
            }
        }

        stage('Build docker iamge') {
            when { anyOf { branch 'bugfix-*'; branch 'release-*' } }

            agent any

            steps {
                script {
                    def version_index = env.BRANCH_NAME.indexOf('-')
                    def version = env.BRANCH_NAME.substring(version_index+1)

                    sh 'docker build -t jasonb87/cwt_api:${version} --build-arg BRANCH=${env.BRANCH_NAME} --network outside docker/'
                }
            }
        }
    }

    post {
        always {
            node('master') {
                step([$class: 'XUnitBuilder',
                    tools: [[$class: 'JUnitType', pattern: 'nose2-junit.xml']]])

                step([$class: 'CoberturaPublisher',
                    coverturaReportFile: 'coverage.xml'])
            } 
        }
    }
}
