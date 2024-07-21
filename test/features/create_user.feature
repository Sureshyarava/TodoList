Feature: User creation through api

  Scenario: Testing user creation though api call
    Given user is having "priya" , "priyayarava"
    When user is created with given name and email
    Then user gets a response saying user is successfully created