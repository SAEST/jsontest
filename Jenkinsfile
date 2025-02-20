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
    }
}
