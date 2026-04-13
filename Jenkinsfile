pipeline {
    agent any

    stages {
        stage('Setup Python (No Permission Needed)') {
            steps {
                sh '''
                if ! command -v python3 &> /dev/null
                then
                    echo "Downloading portable Python..."
                    wget https://www.python.org/ftp/python/3.9.19/Python-3.9.19.tgz
                    tar -xzf Python-3.9.19.tgz
                    cd Python-3.9.19
                    ./configure --prefix=$PWD/python-install
                    make -j2
                    make install
                    export PATH=$PWD/python-install/bin:$PATH
                    cd ..
                fi
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                export PATH=$PWD/Python-3.9.19/python-install/bin:$PATH
                python3 -m ensurepip
                python3 -m pip install --upgrade pip
                python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                export PATH=$PWD/Python-3.9.19/python-install/bin:$PATH
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