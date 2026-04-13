pipeline {
    agent any

    stages {
        stage('Setup Pip') {
            steps {
                sh '''
                python3 -m ensurepip --upgrade || true
                python3 -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python3 train.py'
            }
        }

        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: '*.pkl', fingerprint: true
            }
        }
    }
}