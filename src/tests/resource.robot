*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Reset
    Reset Bibtexfile

Input Reference
    [Arguments]  ${key}  ${author}  ${title}  ${year}
    Input  ${key}
    Input  ${author}
    Input  ${title}
    Input  ${year}

Add Test Reference Potter
    Go To Input Book
    Input Reference  HP1  J.K. Rowling  Harry Potter  1997

Run App And Stop
    Input  5
    Start

Go To Input Article
    Input  1
    Input  2

Go To Input Book
    Input  1
    Input  3

Choose To List All References
    Input  2
    Input  5

Delete Reference With Key
    [Arguments]  ${key}
    Input  3
    Input  ${key}

Delete All References
    Input  3
    Input  DELALL