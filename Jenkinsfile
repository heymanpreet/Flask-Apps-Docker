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
                dir("folder") {
                        sh "pwd"
                   }
                sh 'pwd'
                sh 'cd ~'
                sh 'cd /var/jenkins_home/workspace/Flask-Jenkins-build'
                sh 'pwd'
                sh 'docker-compose up --build -d'
                echo "Deployed"
            }
        }
    }
}
