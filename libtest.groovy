//library identifier: 'my-test-lib', retriever: modernSCM([$class: 'GitSCMSource', credentialsId: 'MyGit', remote: 'https://github.com/antman25/PipelineLib.git', traits: [gitBranchDiscovery()]])
@Library('my-test-lib') 
import org.antman.*


org.antman.MyUtil.staticFunc('blah')

/*def test()
{
    print ("test")
}*/

//print(antenv.getData())

//def a = new org.antman.MyClass()

//def request = libraryResource 'org/antman/env.json'
//print (request)

