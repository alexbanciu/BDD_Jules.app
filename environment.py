from browser import Browser
from pages.sign_up_page import SignUpPage


def before_all(context):
    context.browser = Browser()
    context.sign_up_object = SignUpPage()


def after_all(context):
    context.browser.close()