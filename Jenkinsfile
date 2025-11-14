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

        stage('Deploy via Ansible in WSL2') {
    steps {
        sh '''
            export LANG=en_US.UTF-8
            export LC_ALL=en_US.UTF-8
            export PATH="$HOME/.local/bin:$PATH"

            ansible-playbook deploy_playbook.yml
        '''
    }
}

        



    }   
}


