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
${REGISTER_URL}  ${HOME_URL}/register

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Welcome Page Should Be Open
    Title Should Be  CiteNinja Login

Go To Login Page
    Go To  ${LOGIN_URL}

Go To Register Page
    Go To  ${REGISTER_URL}

Submit Login
    Click Element  name=login

Submit Logout
    Go To  ${HOME_URL}/logout

Go To Main Page
    Go To  ${HOME_URL}
    
Input User
    [Arguments]    ${username}    ${password}
    Input Text     name=username    ${username}
    Input Password    name=password_hash    ${password}

Create Test User
    Go To Register Page
    Input Text     name=username    test_user123
    Input Password    name=password_hash    Test_password123
    Click Element  xpath=//html/body/form/div[2]/div[1]/input
    Submit Logout
    Welcome Page Should Be Open

Delete Test User
    Go To  ${HOME_URL}/delete_user
