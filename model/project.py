

class Project:
    def __init__(self, name, status=None, viewstate=None, description=None):
        self.name = name
        self.status = status
        self.viewstate = viewstate
        self.description = description

    def __repr__(self):
        return "%s:%s;%s;%s" % (self.name, self.status, self.viewstate, self.description)