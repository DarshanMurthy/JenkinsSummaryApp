from flask import Flask
import time
import requests
import jenkinsapi
from jenkinsapi.jenkins import Jenkins
from flask import render_template
from operator import itemgetter
from jenkinsapi.jenkins import Jenkins
SERVER = 'http://scit-i-ec76021a:8080/'

class JenkinsStuff:
    def Jenkins(self):
    	url = "http://slc3win72:8080/api/json?pretty=true"
        response = requests.get(url)
        stuff = response.json()['jobs']
        # sort the array by the color tag (alphabetically)
        sorted_stuff = sorted(stuff, key=itemgetter('color'), reverse=True)
        print(sorted_stuff)
        print("Hello I'm just awesome!")
        """ Juno pod would like to see what version of MySolarCity is up on production """
    def JunoProducation(self):
        print("Juno Producation")
        server = Jenkins(SERVER)
        MySolarCity ='Test_My_Solar_City_15_12_C'
        for job in server:
            print "Exist"



        




if __name__ == '__main__':
	Data = JenkinsStuff()
	Data.Jenkins()



 
	
