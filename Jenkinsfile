pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/Swarnashree1309/travel-app.git'
            }
        }

        stage('Copy Code To Docker VM') {
            steps {
                sh '''
                scp -r * ubuntu@13.48.56.23:/home/ubuntu/travel-app
                '''
            }
        }

        stage('Build Image On Docker VM') {
            steps {
                sh '''
                ssh ubuntu@13.48.56.23 "
                cd ~/travel-app &&
                docker build -t travel-app .
                "
                '''
            }
        }

        stage('Run Container On Docker VM') {
            steps {
                sh '''
                ssh ubuntu@13.48.56.23 "
                docker stop travel-app || true &&
                docker rm travel-app || true &&
                docker run -d -p 9090:80 --name travel-app travel-app
                "
                '''
            }
        }
    }
}
