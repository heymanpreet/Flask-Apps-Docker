pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                //  Building new image
//                 git url: 'https://github.com/heymanpreet/Flask-Apps-Docker.git'

                echo "Image built and pushed to repository"
            }
        }
        stage('Deploy') {
            steps {
                sh 'pwd'
                sh 'cd Flask-Apps-Docker'
                sh 'docker-compose up'
                echo "Deployed"
            }
        }
    }
}
