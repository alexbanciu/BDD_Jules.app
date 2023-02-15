from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(Browser):

    def wait_for_elem(self, selector):
        WebDriverWait(self.chrom, 5).until(EC.presence_of_element_located(*selector))