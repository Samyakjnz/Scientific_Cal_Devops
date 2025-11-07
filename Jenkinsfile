// Jenkinsfile
pipeline {
    agent any

    tools {
        // This 'git' tool needs to be configured in Jenkins settings
        git 'Default'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Samyakjnz/Scientific_Cal_Devops.git', branch: 'main'
            }
        }

        stage('Build & Test') {
            steps {
                sh 'python3 -m unittest tester.py'
            }
        }

        stage('Containerize') {
            steps {
                script {
                    def dockerHubUsername = 'equador007'
                    def dockerHubRepo = 'scientific-calculator'
                    def fullImageName = "${dockerHubUsername}/${dockerHubRepo}"
                    
                    sh "docker build -t ${fullImageName} ."
                    
                    withCredentials([usernamePassword(credentialsId: 'Docker-hub-creds-id', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin"
                        sh "docker push ${fullImageName}"
                    }
                    
                }
            }
        }
    }
    
}