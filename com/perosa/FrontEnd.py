import cherrypy
import os

#import pandas as pd


# import myprocessor

# p = myprocessor.MyProcessor()

class Home(object):


    def response(data, msg):
        return {'text': msg}

    def sendChallengeBack(self, data):
        return data['challenge'];

    def getMessage(self, data):
        return data['event']['text']

    @cherrypy.expose
    def test(self):
        print("1")
        return "Hello from slackSimpleBot"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def index(self):

        data = cherrypy.request.json
        print(data)

        if data['type'] == 'url_verification':
            return self.sendChallengeBack(data)
        else:
            return self.response(self.getMessage(data))


if __name__ == '__main__':

    def getPort():
        return(os.getenv('PORT', 8080))

    port = getPort()
    print("port", port)

    config = {'server.socket_host': '0.0.0.0', 'server.socket_port': int(getPort())}

    cherrypy.config.update(config)
    cherrypy.quickstart(Home())
