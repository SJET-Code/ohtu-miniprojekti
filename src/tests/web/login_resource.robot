*** Settings ***
Resource  login_resource.robot

Library  ../../AppLibrary.py
Library  SeleniumLibrary
Library  RequestsLibrary

*** Variables ***
${SERVER}  localhost:5000/login
${DELAY}  0.1 seconds
${LOGIN_URL}  http://${SERVER}
${HOME_URL}  http://localhost:5000

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Welcome Page Should Be Open
    Title Should Be  Login

Go To Login Page
    Go To  ${LOGIN_URL}

Submit Login
    Click Button  login

Go To Main Page
    Go To  ${HOME_URL}
    
Input User
    [Arguments]    ${username}    ${password}
    Input Text     name=username    ${username}
    Input Password    name=password_hash    ${password}

