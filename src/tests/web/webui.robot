*** Settings ***
Resource  web_resource.robot

Suite Setup  Open And Configure Browser
Suite Teardown  Run Keywords  Delete Test User  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Open WebUi
    Open And Configure Browser
    Go To Main Page
    Create Test User And Login
    Welcome Page Should Be Open

Add Inproceedings Reference
    Select From List by Value  id=reference_type  inproceedings

    Input Reference  test_key1  test_author  test_title  2023

    Submit Reference

    Wait Until Page Contains Element  xpath=//tr[contains(@class,'referenceItem') and .//td[contains(text(),'test_key1')]]

Add Article Reference

    Select From List by Value  id=reference_type  article
    Input Reference  test_key2  test_author  test_title  2023

    Submit Reference

    Wait Until Page Contains Element  xpath=//tr[contains(@class,'referenceItem') and .//td[contains(text(),'test_key2')]]


Add Book Reference

    Select From List by Value  id=reference_type  book
    Input Reference  test_key3  test_author  test_title  2023

    Submit Reference

    Wait Until Page Contains Element  xpath=//tr[contains(@class,'referenceItem') and .//td[contains(text(),'test_key3')]]

List All References
    ${reference_count}=  Get Element Count  xpath=//tr[contains(@class,'referenceItem')]

    Should Be Equal As Integers  ${reference_count}  ${reference_count}

Remove Reference
    Set Selenium Implicit Wait  1s

    Run Keyword Until Success  Click Element  name=delete_test_key1
    Run Keyword Until Success  Click Element  name=delete_test_key2
    Run Keyword Until Success  Click Element  name=delete_test_key3

Show References As Bibtex
    Select From List by Value  id=reference_type  article
    Input Reference  test_key4  test_author  test_title  2023
    Submit Reference

    Run Keyword Until Success  Click Element  name=toggle_bibtex_on

    Wait Until Page Contains Element  xpath=//div[contains(@class,'referenceBibtex') and .//p[contains(text(),'@article{test_key4,')]]
    Run Keyword Until Success  Click Element  name=toggle_bibtex_off
    Run Keyword Until Success  Click Element  name=delete_test_key4

Download References
    Click Element    xpath=//form[@action="/download_references"]/button[@type="submit"]
    Wait Until File Exists    ${DOWNLOAD_PATH}${/}references.bib
    ${file_exists}    File Should Exist    ${DOWNLOAD_PATH}${/}references.bib

Website can be accessed
    Go To Website
    Login Page Should Be Open

Add Reference With Doi
    Input Doi    10.1002/chem.202000622
    Submit Doi
    Wait Until Page Contains Element  xpath=//tr[contains(@class,'referenceItem') and .//td[contains(text(),'Knittl_Frank_2020')]]
    Run Keyword Until Success  Click Element  name=delete_Knittl_Frank_2020
