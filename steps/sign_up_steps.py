@given('sign_in: I am a user on jules sign in page')
def step_impl(context):



@when('sign_in: I click sign up button')
def step_impl(context):



@when('sign_up: I click personal radio button')
def step_impl(context):



@when('sign_up: I click the continue button')
def step_impl(context):



@when('sign_up: I type first name "Alex"')
def step_impl(context):



@when('sign_up: I click continue first name button')
def step_impl(context):

@when('sign_up: I set my email "abcd"')
def step_impl(context):



@then('sign_up: I recieve message: Please enter a valid email adress')
def step_impl(context):