pipeline {
    agent { docker { image 'python:3.7' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pip install pipenv'
                sh 'pipenv install --dev'
                sh 'pipenv run nosetests'
            }
        }
    }
}
