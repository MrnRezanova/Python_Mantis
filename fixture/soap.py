from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app, id=None, name=None):
        self.app = app
        self.id = id
        self.name = name


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name)


    def can_login(self, username, password):
        client = Client(self.app.config['web']['baseUrl'] + "api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except:
            return False


    def get_projects(self):
        client = Client(self.app.config['web']['baseUrl'] + "api/soap/mantisconnect.php?wsdl")
        try:
            return client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['username'], self.app.config['webadmin']['password'])
        except:
            return False

