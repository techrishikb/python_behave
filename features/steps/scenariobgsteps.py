from behave import *
from selenium import webdriver


@given(u'Launch chrome browser for opening appliocation')
def launchbrowser(context):
    context.driver=webdriver.Chrome(executable_path="E:\\ecomm\\bee\\driver\\chromedriver")



@when(u'Open ecom homepage after launching url')
def launchurl(context):
    context.driver.get("https://admin-demo.nopcommerce.com/")


@then(u'Verify message displayed on home page')
def usernpass(context,user,pwd):
    text = context.driver.find_elelemt_by_xpath("//*[@class = 'content-header']").text()
    assert text == ""
    context.driver.close()


@then(u'Close the browser')
def clicklogin(context):
    context.driver.find_element_id("Login").click()



