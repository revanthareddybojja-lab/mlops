pipeline {
    agent {
        dockerfile true
    }

    stages {

        stage('Setup') {
            steps {
                echo 'Installing dependencies using Dockerfile'
            }
        }

        stage('Train') {
            steps {
                sh 'python train.py'
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