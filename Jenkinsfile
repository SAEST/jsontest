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
        stage('Ejecutar Test con Pytest, Selenium - POM') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                // pytest tests/test_public_page.py --html=reports/pytestreport/report2.html --self-contained-html --alluredir=reports/report
                //pytest tests/test_descarga_csv.py --html=reports/pytestreport/report1.html --self-contained-html --alluredir=reports/report
                //pytest_html_merger -i /var/jenkins_home/workspace/scjn/reports/pytestreport -o /var/jenkins_home/workspace/scjn/reports/pytestreport/report.html
                sh """
                    . ${VENV_DIR}/bin/activate > /dev/null 2>&1
                    python testjson.py 
               """
                }
            }
        }
    }
}
