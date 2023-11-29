*** Settings ***
Resource  web_resource.robot

Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Open WebUi
    Welcome Page Should Be Open

Add Inproceedings Reference 
    Open Browser  ${HOME_URL}  chrome
    Maximize Browser Window

    Select From List by Value  id=reference_type  inproceedings

    Input Reference  test_key  test_author  test_title  2023

    Submit Reference

    Wait Until Page Contains Element  xpath=//div[contains(@class,'referenceItem') and .//p[contains(text(),'test_key')] and .//p[contains(text(),'test_author')] and .//p[contains(text(),'test_title')] and .//p[contains(text(),'2023')]]

Add Article Reference 

    Select From List by Value  id=reference_type  article
    Input Reference  test_key  test_author  test_title  2023

    Submit Reference

    Wait Until Page Contains Element  xpath=//div[contains(@class,'referenceItem') and .//p[contains(text(),'test_key')] and .//p[contains(text(),'test_author')] and .//p[contains(text(),'test_title')] and .//p[contains(text(),'2023')]]

Add Book Reference

    Select From List by Value  id=reference_type  book
    Input Reference  test_key  test_author  test_title  2023

    Submit Reference

    Wait Until Page Contains Element  xpath=//div[contains(@class,'referenceItem') and .//p[contains(text(),'test_key')] and .//p[contains(text(),'test_author')] and .//p[contains(text(),'test_title')] and .//p[contains(text(),'2023')]]


List All References
    ${reference_count}=  Get Element Count  xpath=//div[contains(@class,'referenceItem')]

    Should Be Equal As Integers  ${reference_count}  3

Remove Reference
    Set Selenium Implicit Wait  1s
    
    Click Element  xpath=//div[contains(@class,'referenceItem') and .//p[contains(text(),'test_key')]]//button

    Close Browser
    