pipeline {
    agent {
        docker { image 'isaacfife/python-selenium-gecko:latest' }
    }

    stages {
        stage('Check Stock and Notify') {
            steps {
                sh 'python main.py'
            }
        }
    }
}
