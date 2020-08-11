from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

@given(u'chrome')
def step_impl(context):
    chrome_option = webdriver.ChromeOptions()
    if os.environ.get('docker') == 'true':
        chrome_option.add_argument("headless")
        chrome_option.add_argument("--no-sandbox")
        chrome_option.add_argument("--disable-dev-shm-usage")
        context.browser = webdriver.Chrome(options=chrome_option)
    else:
        context.browser = webdriver.Chrome(options=chrome_option)


@when(u'select category "Работа"')
def step_impl(context):
    context.browser.get("http://qa-assignment.oblakogroup.ru/board/vlad_makarov#")
    context.browser.find_element_by_id('add_new_todo').click()
    select = Select(context.browser.find_element_by_id('select_category'))
    select.select_by_visible_text("Работа")

@then(u'Add a fake task "{text000}"')
def step_impl(context,text000):
    context.browser.find_element_by_id('project_text').send_keys(text000)


@then(u'Testing button operation')
def step_impl(context):
    context.browser.find_element_by_id("submit_add_todo").click()
    assert context.browser, f"Кнопка не должна быть доступна"

@then(u'finish')
def step_impl(context):
    time.sleep(5)
    context.browser.close()
