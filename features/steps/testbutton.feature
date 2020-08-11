Feature: use add task button
  Scenario: wrong operation
    Given chrome
    When select category "Работа"
    Then Add a fake task "    "
    Then Testing button operation
    And finish
