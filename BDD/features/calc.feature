#  language : en



Feature: Calculator
    Scenario: Sum
        When I add "2" to "2"
        Then the result must be "4"

    Scenario: Sum with float
        When I add "2.0" to "2.0"
        Then the result must be "4.0"

