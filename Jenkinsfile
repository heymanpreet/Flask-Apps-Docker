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
//                 dir("") {
//                         sh 'pwd'
//                         sh "cd pwd && /usr/local/bin/docker-compose  up --build -d"
//                    }
//                    sh "pwd && cd pwd && docker-compose up --build -d"
//                 sh 'pwd'
//                 sh 'cd ~'
                sh '/usr/local/bin/docker-compose  up --build -d'
//                 sh 'pwd'
//                 sh 'docker-compose up --build -d'
                echo "Deployed"
            }
        }
    }
}
