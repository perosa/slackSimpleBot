import cherrypy
import pandas as pd


# import myprocessor

# p = myprocessor.MyProcessor()

class Home(object):


    def response(data):
        return {'key': 'value'}

    def sendChallengeBack(self, data):
        return data['challenge'];

    @cherrypy.expose
    def index(self):
        return "Hello from slackSimpleBot"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def bot(self):
        data = cherrypy.request.json
        print(data)

        if data['type'] == 'url_verification':
            return self.sendChallengeBack(data)
        else:
            return "OK"


if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(Home())
