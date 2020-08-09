Feature: Task list

  Scenario: Add new task
    Given launch chrome browser
    When I open page
    Then I click the add a new task button
    And select category "Прочее"
    And add name task "Выжить"
    And create new task
    And close browser
