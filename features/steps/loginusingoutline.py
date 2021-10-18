from behave import *
from selenium import webdriver


@given(u'Browser is launched')
def launchbrowser(context):
    context.driver=webdriver.Chrome(executable_path="E:\ecomm\bee\driver\chromedriver")



@when(u'I launch ecom url')
def launchurl(context):
    context.driver.get("https://admin-demo.nopcommerce.com/")


@then(u'username "{user}" and password "{pwd}" is provided')
def usernpass(context,user,pwd):
    context.driver.find_element_id("Email").send_Keys(user)
    context.driver.find_elelemt_id("password").send_Keys(pwd)


@then(u'click login button')
def clicklogin(context):
    context.driver.find_element_id("Login").click()

@then(u'user is in the homepage')
def homepage(context):
    try:
        text=context.driver.find_elelemt_by_xpath("//*[@class = 'content-header']").text
    except:
        context.driver.close()
        assert False,"Test Failed"
    if text=="Dashboard":
        context.driver.close()
        assert True,"Test Passed"
