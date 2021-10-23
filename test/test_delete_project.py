import random

from model.project import Project

def test_delete_project(app):
    if app.project.get_projects_number() == 0:
        app.project.create(Project(name="NewProject"))
    old_projects_list = app.project.get_projects()
    old_projects_number = app.project.get_projects_number()
    project = random.choice(old_projects_list)
    app.project.delete_by_id(project.id)
    old_projects_list.remove(project)
    new_projects_list = app.project.get_projects()
    new_projects_number = app.project.get_projects_number()
    assert old_projects_number -1 == new_projects_number
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)
    list_project_from_soap = []
    for project in old_projects_list:
        id_from_soap = app.soap.get_id_project_from_name('administrator', 'root', project.name)
        list_project_from_soap.append(Project(name=project.name, id=str(id_from_soap)))
    assert sorted(projects_list, key=Project.id_or_max) == sorted(list_project_from_soap, key=Project.id_or_max)