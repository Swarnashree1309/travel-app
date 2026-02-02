pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Swarnashree1309/travel-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build --no-cache -t travel-app:latest .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
		docker stop travel-app || true
                docker rm -f travel-app || true
                docker run -d -p 5000:5000 --name travel-app travel-app:latest
                '''
            }
        }
    }
}

