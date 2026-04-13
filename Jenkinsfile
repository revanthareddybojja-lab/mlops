pipeline {
    agent any

    stages {

        stage('Setup') {
            steps {
                sh 'python3 --version || true'
                sh 'python3 -m ensurepip || true'
                sh 'python3 -m pip install --user --upgrade pip'
                sh 'python3 -m pip install --user -r requirements.txt'
            }
        }

        stage('Train') {
            steps {
                sh 'python3 train.py'
            }
        }

        stage('Identity') {
            steps {
                echo 'Student: P. Revanth Reddy | Roll No: L22BCS016'
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'model.pkl, metrics.json'
            }
        }
    }
}