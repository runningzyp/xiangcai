pipeline {
    agent xiangcai
        stage('Build') {
            steps {
                echo 'Building'
                sh 'docker build -t reg.xiangcaihua.cc/xiangcai/backend .'
                sh 'docker push reg.xiangcaihua.cc/xiangcai/backend'
            }
        }
        // stage('Test') {
        //     steps {
        //         echo 'Testing'
        //         sh 'mvn clean verify sonar:sonar' # 此处可以使用mvn test替代，笔者这步是检测代码的质量同步到自己的代码质量检测平台。
        //     }
        // }
        stage('Deploy') {
            steps {
                echo 'Deploying'
                // sh 'mvn clean deploy'  # 此处调用脚本或者ansible、saltstak，部署到远程
            }
        }
    }
}
