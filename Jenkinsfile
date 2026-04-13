pipeline {
    agent any

    stages {
        stage('Setup Pip (No Permission Needed)') {
            steps {
                sh '''
                python3 - <<EOF
import urllib.request
url = "https://bootstrap.pypa.io/get-pip.py"
urllib.request.urlretrieve(url, "get-pip.py")
EOF

                python3 get-pip.py --user
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                export PATH=$HOME/.local/bin:$PATH
                pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                export PATH=$HOME/.local/bin:$PATH
                python3 train.py
                '''
            }
        }

        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: '*.pkl', fingerprint: true
            }
        }
    }
}