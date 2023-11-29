*** Settings ***
Library  ../AppLibrary.py
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0.5 seconds
${HOME_URL}  http://${SERVER}

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox

    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Welcome Page Should Be Open
    Title Should Be  Bibtex Web App

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


