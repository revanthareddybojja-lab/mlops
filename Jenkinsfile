pipeline {
    agent any

    stages {

        stage('Setup') {
            steps {
                sh '''
                apt-get update
                apt-get install -y python3 python3-pip
                pip3 install --upgrade pip
                pip3 install -r requirements.txt
                '''
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