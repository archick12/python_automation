from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class CreateIssue(BasePage):

    def should_have_title(self):
        for i in range(3):
            try:
                __create_issue_title = self.browser.find_element(By.CSS_SELECTOR, "[title=\"Create Issue\"]").text
                if "Create Issue" in __create_issue_title:
                    break
            except (NoSuchElementException, StaleElementReferenceException):
                    time.sleep(5)
                    i += 1

    def choose_the_project(self, project_name):
         #type: (WebDriver) -> ()
        __project_field = self.browser.find_element(By.CSS_SELECTOR, "#project-field")
        __project_field.clear()
        __project_field.send_keys(project_name)
        __project_field.send_keys(Keys.ENTER)

    def click_create_issue_button(self):
        for i in range(3):
            try:
                __create_issue_button = self.browser.find_element(By.CSS_SELECTOR, "#create_link")
                if __create_issue_button.is_displayed():
                   return __create_issue_button.click()

            except (NoSuchElementException, StaleElementReferenceException):
                time.sleep(5)
                i += 1
                print("Couldn't find element. Retrying... " + str(i) + " attempt")

    def enter_summary_field(self):
        __summary_field = self.browser.find_element(By.CSS_SELECTOR, "#summary")
        __summary_field.clear()
        __summary_field.send_keys("UI bug In Jira")


    def enter_reporter(self):
        # type: (WebDriver) -> ()
        __reporter_field = self.browser.find_element(By.CSS_SELECTOR, "#reporter-field")
        __reporter_field.clear()
        __reporter_field.send_keys("webinar5")
        __reporter_field.send_keys(Keys.ENTER)

    def is_alert_present(self):
        for i in range(3):
            try:
                __issue = self.browser.find_element_by_css_selector(".aui-will-close")
                if __issue.is_displayed():
                    return str(__issue).text
            except (NoSuchElementException, StaleElementReferenceException):
                time.sleep(5)
                i += 1
