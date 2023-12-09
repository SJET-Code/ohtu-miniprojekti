*** Settings ***
Resource  register_resource.robot

Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Open WebUi
    Open And Configure Browser
    Go To Register Page
    Welcome Page Should Be Open

Register With Correct Credentials
    Input User  testi  testiman123
    Submit Register
    Title Should Be  CiteNinja
    Delete User
