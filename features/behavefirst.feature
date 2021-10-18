Feature: Ecom welcome message

  Scenario: Welcome message present on homepage
    Given Launch chrome browser
    When Open ecom homepage
    Then Verify message on home page
    And Close browser