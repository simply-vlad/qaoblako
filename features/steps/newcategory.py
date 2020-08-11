from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

@given(u'I launch Chrome')
def step_impl(context):
  chrome_option = webdriver.ChromeOptions()
  if os.environ.get('docker') == 'true':
    chrome_option.add_argument("headless")
    chrome_option.add_argument("--no-sandbox")
    chrome_option.add_argument("--disable-dev-shm-usage")
    context.browser = webdriver.Chrome(options=chrome_option)
  else:
    context.browser = webdriver.Chrome(options=chrome_option)


@when(u'open test page')
def step_impl(context):
    context.browser.get("http://qa-assignment.oblakogroup.ru/board/vlad_makarov#")


@then(u'click add button')
def step_impl(context):
    context.browser.find_element_by_id('add_new_todo').click()


@then(u'Change new category "Создать новый список"')
def step_impl(context):
    select = Select(context.browser.find_element_by_id('select_category'))
    select.select_by_visible_text("Создать новый список")


@then(u'Write name new category "{text2}"')
def step_impl(context,text2):
    context.browser.find_element_by_id('project_title').clear()
    context.browser.find_element_by_id('project_title').send_keys(text2)


@then(u'Write name new task "{text3}"')
def step_impl(context,text3):
    context.browser.find_element_by_id('project_text').clear()
    context.browser.find_element_by_id('project_text').send_keys(text3)

@then(u'push finish button')
def step_impl(context):
    context.browser.find_element_by_id("submit_add_todo").click()

@then(u'checking the correct of adding a category and task')
def step_impl(context):
    assert context.browser.find_element_by_css_selector(".container > div:nth-child(5) > div.shadow_todos > h2:last-of-type"), "Категория Работа QA добавлена"
    assert context.browser.find_element_by_css_selector(".container > div:nth-child(5) > div.shadow_todos > form:nth-child(17) > ul > table > tbody > tr  > td:nth-child(3) > label[id='7489']"), "Задача Я пытался1 добавлена"

@then(u'Write false name new category "{text0}"')
def step_impl(context,text0):
    context.browser.find_element_by_id('project_title').clear()
    context.browser.find_element_by_id('project_title').send_keys(text0)


@then(u'Write false name new task "{text01}"')
def step_impl(context,text01):
    context.browser.find_element_by_id('project_text').clear()
    context.browser.find_element_by_id('project_text').send_keys(text01)

@then(u'click finish button')
def step_impl(context):
    context.browser.find_element_by_id("submit_add_todo").click()

@then(u'checking the false of adding a category and task')
def step_impl(context):
    assert context.browser.find_element_by_css_selector(".container > div:nth-child(6) > div.shadow_todos > h2:last-of-type"), "Неверная пустая категория"
    assert context.browser.find_element_by_css_selector(".container > div:nth-child(6) > div.shadow_todos > form:nth-child(16) > ul > table > tbody > tr  > td:nth-child(3) > label[id='7490']"), "Неверная пустая задача"

@then(u'close Chrome browser')
def step_impl(context):
    time.sleep(5)
    context.browser.close()


