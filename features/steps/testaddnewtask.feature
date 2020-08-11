Feature: Task list

  Scenario: Add new task
    Given launch chrome browser
    When I open page
    Then I click the add a new task button
    And select category "Прочее"
    And add name task "Тест2"
    And create new task
    And checking the correct of adding a category
    And close browser
