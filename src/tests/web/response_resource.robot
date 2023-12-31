*** Settings ***
Library  ../../AppLibrary.py
Library  SeleniumLibrary
Library  RequestsLibrary

*** Variables ***
${REGISTER_SERVER}  localhost:5000/register
${LOGIN_SERVER}  localhost:5000/login
${DELAY}  0.3 seconds
${REGISTER_URL}  http://${REGISTER_SERVER}
${LOGIN_URL}  http://${LOGIN_SERVER}
${HOME_URL}  http://localhost:5000

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Open Register Login And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}



Register Login And Go To Home Page
    Go To  ${REGISTER_URL}
    Input User  newUser  Seven777
    Submit Register
    Go To  ${LOGIN_URL}
    Input User  newUser  Seven777
    Submit Login

Go To Register Page
    Go To  ${REGISTER_URL}

Go To Login Page
    Go To  ${LOGIN_URL}

Go To Home Page
    Go To  ${HOME_URL}

Register Page Should Be Open
    Title Should Be  CiteNinja Register

Login Page Should Be Open
    Title Should Be  CiteNinja Login

Home Page Should Be Open
    Title Should Be  CiteNinja

Submit Register
    Click Element  name=register

Submit Login
    Click Element  name=login

Input User
    [Arguments]    ${username}    ${password}
    Input Text     name=username    ${username}
    Input Password    name=password_hash    ${password}

Input Reference
    [Arguments]  ${key}  ${author}  ${title}  ${year}
    Input Text  name=ID  ${key}
    Input Text  name=author  ${author}
    Input Text  name=title  ${title}
    Input Text  name=year  ${year}