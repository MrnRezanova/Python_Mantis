from model.project import Project
import string
import random


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = Project(name=random_string("name", 6))


def test_add_project(app):
    old_projects_number = app.project.get_projects_number()
    app.project.create(testdata)
    new_projects_number = app.project.get_projects_number()
    assert old_projects_number + 1 == new_projects_number


