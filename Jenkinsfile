pipeline {
    agent {
        docker { image 'isaacfife/python-selenium-gecko:latest' }
    }
    environment {
        PUSHOVER_API_TOKEN = credentials('pushover-api-token-creds-id')
        PUSHOVER_USER_TOKEN = credentials('pushover-user-token-creds-id')
    }
    stages {
        stage('Check Stock and Notify') {
            steps {
                sh 'python main.py'
            }
        }
    }
}
