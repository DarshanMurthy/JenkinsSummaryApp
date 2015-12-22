from flask import Flask
import requests
from flask import render_template
from operator import itemgetter
from slacker import Slacker
from jenkinsapi.jenkins import Jenkins

app = Flask(__name__)

 
@app.route('/')
def get_jenkins_stuff():
    try:
        # general apache url with lots of colors and jobs
        # url = "https://builds.apache.org/api/json?pretty=true"
        # LR builds
        #http://slc3win72:8080/
        #http://scit-i-ec76021a:8080/
        url = "http://scit-i-ec76021a:8080/api/json?pretty=true"
        response = requests.get(url)
        stuff = response.json()['jobs']
        # sort the array by the color tag (alphabetically)
        sorted_stuff = sorted(stuff, key=itemgetter('color'), reverse=True)

    except Exception, e:
        # it went wrong so send back some information for debug
        return render_template("error.html", error=e)

    return render_template("index.html", results=sorted_stuff)

@app.route("/search")
def get_search():
    slack = Slacker('xoxp-2192405489-13339282129-16958704228-4847d229cf')
    """ #coredevops #devopscool """
    url = "http://scit-i-ec76021a:8080/"
    jobName = 'Test_My_Solar_City_15_12_C'
    J = Jenkins(url)
    job = J[jobName]
    lgb = job.get_last_good_build()
  
    slack.chat.post_message('#core-devops', lgb, as_user=True)
    return render_template("search.html", results= "Darshan")




if __name__ == '__main__':
    app.run(host='localhost',port=8080 ,debug=True)
