from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

@given(u'chrome browser')
def step_impl(context):
  chrome_option = webdriver.ChromeOptions()
  if os.environ.get('docker') == 'true':
    chrome_option.add_argument("headless")
    chrome_option.add_argument("--no-sandbox")
    chrome_option.add_argument("--disable-dev-shm-usage")
    context.browser = webdriver.Chrome(options=chrome_option)
  else:
    context.browser = webdriver.Chrome(options=chrome_option)

@when(u'page')
def step_impl(context):
    context.browser.get("http://qa-assignment.oblakogroup.ru/board/vlad_makarov#")


@then(u'use button add task')
def step_impl(context):
    context.browser.find_element_by_id('add_new_todo').click()


@then(u'new category "Создать новый список"')
def step_impl(context):
    select = Select(context.browser.find_element_by_id('select_category'))
    select.select_by_visible_text("Создать новый список")


@then(u'new category "{text11}"')
def step_impl(context,text11):
    context.browser.find_element_by_id('project_title').clear()
    context.browser.find_element_by_id('project_title').send_keys(text11)


@then(u'new task "{text12}"')
def step_impl(context,text12):
    context.browser.find_element_by_id('project_text').clear()
    context.browser.find_element_by_id('project_text').send_keys(text12)


@then(u'finish button')
def step_impl(context):
    context.browser.find_element_by_id("submit_add_todo").click()


@then(u'Check if a new task has been added to the old category')
def step_impl(context):
    assert context.browser.find_element_by_css_selector(".container > div:nth-child(2) > div.shadow_todos > form:nth-child(6) > ul > table > tbody > tr  > td > label[id='7498']"), "Новая задача добавлена в старую категорию"


@then(u'close')
def step_impl(context):
    time.sleep(5)
    context.browser.close()
