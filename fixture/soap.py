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
        client = Client('http://localhost/mantisbt-2.25.2/api/soap/mantisconnect.php?wsdl')
        try:
            client.service.mc_login(username, password)
            return True
        except:
            return False


    def get_id_project_from_name(self, username, password, name):
        client = Client('http://localhost/mantisbt-2.25.2/api/soap/mantisconnect.php?wsdl')
        try:
            return client.service.mc_project_get_id_from_name(username, password, name)
        except:
            return False


