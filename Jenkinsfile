
pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }
        stage('Remove Old Docker Container') {
            steps {
                script {
                    containerExists = sh ( script: "docker ps -a | grep ${CONTAINER_NAME}", returnStatus: true)
                    
                    if (!containerExists) {
                        containerIsRunning = sh (script: "docker container inspect -f '{{.State.Running}}' ${CONTAINER_NAME}", returnStatus: true)
                        
                        if (!containerIsRunning) {
                            sh "docker stop ${CONTAINER_NAME}"
                        }
                        
                        sh "docker rm ${CONTAINER_NAME}"
                    }
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                sh "docker run -d -e API_URL=${API_URL} -e DISCORD_TOKEN=${DISCORD_TOKEN} --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest"
            }
        }
    }
}