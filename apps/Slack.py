from slacker import Slacker
from jenkinsapi.jenkins import Jenkins

def getSCMInfroFromLatestGoodBuild(url, jobName, username=None, password=None):
	slack = Slacker('')
	""" #coredevops #devopscool """
    J = Jenkins(url, username, password)
    job = J[jobName]
    lgb = job.get_last_good_build()
    job_info = J.get_job_info(job)
    slack.chat.post_message('#coredevops', job_info, as_user=True)
    """return lgb.get_revision()"""




if __name__ == '__main__':
    print getSCMInfroFromLatestGoodBuild('', '')
