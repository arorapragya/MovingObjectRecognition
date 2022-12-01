pipeline {
   agent any
   stages {
       stage('Build Code') {
           steps {
               bat """
               echo "Building Moving Object Detector"
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
