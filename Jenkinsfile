pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                //  Building new image
                git url: 'https://github.com/heymanpreet/Flask-Apps-Docker.git'

                echo "Image built and pushed to repository"
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run --rm \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v "$PWD:$PWD" \
    -w="$PWD" \
    docker/compose:1.24.0 up'
                echo "Deployed"
            }
        }
    }
}
