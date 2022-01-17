pipeline {
    agent{
  node {
      label 'main'
    }
 }
    stages {
        stage('Build') {
            steps {
                //  Building new image
                git url: 'https://github.com/russmckendrick/jenkins-docker-example.git'

                echo "Image built and pushed to repository"
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose up --build -d'
                echo "Deployed"
            }
        }
    }
}
