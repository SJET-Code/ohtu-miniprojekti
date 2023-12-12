*** Settings ***
Library  ../../AppLibrary.py
Library  SeleniumLibrary
Library  ../FileOperations.py


*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0.5 seconds
${HOME_URL}  http://${SERVER}
${DOWNLOAD_PATH}    ${CURDIR}
${WEB_URL}  https://citeninja.fly.dev/
${REGISTER_URL}  ${HOME_URL}/register
${LOGIN_URL}  ${HOME_URL}/login
${DELETE_USER_URL}  ${HOME_URL}/delete_user

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    #Call Method    ${options}    add_argument    --no-sandbox
    #Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Welcome Page Should Be Open
    Title Should Be  CiteNinja

Login Page Should Be Open
    Title Should Be  Login

Go To Main Page
    Go To  ${HOME_URL}

Input Reference
    [Arguments]  ${key}  ${author}  ${title}  ${year}
    Input Text  name=ID  ${key}
    Input Text  name=author  ${author}
    Input Text  name=title  ${title}
    Input Text  name=year  ${year}


Submit Reference
    Click Button  Add Reference

Get Bibfile Path
    Click Element    xpath=//form[@action="/download_references"]/button[@type="submit"]
    Wait Until File Exists    ${DOWNLOAD_PATH}${/}references.bib
    ${file_exists}    File Should Exist    ${DOWNLOAD_PATH}${/}references.bib

Go To Website
    Go To  ${WEB_URL}

Go To Register Page
    Go To  ${REGISTER_URL}

Go To Login Page
    Go To  ${LOGIN_URL}

Submit Doi
    Click Button  Find

Input Doi
    [Arguments]  ${doi}
    Input Text  name=doiInput  ${doi}

Create Test User And Login
    Go To Register Page
    Input Text     name=username    test_user123
    Input Password    name=password_hash    Test_password123
    Click Button  register
    Go To Main Page

Delete Test User
    Go To  ${DELETE_USER_URL}