Feature: checking products

    Scenario: check the product list
        Given launch firefox browser
        When open the homepage
        Then verify that the product is there
        And close browser
