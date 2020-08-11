Feature: Old task
  Scenario: Add old task
    Given chrome browser
    When page
    Then use button add task
    And new category "Создать новый список"
    And new category "Работа"
    And new task "Потеть"
    And finish button
    And Check if a new task has been added to the old category
    And close
