Feature: Ecom Login

  Scenario: Login to ecom website
    Given Browser is launched
    When I launch ecom url
    Then username "admin@yourstore.com" and password "admin" is provided
    And click login button
    Then user is in the homepage


