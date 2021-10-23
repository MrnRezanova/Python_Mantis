from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_manage_project_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            if len(wd.find_elements_by_xpath("//button[@id='menu-toggler']/span[3]")) > 0:
                wd.find_element_by_xpath("//button[@id='menu-toggler']/span[3]").click()
                wd.find_element_by_xpath("//*/text()[normalize-space(.)='Manage']/parent::*").click()
            else:
                wd.find_element_by_xpath("//*/text()[normalize-space(.)='Manage']/parent::*").click()
        wd.find_element_by_xpath("//a[contains(text(),'Manage Projects')]").click()

    def open_create_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*/text()[normalize-space(.)='Create New Project']/parent::*").click()

    def fill_create_project_form(self, project):
        wd = self.app.wd
        self.app.change_field_value("name", project.name)
        self.app.change_droplist_value("status", project.status.name)
        self.app.change_droplist_value("view_state", project.viewstate.name)
        self.app.change_field_value("description", project.description)

    def create(self, project):
        wd = self.app.wd
        self.open_manage_project_page()
        self.open_create_page()
        self.fill_create_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        wd.find_element_by_xpath("//a[contains(text(),'Proceed')]").click()
        self.project_cache = None

    def get_projects_number(self):
        wd = self.app.wd
        self.open_manage_project_page()
        return len(wd.find_elements_by_xpath("//*[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr"))

    def delete(self):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_xpath("//div[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr/td/a").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=%s')]" % id).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None

    project_cache = None

    def get_projects(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_project_page()
            self.project_cache = []
            for element in wd.find_elements_by_xpath("//*[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr"):
                row = element.find_elements_by_tag_name("td")
                name = row[0].text
                id = row[0].find_element_by_link_text(name).get_attribute("href").split("project_id=")[1]
                self.project_cache.append(Project(name=name, id=id))
        return list(self.project_cache)