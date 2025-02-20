pipeline {
    agent any
    environment {
        VENV_DIR = '/var/jenkins_home/workspace/jsontest/venv'
    }
    stages {
        stage('Clean Up and Checkout ') {
            steps {
                //deleteDir()
                //Clonar el repositorio Git
                //git url: 'https://github.com/SAEST/scjn.git', branch: 'main'
                checkout scm
            }
        }
        stage('Install & Setup venv') {
            steps {
                sh "python3 -m venv ${VENV_DIR}"
            }
        }
        stage('Install Dependencies') {
            steps {
                // Activar el entorno virtual e instalar las dependencias
                sh """
                    . ${VENV_DIR}/bin/activate >  /dev/null 2>&1
                    pip install --no-cache-dir -r requirements.txt
                """
            }
        }
        stage('Ejecutar Script Actualizacion Json') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                sh """
                    . ${VENV_DIR}/bin/activate > /dev/null 2>&1
                    python jsoncron.py 
               """
                }
            }
        }
        post {
        always {
            script {
                def log = "${env.BUILD_URL}execution/node/3/ws/registro_actualizaciones.txt"

                env.BUILD_RESULT = currentBuild.currentResult
                // Convertir la duración a un formato legible
                def durationMillis = currentBuild.duration
                def durationSeconds = (durationMillis / 1000) as int
                def minutes = (durationSeconds / 60) as int
                def seconds = durationSeconds % 60
                env.BUILD_DURATION = "${minutes}m ${seconds}s"

                // Imprime las URLs en consola
                echo "Archivo log: ${log}"
                
                archiveArtifacts artifacts: '/registro_actualizaciones.txt', allowEmptyArchive: true

                sh """
                    . ${VENV_DIR}/bin/activate > /dev/null 2>&1
                    python3 utils/send_email.py ${env.BUILD_RESULT} ${env.BUILD_DURATION}
                """
            }
        }
    }
}
