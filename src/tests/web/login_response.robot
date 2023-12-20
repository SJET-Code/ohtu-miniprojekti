*** Settings ***
Resource  response_resource.robot

Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Login Page


*** Test Cases ***
Open WebUi
    Open And Configure Browser
    Go To Login Page
    Login Page Should Be Open

Login With Non Existant User
    Input User  testi  Seven777
    Submit Login
    
    Wait Until Page Contains Element  //div[contains(@class,'error') and contains(text(),'Wrong username or password')]


