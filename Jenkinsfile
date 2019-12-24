pipeline {
   agent any

   tools {
      maven "maven 3"
   }

   stages {
      stage('Build') {
         steps {
            // Start Selenium GRID
            sh '''
               java -jar selenium-server-standalone-3.141.59.jar -role hub -hubConfig hubConfig.json -debug &
               java -jar selenium-server-standalone-3.141.59.jar -role node -hub http://localhost:4444 &
               '''

            // Get some code from a GitHub repository
            git 'https://github.com/archick12/python_automation.git'

            // Install libraries
            sh '''
                    /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 -m venv venv
                    . venv/bin/activate
                    python3 -m pip install --ignore-installed -r requirements.txt
                    python3 -m pytest
                '''
         }
      }
   }
}