import os

from behave import *
from selenium import webdriver


@given(u'I launch Firefox browser')
def launchPage(context):
    FIREFOX_DRIVER = os.path.join('driver/geckodriver')
    context.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER)


@when(u'I open the login page')
def openLoginPage(context):
    context.driver.get("http://127.0.0.1:8000/login/")


@when(u'Enter username "{user}" and password "{pwd}"')
def enterData(context, user, pwd):
    context.driver.find_element_by_name('username').send_keys(user)
    context.driver.find_element_by_name('password').send_keys(pwd)


@when(u'Click on login button')
def clickLogin(context):
    context.driver.find_element_by_name('submit').click()


@then(u'User must successfully login to the page')
def getStatus(context):
    text = context.driver.find_element_by_xpath('/html/body/ul/li[1]/a').text
    assert text == 'Wine - Semi Dry Riesling Vineland'
    context.driver.close()
