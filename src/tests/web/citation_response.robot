*** Settings ***
Resource  response_resource.robot

Suite Setup  Open Register Login And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page


*** Test Cases ***
Create user
    Open And Configure Browser
    Go To Register Page
    Input User  newUser  Seven777
    Submit Register
    Go To Login Page
    Input User  newUser  Seven777
    Submit Login
    Home Page Should Be Open

Add Incorrect Key Citation
    Home Page Should Be Open
    Select From List by Value  id=reference_type  inproceedings

    Input Reference  test_key1%%%%%  test_author  test_title  2023

    Click Element  name=add_ref

    Wait Until Page Contains Element  //div[contains(@class,'error') and contains(text(),'Citation key can only contain alphanumeric, "-", "_", and ":" characters')]

Add Incorrect Author Citation
    Home Page Should Be Open
    Select From List by Value  id=reference_type  inproceedings

    Input Reference  test_key1  test_author%%%%%  test_title  2023

    Click Element  name=add_ref

    Wait Until Page Contains Element  //div[contains(@class,'error') and contains(text(),'Author was invalid')]

Add Incorrect Title Citation
    Home Page Should Be Open
    Select From List by Value  id=reference_type  inproceedings

    Input Reference  test_key1  test_author  test_title%%%%%  2023

    Click Element  name=add_ref

    Wait Until Page Contains Element  //div[contains(@class,'error') and contains(text(),'Title was invalid')]



