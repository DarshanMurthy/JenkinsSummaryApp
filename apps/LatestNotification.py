from jenkinsapi.jenkins import Jenkins
from slacker import Slacker

def getSCMInfroFromLatestGoodBuild(url, jobName, username=None, password=None):
    J = Jenkins(url, username, password)
    slack = Slacker('xoxp-2192405489-13339282129-16958704228-4847d229cf')
    job = J[jobName]
    lgb = job.get_last_good_build()
    print(lgb.get_revision())
    slack.chat.post_message('#core-devops',lgb, as_user=True)


if __name__ == '__main__':
   getSCMInfroFromLatestGoodBuild('http://scit-i-ec76021a:8080/', 'Test_My_Solar_City_15_12_C')