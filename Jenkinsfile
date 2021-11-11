pipeline {
    agent {
        docker { image 'isaacfife/python-selenium-gecko:latest' }
    }
    environment {
        PUSHOVER_API_TOKEN = credentials(params.PUSHOVER_API_TOKEN_CREDS_ID)
        PUSHOVER_USER_TOKEN = credentials(params.PUSHOVER_USER_TOKEN_CREDS_ID)
    }
    stages {
        stage('Check Stock and Notify') {
            steps {
                sh 'python main.py'
            }
        }
    }
}
