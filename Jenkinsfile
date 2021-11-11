pipeline {
    agent {
        docker { image 'isaacfife/python-selenium-gecko:latest' }
    }

    stages {
        stage('Build') {
            steps {
                sh 'python --version'
                sh 'pip --version'
                sh 'pip list'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}
