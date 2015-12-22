from slacker import Slacker
from jenkinsapi.jenkins import Jenkins

slack = Slacker('xoxp-2192405489-13339282129-16958704228-4847d229cf')
"""slack.chat.post_message('#devopscool', 'PythonClient to Notify you the latest build', as_user=True)"""
response = slack.users.list()
users = response.body['members']

print(users)