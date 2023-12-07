*** Settings ***
Library  ../../AppLibrary.py
Library  SeleniumLibrary
Library  ../FileOperations.py


*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0.1 seconds
${HOME_URL}  http://${SERVER}
${DOWNLOAD_PATH}    ${CURDIR}
${WEB_URL}  https://citeninja.fly.dev/

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}
Welcome Page Should Be Open
    Title Should Be  CiteNinja

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
    Title Should Be  CiteNinja
