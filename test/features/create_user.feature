Feature: User tries to register by him/her self
  after successful registration user logs in and verifies the login is successful
  after successful login user deletes his credentials

  Scenario: Registering user and verifying the user registration is successful
    Given user registers with given name "priya" and email "priyayarava2"
    When user is created with given name and email
    Then user validates user is created sucessfully