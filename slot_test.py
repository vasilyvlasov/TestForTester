import os
import unittest
from selenium import webdriver
from page.page_elements import SlotPage


# from selenium.common.exceptions import NoSuchElementException,ElementNotSelectableException
# from selenium.webdriver.support.ui import WebDriverWait


class TestForTester(unittest.TestCase):

    BASE_URL = "http://slotmachinescript.com/"

    def setUp(self):
        driver_location = "/Users/vasily_vlasov/PycharmProjects/TestForTesters/driver/chromedriver"
        os.environ['webdriver.chrome.driver'] = driver_location
        self.driver = webdriver.Chrome(driver_location)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.BASE_URL)
        self.slot = SlotPage(self.driver)

    def test_spin(self):
        self.slot.click_spin()
        self.assertEquals(self.slot.spin_button().is_enabled(), True)

    def test_bet_change(self):
        self.slot.raise_bet()
        self.slot.raise_bet()
        self.slot.click_spin()
        print("Current credits are: %s" % self.slot.credits_field().text)

    def test_winning_spin(self):
        while not self.slot.winning_indicator():
            bet = int(self.slot.current_bet().text)
            credits = int(self.slot.credits_field().text)
            self.slot.click_spin()
            if self.slot.winning_indicator() is True:
                last_win = int(self.slot.last_win_field().text)
                result = credits - bet + last_win
                new_credits = int(self.slot.credits_field().text)
                self.assertEquals(new_credits, result)

    def tearDown(self):
        self.driver.close()
