from selenium.common.exceptions import NoSuchElementException,ElementNotSelectableException
from selenium.webdriver.support.ui import WebDriverWait


class SlotPage():

    def __init__(self, driver):
        self.driver = driver

    def spin_button(self):
        element = self.driver.find_element_by_id("spinButton")
        return element

    def click_spin(self):
        try:
            self.spin_button().click()
        except ElementNotSelectableException:
            self.driver.quit()
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id("spinButton").get_attribute("class") != "disabled"
        )

    def raise_bet(self):
        element = self.driver.find_element_by_id("betSpinUp")
        try:
            element.click()
        except ElementNotSelectableException:
            self.driver.quit()

    def lower_bet(self):
        element = self.driver.find_element_by_id("betSpinDown")
        try:
            element.click()
        except ElementNotSelectableException:
            self.driver.quit()

    def credits_field(self):
        try:
            element = self.driver.find_element_by_id("credits")
            return element
        except NoSuchElementException:
            self.driver.quit()

    def last_win_field(self):
        try:
            element = self.driver.find_element_by_id("lastWin")
            return element
        except NoSuchElementException:
            self.driver.quit()

    def current_bet(self):
        try:
            element = self.driver.find_element_by_id("bet")
            return element
        except NoSuchElementException:
            self.driver.quit()

    def winning_indicator(self):
        element = self.driver.find_element_by_id("SlotsOuterContainer")
        if element.get_attribute("class") == "won":
            return True
        return False