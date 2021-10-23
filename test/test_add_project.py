from model.project import Project, Status, Viewstate
import string
import random
import time

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = Project(name=random_string("name", 10), status=Status(name="stable"), viewstate=Viewstate(name="public"))


def test_add_project(app):
    old_projects_number = app.project.get_projects_number()
    old_projects_list = app.project.get_projects()
    old_projects_from_soap = app.soap.get_projects('administrator', 'root')
    app.project.create(testdata)
    new_projects_number = app.project.get_projects_number()
    new_projects_list = app.project.get_projects()
    new_projects_from_soap = app.soap.get_projects('administrator', 'root')
    old_projects_list.append(testdata)
    old_projects_from_soap.append(testdata)
    assert old_projects_number + 1 == new_projects_number
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)
    for idx, project in enumerate(old_projects_from_soap):
        if project.id == new_projects_from_soap[idx].id:
            assert project.name ==new_projects_from_soap[idx].name
            assert project.status.name == new_projects_from_soap[idx].status.name
            assert project.view_state.name == new_projects_from_soap[idx].view_state.name
            assert project.description == new_projects_from_soap[idx].description



