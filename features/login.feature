Feature: Login

    Scenario: Login with valid parameters
        Given I launch Firefox browser
        When I open the login page
        And Enter username "aaa" and password "111"
        And Click on login button
        Then User must successfully login to the page