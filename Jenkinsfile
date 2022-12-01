pipeline {
    agent any
    stages {
        stage('Master Branch Deploy Code') {
            when {
                branch 'master'
            }
            steps {
                bat """
                echo "Building MOR from Master branch"
                """

                bat """
                echo "Deploying Code from Master branch"
                """
            }
        }
        stage('Develop Branch Deploy Code') {
            when {
                branch 'develop'
            }
            steps {
                bat """
                echo "Building MOR from Develop branch"
                """
                bat """
                echo "Deploying Code from Develop branch"
                """
           }
        }
    }
}
