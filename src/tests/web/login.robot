*** Settings ***
Resource  login_resource.robot

Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Login Page

*** Test Cases ***
Open WebUi
    Open And Configure Browser
    Go To Login Page
    Welcome Page Should Be Open

Login With Correct Credentials
    Input User  admin  password
    Submit Login
    Title Should Be  CiteNinja
