Feature: Purchase product

  Scenario: Purchase
    Given Open Firefox browser
    When login in the login page
    And Input username "aaa" and password "111"
    And Click on login
    And I chose one product
    And Enter the quantity of the product and submit
    And Open the basket page
    Then Product in the basket
