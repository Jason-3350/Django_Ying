Feature: Register

    Scenario: Register with valid parameters
        Given Launch the Firefox browser
        When Open the register page
        And Input register username "bbb" and register password "111"
        And Click on submit button
        Then User will be asked to login