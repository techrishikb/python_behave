Feature: Ecommerce welcome message

  Background: common steps
    Given I launch browser
    When I open application
    And Enter valid Username and Password
    And click on login

  Scenario: Welcome message present on homepage of the application
    Given Launch chrome browser for opening appliocation
    When Open ecom homepage after launching url
    Then Verify message displayed on home page
    And Close the browser