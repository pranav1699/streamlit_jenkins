pipeline {
    environment {
    registry = "dgmtech"
    registryCredential = 'dockerhub'
}
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
              sh 'docker build -t streamlit_app:latest .' 
              
            }
        }
       
        
         
         stage('Launch Application') {
            steps {
              sh 'docker run --rm -itd -p 8502:8502 --name streamlit streamlit_app:latest' 
              
            }
        }
    }
}
