from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage

class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def exist_icon_username(self):
        try:
            self.find_element(locator='div.form_group > username')
        except NoSuchElementException:
            return False
        return True

    def exist_icon_password(self):
        try:
            self.find_element(locator='div.form_group > password')
        except NoSuchElementException:
            return False
        return True