pipeline {
  agent any
  stages {
    stage("verify tooling") {
      steps {
        bat '''
          docker version
          docker info
          docker compose version 
        '''
      }
    }
   
    stage("build container") {
      steps {
        bat "docker build -t streamlit_app:latest ."
      }
    }
    stage('Start containers') {
      steps {
          bat "docker run --rm -itd -p 8502:8502 -e PROJECT=${PROJECT} --name streamlit streamlit_app:latest"
      }
    }
    
  }
}
