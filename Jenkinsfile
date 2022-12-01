pipeline {
   agent any
   stages {
       stage('Build Code') {
           steps {
               bat """
               echo "Building Artifact"
               """
           }
       }
      stage('Deploy Code') {
          steps {
               bat """
               echo "Deploying Code"
               """
          }
      }
   }
}
