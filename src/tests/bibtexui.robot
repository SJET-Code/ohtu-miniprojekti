*** Settings ***
Resource  resource.robot
Test Setup  Reset
Library    Process

*** Test Cases ***
Add Article Reference
    Go To Input Article
    Input Reference  test_key  test_author  test_title  2023
    Run App And Stop
    Output Should Contain  Added an article test_key, titled test_title (2023), by test_author

List All References
    Add Test Reference Potter
    Choose To List All References
    Run App And Stop
    Output Should Contain  \nID: HP1\nTitle: Harry Potter\nAuthor: J.K. Rowling\nYear: 1997\nReference type: book\n

Remove Reference From List With Key
    Add Test Reference Potter
    Delete Reference With Key  HP1
    Run App And Stop
    Reset Outputs
    Choose To List All References
    Run App And Stop
    Output Should Not Contain  \nID: HP1\nTitle: Harry Potter\nAuthor: J.K. Rowling\nYear: 1997\nReference type: book\n

Remove All References From List
    Add Test Reference Potter
    Delete All References
    Choose To List All References
    Run App And Stop
    Output Should Contain  \nNo Citations Found\n

Filter References
    Add Test Reference Potter
    Choose To List References By Title
    Run App And Stop
    Output Should Contain    \nID: HP1\nTitle: Harry Potter\nAuthor: J.K. Rowling\nYear: 1997\nReference type: book\n

Add Reference With DOI
    Go To Input Doi
    Input Doi    10.1002/chem.202000622
    Run App And Stop
    Output Should Contain  Added an article successfully
