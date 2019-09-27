pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'docker build -t reg.xiangcaihua.com/test/xiangcai/backend .'
                sh 'docker push reg.xiangcaihua.cc/test/xiangcai/backend'
            }
        }
        // stage('Test') {
        //     steps {
        //         echo 'Testing..'
        //     }
        // }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}