from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

@given(u'launch chrome browser')
def step_impl(context):
  chrome_option = webdriver.ChromeOptions()
  if os.environ.get('docker') == 'true':
    chrome_option.add_argument("headless")
    chrome_option.add_argument("--no-sandbox")
    chrome_option.add_argument("--disable-dev-shm-usage")
    context.browser = webdriver.Chrome(options=chrome_option)
  else:
    context.browser = webdriver.Chrome(options=chrome_option)

@when(u'I open page')
def step_impl(context):
    context.browser.get("http://qa-assignment.oblakogroup.ru/board/vlad_makarov#")

@then(u'I click the add a new task button')
def step_impl(context):
    context.browser.find_element_by_id('add_new_todo').click()

@then(u'select category "Прочее"')
def step_impl(context):
    select=Select(context.browser.find_element_by_id('select_category'))
    select.select_by_visible_text("Прочее")

@then(u'add name task "{text1}"')
def step_impl(context,text1):
    context.browser.find_element_by_id('project_text').clear()
    context.browser.find_element_by_id('project_text').send_keys(text1)

@then(u'create new task')
def step_impl(context):
    context.browser.find_element_by_id("submit_add_todo").click()

@then(u'close browser')
def step_impl(context):
    time.sleep(5)
    context.browser.close()