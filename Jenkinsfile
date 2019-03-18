node('build-pod') {
  triggers {
    pollSCM('')
  }

  stage('Checkout') {
    checkout scm
  }


  stage('Unittest') {
    container('conda') {
      sh "conda env create -p ${HOME}/cwt -f environment.yml"

      sh "conda env update -p ${HOME}/cwt -f cwt/tests/environment.yml"

      sh ''' #!/bin/bash
      . /opt/conda/etc/profile.d/conda.sh

      conda activate ${HOME}/cwt

      conda install -y -c conda-forge flake8

      pytest cwt/tests \
        --junit-xml=junit.xml \
        --cov=cwt --cov-report=xml

      flake8 --format=pylint --output-file=flake8.xml --exit-zero
      '''

      archiveArtifacts 'junit.xml'

      archiveArtifacts 'coverage.xml'

      archiveArtifacts 'flake8.xml'

      xunit([JUnit(deleteOutputFiles: true, failIfNotNew: true, pattern: 'junit.xml', skipNoTestFiles: true, stopProcessingIfError: true)])

      cobertura(coberturaReportFile: 'coverage.xml')

      def flake8 = scanForIssues filters: [
      ], tool: flake8(pattern: 'flake8.xml')

      publishIssues issues: [flake8], filters: [includePackage('wps')]
    }
  }

  stage('UnittestPy3') {
    container('conda') {
      sh "conda env update -p ${HOME}/cwt_py3 -f cwt/tests/environment_py3.yml"

      sh ''' #!/bin/bash
      . /opt/conda/etc/profile.d/conda.sh

      conda activate ${HOME}/cwt_py3

      pytest cwt/tests \
        --junit-xml=junit.xml \
        --cov=cwt --cov-report=xml

      flake8 --format=pylint --output-file=flake8.xml --exit-zero
      '''

      archiveArtifacts 'junit.xml'

      archiveArtifacts 'coverage.xml'

      archiveArtifacts 'flake8.xml'

      xunit([JUnit(deleteOutputFiles: true, failIfNotNew: true, pattern: 'junit.xml', skipNoTestFiles: true, stopProcessingIfError: true)])

      cobertura(coberturaReportFile: 'coverage.xml')

      def flake8 = scanForIssues filters: [
      ], tool: flake8(pattern: 'flake8.xml')

      publishIssues issues: [flake8], filters: [includePackage('wps')]
    }
  }
  stage('Build conda package') {
    def parts = env.BRANCH_NAME.split('/')

    env.API_VERSION = parts[parts.length-1]

    env.GIT_VERSION = env.BRANCH_NAME

    withCredentials([usernamePassword(credentialsId: 'jasonb5-anaconda', passwordVariable: 'PASSWORD', usernameVariable: 'USERNAME')]) {
      container('conda') {
        sh 'conda install -y -c conda-forge conda-build anaconda-client'

        sh 'conda build -c conda-forge -c cdat conda/'

        sh 'anaconda login --username ${USERNAME} --password ${PASSWORD}'

        sh 'anaconda upload -u cdat --skip-existing $(conda build --output conda/)'
      }
    }
  }

  stage('Build docker image') {
    container(name: 'kaniko', shell: '/busybox/sh') {
      sh '''#!/busybox/sh
        /kaniko/executor --cache --cache-dir=/cache --context=`pwd` \
        --destination=${LOCAL_REGISTRY}/api:${GIT_VERSION} \
        --dockerfile `pwd`/docker/Dockerfile --insecure-registry \
        ${LOCAL_REGISTRY}
      '''
    }
  }

  stage('Docker image security scan') {
    container('conda') {
      sh '''#!/bin/bash
      clairctl --config ${CLAIR_CONFIG} --log-level debug report ${LOCAL_REGISTRY}/api:${GIT_VERSION}
      '''

      publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, 
          reportDir: 'reports/html/', reportFiles: '*.html', reportName: 'HTML Report', reportTitles: ''])
    }
  }

  stage('Docker push image') {
    container('dind') {
      sh ''' #!/bin/bash
      docker pull ${LOCAL_REGISTRY}/api:${GIT_VERSION}

      docker tag ${LOCAL_REGISTRY}/api:${GIT_VERSION} jasonb87/cwt_api:${GIT_VERSION}

      docker push jasonb87/cwt_api:${GIT_VERSION}
      '''
    }
  }
}
