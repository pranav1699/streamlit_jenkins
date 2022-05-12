pipeline {
    agent any
        stage('Build Docker Image') {
            steps {
              bat 'docker build -t streamlit_app:latest .' 
              
            }
        }
       
        stage('Stop Running Container ') {
            steps {
              bat 'docker stop streamlit' 
              
            }
        } 
         
         stage('Launch Application') {
            steps {
              bat "docker run --rm -itd -p 8502:8502 -e PROJECT=${PROJECT} --name streamlit streamlit_app:latest"
              
            }
        }
    }
}
