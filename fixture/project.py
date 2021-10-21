from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_manage_project_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            if len(wd.find_elements_by_xpath("//button[@id='menu-toggler']/span[3]")) > 0:
                wd.find_element_by_xpath("//button[@id='menu-toggler']/span[3]").click()
                wd.find_element_by_xpath("//*/text()[normalize-space(.)='Управление']/parent::*").click()
            else:
                wd.find_element_by_xpath("//*/text()[normalize-space(.)='Управление']/parent::*").click()
        wd.find_element_by_xpath("//a[contains(text(),'Управление проектами')]").click()

    def open_create_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*/text()[normalize-space(.)='Создать новый проект']/parent::*").click()

    def fill_create_project_form(self, project):
        wd = self.app.wd
        self.app.change_field_value("name", project.name)
        self.app.change_field_value("status", project.status)
        self.app.change_field_value("view_state", project.viewstate)
        self.app.change_field_value("description", project.description)

    def create(self, project):
        wd = self.app.wd
        self.open_manage_project_page()
        self.open_create_page()
        self.fill_create_project_form(project)
        wd.find_element_by_xpath("//input[@value='Добавить проект']").click()
        wd.find_element_by_xpath("//a[contains(text(),'Продолжить')]").click()


    def get_project_list(self):
        wd = self.app.wd
        self.open_manage_project_page()
        for element in wd.find_elements_by_xpath("//*[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table"):
            cells = element.find_elements_by_tag_name("tr")
        return len(cells)

    def delete(self):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_xpath("//div[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr/td/a").click()
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()