from model.project import Project

def test_delete_project(app):
    app.session.login("administrator", "root")
    print(app.project.get_project_list())
    if app.project.get_project_list() == 1:
        app.project.create(Project(name="NewProject"))
    old_projects = app.project.get_project_list()
    app.project.delete()
    new_projects = app.project.get_project_list()
    assert old_projects -1 == new_projects