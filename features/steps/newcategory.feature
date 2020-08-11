Feature: Add new category

  Background: common steps
    Given I launch Chrome
    When open test page
    Then click add button

  Scenario: add new category and new task
    And Change new category "Создать новый список"
    And Write name new category "Работа QA"
    And Write name new task "Я пытался1"
    And push finish button
    And checking the correct of adding a category and task

  Scenario: add new false category and new false task
    And Change new category "Создать новый список"
    And Write false name new category "   "
    And Write false name new task "   "
    And click finish button
    And checking the false of adding a category and task
    And close Chrome browser

