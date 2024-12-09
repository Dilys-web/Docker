def appName = 'Flask-application'

   environment {
        DOCKER_IMAGE = "dilys243/flask-app" 
        DOCKER_REGISTRY = "dilys243/flask_docker_app" 
        EC2_HOST = "ubuntu@44.204.159.53"
        APP_PORT = "5000" 
            }

pipeline {
    agent any

    stages {
        stage('VCS Code Checkout') {
            steps {
                git url: 'https://github.com/Dilys-web/Docker.git', branch: 'main'
            }
        }

        stage('Code Testing') {
            steps {                l

                dir('Flask_app')
                sh 'pip install -r requirements.txt' 
                sh 'pytest'    
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = "${appName}:latest"
                    dir('Flask_app')
                    sh "docker build -t ${dockerImage} ."
                }
            }
        }

        stage('Deploy Application to EC2 Instance') {
            steps {
                     withCredentials([usernamePassword(credentialsId:'docker-Cred', usernamevariable:'DockerUsername',passwordVariable:
                     'DockerPassword')]){
                        
                    sshagent(['ssh-key']){  

                    def ec2Instance = 'ubuntu@44.204.159.53'
                    def dockerImage = 'flask_app:latest'
                    sh """
                    ssh -o StrictHostKeyChecking=no ${ec2Instance} '
                    echo ${DockerPassword} | docker login -u ${DockerUsername} --password-stdin && 
                        docker pull ${dockerImage} &&
                        docker stop ${appName} || true &&
                        docker rm ${appName} || true &&
                        docker run -d --name ${appName} -p 5000:5000 ${dockerImage}
                    '
                    """
                }
                
                }
            }
        }
    }

    post {

        success{
            echo 'Application deployed successfully!'        
            }

            failure{
                echo 'Application deployment failed!'
            }
        always {
            cleanWs()
        }
    }
}