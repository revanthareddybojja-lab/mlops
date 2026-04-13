pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo 'Starting ML Pipeline'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python train.py'
            }
        }

        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: '*.pkl', fingerprint: true
            }
        }
    }
}