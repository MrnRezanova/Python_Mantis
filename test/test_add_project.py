from model.project import Project
import string
import random
import time

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = Project(name=random_string("name", 10))


def test_add_project(app):
    old_projects_number = app.project.get_projects_number()
    old_projects_list = app.project.get_projects()
    app.project.create(testdata)
    old_projects_list.append(testdata)
    new_projects_number = app.project.get_projects_number()
    assert old_projects_number + 1 == new_projects_number
    new_projects_list = app.project.get_projects()
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)
    list_project_from_soap = []
    for project in old_projects_list:
        id_from_soap = app.soap.get_id_project_from_name('administrator', 'root', project.name)
        list_project_from_soap.append(Project(name=project.name, id=str(id_from_soap)))
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(list_project_from_soap, key=Project.id_or_max)

