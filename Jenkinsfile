pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'docker build -t reg.xiangcaihua.com/xiangcai/backend .'
                sh 'docker push reg.xiangcaihua.com/xiangcai/backend'
            }
        }
        // stage('Test') {
        //     steps {
        //         echo 'Testing..'
        //     }
        // }
        stage('Deploy') {
            steps {
                sh 'docker pull reg.xiangcaihua.com/xiangcai/backend'
                sh 'docker rm -f xiangcai'
                sh 'docker run --name=xiangcai -idt -p 5000:80 reg.xiangcaihua.com/xiangcai/backend'
            }
        }
    }
}