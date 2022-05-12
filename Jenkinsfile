pipeline {
    
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
              bat 'docker build -t streamlit_app:latest .' 
              
            }
        }
       
        
         
         stage('Launch Application') {
            steps {
                bat "docker run --rm -e PROJECT=${PROJECT} -itd -p 8502:8502 --name streamlit streamlit_app:latest"
              
            }
        }
        stage('docker container lookup') {
            steps {
                bat "docker ps"
              
            }
        }
    }
}
