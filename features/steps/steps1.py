from behave import given,when,then
from selenium import webdriver

@given(u'Launch chrome browser')
def launchbrowser(context):
    context.driver = webdriver.Chrome(executable_path="E:\ecomm\bee\driver\chromedriver")


@when(u'Open ecom homepage')
def openhomepage(context):
    context.driver.get("https://admin-demo.nopcommerce.com/")


@then(u'Verify message on home page')
def verifymessage(context):
    status = context.driver.find_element_by_xpath("//*[contains(text(),'Welcome, please sign in!')]").is_displayed()
    assert status is True


@then(u'Close browser')
def closebrowser(context):
    context.driver.close()
