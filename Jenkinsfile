def appName = 'Flask-application'

pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'dilys243/flask-app'
        DOCKER_REGISTRY = 'dilys243/flask_docker_app'
        EC2_HOST = 'ubuntu@44.204.159.53'
        APP_PORT = '5000'
    }

    stages {
        stage('VCS Code Checkout') {
            steps {
                git url: 'https://github.com/Dilys-web/Docker.git', branch: 'main'
            }
        }

         stage('Install Packages') {
            steps {
                dir('Flask_app') {
                    script {
                        sh 'python3 -m venv venv'
                        sh '. venv/bin/activate && pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    dir('Flask_app') {
                        sh '''
                        . venv/bin/activate && coverage run -m unittest discover -s tests -p "*.py" && coverage xml
                        '''
                    }
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('My SonarQube Server') { 
                        withEnv(["JAVA_HOME=${tool 'jdk17'}", 
                            "PATH=${tool 'jdk17'}/bin:/opt/sonar-scanner/bin:${env.PATH}"]) {
                        dir('Flask_app') {
                            sh '''
                            sonar-scanner \
                            -Dsonar.projectKey=Flask-Application \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://139.162.172.244:9000 \
                            -Dsonar.qualitygate.wait=true \
                            -Dsonar.exclusions=venv/** \
                            -Dsonar.python.coverage.reportPaths=coverage.xml
                            '''
                    }
                }
            }
        }
            }
    }   

        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = "${DOCKER_IMAGE}:latest"
                    dir('Flask_app') {
                        sh "docker build -t ${dockerImage} ."
                    }
                }
            }
        }

        stage('Deploy Application to EC2 Instance') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-Cred', usernameVariable: 'DockerUsername',
                     passwordVariable: 'DockerPassword')]) {
                        sshagent(['ssh-key']) {
                            def ec2Instance = "${EC2_HOST}"
                            def dockerImage = "${DOCKER_IMAGE}:latest"
                            sh """
                            ssh -o StrictHostKeyChecking=no ${ec2Instance} '
                            echo ${DockerPassword} | docker login -u ${DockerUsername} --password-stdin &&
                            docker pull ${dockerImage} &&
                            docker stop ${appName} || true &&
                            docker rm ${appName} || true &&
                            docker run -d --name ${appName} -p ${APP_PORT}:${APP_PORT} ${dockerImage}
                            '
                            """
                        }
                     }
                }
            }
        }
    }

    post {
        success {
            echo 'Application deployed successfully!'
        }
        failure {
            echo 'Application deployment failed!'
        }
        always {
            cleanWs()
        }
    }
}
