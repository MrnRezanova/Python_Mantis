from model.project import Project
import string
import random


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = Project(name=random_string("name", 6))


def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    app.project.create(testdata)
    new_projects = app.project.get_project_list()
    assert old_projects + 1 == new_projects


