from sys import maxsize

class Viewstate:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.name is None or other.name is None or self.name == other.name)

class Status:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.name is None or other.name is None or self.name == other.name)

class Project:

    def __init__(self, name, status=None, viewstate=None, description=None, id=None):
        self.name = name
        self.status = status
        self.viewstate = viewstate
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.name == other.name) and \
               (self.status is None or other.status is None or self.status == other.status) and \
               (self.description is None or other.description is None or self.description == other.description)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

