Feature: Add new category

  Background: common steps
    Given I launch Chrome
    When open test page
    Then click add button

  Scenario: add new category and new task
    And Change new category "Создать новый список"
    And Write name new category "Работа QA"
    And Write name new task "Я пытался"
    And push finish button

  Scenario: add new false category and new false task
    And Change new category "Создать новый список"
    And Write false name new category "   "
    And Write false name new task "   "
    And click finish button
    And close Chrome browser

