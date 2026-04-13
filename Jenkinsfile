pipeline {
    agent any

    stages {

        stage('Setup') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train') {
            steps {
                sh 'python3 train.py || python train.py'
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