import os

from behave import *
from selenium import webdriver


@given(u'Open Firefox browser')
def openBrowser(context):
    FIREFOX_DRIVER = os.path.join('driver/geckodriver')
    context.driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER)


@when(u'login in the login page')
def loginPage(context):
    context.driver.get("http://127.0.0.1:8000/login/")


@when(u'Input username "{user}" and password "{pwd}"')
def inputData(context, user, pwd):
    context.driver.find_element_by_name('username').send_keys(user)
    context.driver.find_element_by_name('password').send_keys(pwd)


@when(u'Click on login')
def loginClickBtn(context):
    context.driver.find_element_by_name('submit').click()


@when(u'I chose one product')
def choseProduct(context):
    context.driver.find_element_by_xpath('/html/body/ul/li[1]/a').click()


@when(u'Enter the quantity of the product and submit')
def enterQuantity(context):
    context.driver.find_element_by_xpath('/html/body/form/input[3]').send_keys(10)
    context.driver.find_element_by_xpath('/html/body/form/input[4]').click()


@when(u'Open the basket page')
def openBasketPage(context):
    context.driver.get("http://127.0.0.1:8000/basket/")


@then(u'Product in the basket')
def getResult(context):
    status = context.driver.find_element_by_xpath('/html/body/p[2]').is_displayed()
    print(status)
    assert status is True
    context.driver.close()
