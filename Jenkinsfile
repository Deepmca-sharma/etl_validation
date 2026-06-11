// Jenkinsfile
// ─────────────────────────────────────────────────
// PURPOSE: Tell Jenkins 3 things:
//   1. Where to get the code (from Git automatically)
//   2. How to install dependencies
//   3. Which Python script to run
// That's it. All real logic lives in run_tests.py
// ─────────────────────────────────────────────────

pipeline {
    agent any
    tools {
    jenkins.plugins.shiningpanda.tools.PythonInstallation 'Python3'
    }


    parameters {
        // This creates a dropdown in Jenkins UI
        // So you can choose which suite to run manually
        choice(
            name: 'TEST_SUITE',
            choices: ['all', 'sanity', 'regression', 'unit', 'bvt'],
            description: 'Pick which test suite to run'
        )
    }

    stages {

        stage('Get code from Git') {
            steps {
                checkout scm
                // scm = Source Control Management
                // This pulls your latest code from GitHub automatically
                // No URL needed here — Jenkins already knows it
                // from the job configuration you set up earlier
            }
        }

        stage('Install dependencies') {
            steps {
                // Installs everything in your requirements.txt
                // Same as typing: pip install -r requirements.txt
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run ETL pipeline') {
            steps {
                // Runs your pipeline.py first to generate
                // transformed_data.csv before tests check it
                bat 'python etl/pipeline.py'
            }
        }

        stage('Run tests') {
            steps {
                // This is the only important line —
                // calls YOUR Python script with the chosen suite
                // Example: python run_tests.py all
                bat "python run_tests.py ${params.TEST_SUITE}"
            }
        }
    }

    post {
        // These run after tests finish regardless of result
        always {
            // Reads reports/results.xml and shows
            // pass/fail counts in Jenkins dashboard
            junit allowEmptyResults: true,
                  testResults: 'reports/results.xml'
        }
        success { echo '✅ Build passed!' }
        failure { echo '❌ Build failed — check Console Output tab' }
    }
}