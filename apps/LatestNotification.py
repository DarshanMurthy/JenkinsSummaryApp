from jenkinsapi.jenkins import Jenkins
from slacker import Slacker

def getSCMInfroFromLatestGoodBuild(url, jobName, username=None, password=None):
    J = Jenkins(url, username, password)
    slack = Slacker('')
    job = J[jobName]
    lgb = job.get_last_good_build()
    print(lgb.get_revision())
    slack.chat.post_message('#core-devops',lgb, as_user=True)


if __name__ == '__main__':
   getSCMInfroFromLatestGoodBuild('', '')
