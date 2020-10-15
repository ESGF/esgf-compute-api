pipeline {
  agent {
    node {
      label 'jenkins-buildkit'
    }

  }
  stages {
    stage("Unittest") {
      steps {
        container(name: "buildkit", shell: "/bin/sh") {
          sh "make build TARGET=testresult"

          sh "chown -R 1000:1000 output/"
        }

        sh "ls -la"
      }
    }
  }
}
