import cherrypy
import os

#import pandas as pd


# import myprocessor

# p = myprocessor.MyProcessor()

class Home(object):


    def response(data):
        return {'key': 'value'}

    def sendChallengeBack(self, data):
        return data['challenge'];

    @cherrypy.expose
    def test(self):
        print("1")
        return "Hello from slackSimpleBot"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def index(self):
        print("2")
        data = cherrypy.request.json
        print(data)

        if data['type'] == 'url_verification':
            return self.sendChallengeBack(data)
        else:
            return "OK"


if __name__ == '__main__':

    def getPort():
        return(os.getenv('PORT', 8080))

    port = getPort()
    print("port", port)

    config = {'server.socket_host': '0.0.0.0', 'server.socket_port': int(getPort())}

    cherrypy.config.update(config)
    cherrypy.quickstart(Home())
