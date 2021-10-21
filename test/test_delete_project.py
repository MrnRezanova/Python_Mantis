from model.project import Project

def test_delete_project(app):
    if app.project.get_projects_number() == 0:
        app.project.create(Project(name="NewProject"))
    old_projects_number = app.project.get_projects_number()
    app.project.delete()
    new_projects_number = app.project.get_projects_number()
    assert old_projects_number -1 == new_projects_number