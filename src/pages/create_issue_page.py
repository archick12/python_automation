from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage

class CreateIssue(BasePage):

    def should_have_title(self):
        for i in range(3):
            try:
                __create_issue_title = self.browser.find_element(By.CSS_SELECTOR, "[title='Create Issue']").text
                if "Create Issue" in __create_issue_title:
                    break
            except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException):
                    time.sleep(self.sleepTimeForRetry['fast'])
                    i += 1

    def choose_the_project(self, project_name):
        wait = WebDriverWait(self.browser, self.wait)
        element = wait.until(EC.visibility_of_element_located((By.ID, 'project-field')))
        element.clear()
        element.send_keys(project_name)

    def click_create_issue_button(self):
        for i in range(3):
            try:
                __create_issue_button = WebDriverWait(self.browser, self.wait).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#create_link")))
                if __create_issue_button.is_displayed():
                   return __create_issue_button.click()

            except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException):
                time.sleep(self.sleepTimeForRetry['fast'])
                i += 1
                print("Couldn't find element. Retrying... " + str(i) + " attempt")

    def enter_summary_field(self, summary):
        for i in range(3):
            try:
                __enter_summary_field = WebDriverWait(self.browser, self.wait).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#summary")))
                __enter_summary_field.send_keys(summary)

            except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, ElementClickInterceptedException):
                time.sleep(self.sleepTimeForRetry['fast'])
                i +=1



    def enter_reporter(self):
        __reporter_field = self.browser.find_element(By.CSS_SELECTOR, "#reporter-field")
        __reporter_field.clear()
        __reporter_field.send_keys("webinar5")
        __reporter_field.send_keys(Keys.ENTER)

    def is_alert_present(self):
        for i in range(3):
            try:
                __issue = self.browser.find_element_by_css_selector(".aui-will-close")
                if __issue.is_displayed():
                    return __issue.text
            except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, ElementClickInterceptedException):
                time.sleep(self.sleepTimeForRetry['fast'])
                i += 1
