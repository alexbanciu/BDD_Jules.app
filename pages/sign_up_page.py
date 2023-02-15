from pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class SignUpPage(BasePage):
    SIGN_UP = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[4]/a')
    PERSONAL_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]/label/span[2]/span')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[5]/button/span[1]')
    INPUT_CONTINUE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[3]')
    INPUT = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')

    def navigate_to_sign_in_page(self):
        self.chrom.get('https://jules.app/sign-in')

    def navigate_to_sign_up_page(self):
        self.chrom.find_element(*self.SIGN_UP).click()

    def click_personal_button(self):
        self.chrom.find_element(*self.PERSONAL_BUTTON).click()

    def click_continue_button(self):
        self.chrom.find_element(*self.CONTINUE_BUTTON).click()

    def type_first_name(self):
        self.chrom.find_element(*self.INPUT).send_keys('Alex')

    def click_continue_first_name_button(self):
        self.chrom.find_element(*self.INPUT_CONTINUE_BUTTON).click()

    def type_last_name(self):
        self.chrom.find_element(*self.INPUT).send_keys('Banciu')

    def click_continue_last_name_button(self):
        self.chrom.find_element(*self.INPUT_CONTINUE_BUTTON).click()

    def type_email(self):
        self.chrom.find_element(*self.INPUT).send_keys('abcd@1234')

    def click_continue_email_button(self):
        self.chrom.find_element(*self.INPUT_CONTINUE_BUTTON).click()

    def check_error_message_email(self):
        expected = "Please enter a valid email address."
        actual = self.chrom.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/p')