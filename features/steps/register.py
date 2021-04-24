import os

from behave import *
from selenium import webdriver


@given(u'Launch the Firefox browser')
def launchFirefox(context):
    FIREFOX_DRIVER = os.path.join('driver/geckodriver')
    context.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER)


@when(u'Open the register page')
def openRegister(context):
    context.driver.get("http://127.0.0.1:8000/register/")


@when(u'Input register username "{registerUser}" and register password "{registerPwd}"')
def registerInfo(context, registerUser, registerPwd):
    context.driver.find_element_by_name('username').send_keys(registerUser)
    context.driver.find_element_by_name('password').send_keys(registerPwd)
    context.driver.find_element_by_name('re_password').send_keys(registerPwd)


@when(u'Click on submit button')
def submitInfo(context):
    context.driver.find_element_by_xpath('/html/body/form/input[2]').click()


@then(u'User will be asked to login')
def closeBrowser(context):
    context.driver.close()
