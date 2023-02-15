Feature:Jules.app sign-up tests
  Background:
    Given sign_in: I am a user on jules sign in page

    Scenario: I create an account

      When sign_in: I click sign up button
      When sign_up: I click personal radio button
      When sign_up: I click the continue button
      When sign_up: I type first name "Alex"
      When sign_up: I click continue first name button
      When sign_up: I type last name "Banciu"
      When sign_up: I click continue first name button
      When sign_up: I set my email "abcd"
      Then sign_up: I recieve message: Please enter a valid email adress