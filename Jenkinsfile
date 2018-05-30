pipeline {
    agent none

    stages {
        stage('Test API') {
            agent {
                docker {
                    image 'conda-agent'
                    args '--network outside -v /opt/conda/pkgs:/opt/docker/jenkins/conda/pkgs'
                }
            }

            steps {
                checkout scm

                sh 'conda env create --name wps python=2.7'

                sh 'pip install -r requirements.txt'

                sh 'pip install -r cwt/tests/requirements.txt'

                sh '''#! /bin/bash
                    source activate wps

                    nose2 --plugin nose2.plugins.junitxml --junit-xml cwt.tests || exit 1
                '''
            }
        }

        stage('Build docker iamge') {
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
            } 
        }
    }
}
