Feature: Ecom welcome message using multiple parameters

  Scenario Outline: Welcome message present on homepage
    Given Launch chrome browser
    When Open ecom homepage
    Then Enter username "<username>" and password "<password>" to login
    And Close browser
    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |