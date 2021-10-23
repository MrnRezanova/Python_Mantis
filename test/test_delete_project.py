import random

from model.project import Project

def test_delete_project(app):
    if app.project.get_projects_number() == 0:
        app.project.create(Project(name="NewProject"))
    old_projects_list = app.project.get_projects()
    old_projects_number = app.project.get_projects_number()
    old_projects_from_soap = app.soap.get_projects()
    project = random.choice(old_projects_from_soap)
    idx = old_projects_from_soap.index(project)
    app.project.delete_by_id(project.id)
    del old_projects_list[idx]
    old_projects_from_soap.remove(project)
    new_projects_list = app.project.get_projects()
    new_projects_number = app.project.get_projects_number()
    new_projects_from_soap = app.soap.get_projects()
    assert old_projects_number -1 == new_projects_number
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)
    for idx, project in enumerate(old_projects_from_soap):
        if project.id == new_projects_from_soap[idx].id:
            assert project.name ==new_projects_from_soap[idx].name
            assert project.status.name == new_projects_from_soap[idx].status.name
            assert project.view_state.name == new_projects_from_soap[idx].view_state.name
            assert project.description == new_projects_from_soap[idx].description
