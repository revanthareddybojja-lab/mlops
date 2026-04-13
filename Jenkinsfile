pipeline {
    agent any

    stages {

        stage('Setup') {
            steps {
                echo 'No dependencies required'
            }
        }

        stage('Train') {
            steps {
                sh '''
                docker run --rm -v $(pwd):/app -w /app python:3.9 \
                python train.py
                '''
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