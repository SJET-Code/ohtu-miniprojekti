*** Settings ***
Resource  login_resource.robot

Suite Setup  Run Keywords  Open And Configure Browser  Create Test User
Suite Teardown  Close Browser
Test Setup  Go To Login Page

*** Test Cases ***
Open WebUi
    Open And Configure Browser
    Go To Login Page
    Welcome Page Should Be Open

Login With Correct Credentials
    Input User  test_user123  Test_password123
    Submit Login
    Title Should Be  CiteNinja
    Delete Test User
