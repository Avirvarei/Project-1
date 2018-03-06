def run_tests(){
    sh 'tox -ejenkins || true'
}
def publish(){
    warnings canComputeNew: false, canResolveRelativePaths: false, categoriesPattern: '', defaultEncoding: '', excludePattern: '', healthy: '', includePattern: '', messagesPattern: '', parserConfigurations: [[parserName: 'Pep8', pattern: 'flake8_report.txt'],[parserName: 'PyLint', pattern: 'pylint_report.txt']], unHealthy: '', unstableTotalAll: '0'

    junit([allowEmptyResults: true, testResults: '**/junit_report.xml']);
                step([$class: 'CoberturaPublisher', autoUpdateHealth: false, autoUpdateStability: false,
                 coberturaReportFile: '**/coverage.xml', failUnhealthy: false,
                  failUnstable: false, maxNumberOfBuilds: 0, onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false]);

}

node() {
        stage('Clean'){
            deleteDir();
        }
        stage('Clone'){
            checkout([$class: 'GitSCM', branches: [[name: '$GERRIT_REFSPEC']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: env.CREDENTIALS, refspec: '+refs/heads/*:refs/remotes/origin/* +refs/tags/*:refs/tags/* +refs/changes/*:refs/changes/*', url: '$URL']]])
        }
        stage('Run tests'){
            run_tests();
        }
        stage('Publish test results'){
            publish();
        }
}