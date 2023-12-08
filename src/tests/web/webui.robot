*** Settings ***
Resource  web_resource.robot

Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Open WebUi
    Open And Configure Browser
    Go To Main Page
    Welcome Page Should Be Open

Add Inproceedings Reference
    Select From List by Value  id=reference_type  inproceedings

    Input Reference  test_key1  test_author  test_title  2023

    Submit Reference

    Wait Until Page Contains Element  xpath=//div[contains(@class,'referenceItem') and .//p[contains(text(),'test_key1')]]

Add Article Reference

    Select From List by Value  id=reference_type  article
    Input Reference  test_key2  test_author  test_title  2023

    Submit Reference

    Wait Until Page Contains Element  xpath=//div[contains(@class,'referenceItem') and .//p[contains(text(),'test_key2')]]


Add Book Reference

    Select From List by Value  id=reference_type  book
    Input Reference  test_key3  test_author  test_title  2023

    Submit Reference

    Wait Until Page Contains Element  xpath=//div[contains(@class,'referenceItem') and .//p[contains(text(),'test_key3')]]

List All References
    ${reference_count}=  Get Element Count  xpath=//div[contains(@class,'referenceItem')]

    Should Be Equal As Integers  ${reference_count}  ${reference_count}

Remove Reference
    Set Selenium Implicit Wait  1s

    Click Element  xpath=//div[contains(@class,'referenceItem') and .//p[contains(text(),'test_key1')]]//button
    Click Element  xpath=//div[contains(@class,'referenceItem') and .//p[contains(text(),'test_key2')]]//button
    Click Element  xpath=//div[contains(@class,'referenceItem') and .//p[contains(text(),'test_key3')]]//button

Show References As Bibtex
    Select From List by Value  id=reference_type  article
    Input Reference  test_key4  test_author  test_title  2023
    Submit Reference

    Click Element  xpath=//button[contains(text(), "Show references as bibtex")]

    Wait Until Page Contains Element  xpath=//div[contains(@class,'referenceBibtex') and .//p[contains(text(),'@article{test_key4,')]]

Download References
    Click Element    xpath=//form[@action="/download_references"]/button[@type="submit"]
    Wait Until File Exists    ${DOWNLOAD_PATH}${/}references.bib
    ${file_exists}    File Should Exist    ${DOWNLOAD_PATH}${/}references.bib

Website can be accessed
    Go To Website
    Welcome Page Should Be Open

Add Reference With Doi
    Input Doi    10.1002/chem.202000622
    Submit Doi
    Wait Until Page Contains Element  xpath=//div[contains(@class,'referenceItem') and .//p[contains(text(),'Knittl_Frank_2020')]]