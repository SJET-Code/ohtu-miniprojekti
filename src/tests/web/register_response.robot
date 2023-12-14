*** Settings ***
Resource  response_resource.robot

Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page


*** Test Cases ***
Open WebUi
    Open And Configure Browser
    Go To Register Page
    Welcome Page Should Be Open

Register With Short Password
    Input User  testi  Seven77
    Submit Register
    
    Wait Until Page Contains Element  //div[contains(@class,'error') and contains(text(),'Password must be atleast 8 characters long')]

Register With Password Without Number
    Input User  testi  Sevennnn
    Submit Register
    
    Wait Until Page Contains Element  //div[contains(@class,'error') and contains(text(),'Password must contain a number')]

Register Without Lowercase Letter Password
    Input User  testi  SEVEN777
    Submit Register
    
    Wait Until Page Contains Element  //div[contains(@class,'error') and contains(text(),'Password must contain a lowercase letter')]

Register Without Uppercase Letter Password
    Input User  testi  seven777
    Submit Register
    
    Wait Until Page Contains Element  //div[contains(@class,'error') and contains(text(),'Password must contain a uppercase letter')]

