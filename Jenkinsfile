pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
    post { 
        always { 
            echo 'post Hello World'
        }
    }
}
