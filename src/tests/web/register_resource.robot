*** Settings ***
Library  ../../AppLibrary.py
Library  SeleniumLibrary
Library  RequestsLibrary

*** Variables ***
${SERVER}  localhost:5000/register
${DELAY}  0.1 seconds
${REGISTER_URL}  http://${SERVER}
${HOME_URL}  http://localhost:5000

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Go To Register Page
    Go To  ${REGISTER_URL}

Welcome Page Should Be Open
    Title Should Be  Register

Submit Register
    Click Button  register

Go To Main Page
    Go To  ${HOME_URL}

Input User
    [Arguments]    ${username}    ${password}
    Input Text     name=username    ${username}
    Input Password    name=password_hash    ${password}

