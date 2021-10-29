*** Settings ***
Documentation       Get data from web site.
Variables           m.py
Library             SeleniumLibrary
Library             m.py

*** Variables ***
${SERVER}		https://www.aihitdata.com/
${BROWSER}		Firefox

*** Tasks ***
Open Start Page
    Open Start Page
Login
    Login
Search Companies
    Search Companies
Get Companies Info
    Get Companies Info

*** Keywords ***
Open Start Page
    Open Browser		${SERVER}		${BROWSER}
    Start Page Should Be Open

Login
    Click Link		LOG IN
    Input Email		zimorodokan@gmail.com
    Input Password		111111
    Submit Credentials

Input Email
    [Arguments]		${email}
    Input Text		email		${email}

Input Password
    [Arguments]		${password}
    Input Text		password		${password}

Submit Credentials
    Click Button		submit

Start Page Should Be Open
    Location Should Be		${SERVER}
    Title Should Be			The Company Database | aiHit

Input Country
    [Arguments]		${location}
    Input Text		location		${location}

Input Industry
    [Arguments]		${industry}
    Input Text		industry		${industry}

Search Companies
    Input Country		US
    Input Industry		mortgage
    Click Button		Search

Get Companies Pages Urls
    ${search_links}		Get WebElements		css:.col-md-8 .panel-body .panel-body div a
    ${pages_links_list}		Create Pages Links List		${search_links}
    Log			${pages_links_list}
    [Return]			${pages_links_list}

Get Companies Info
    @{company_links} =    Get Companies Pages Urls
    FOR    ${company}    IN    @{company_links}
        ${company_name} =    Set Variable    ${company}[0]
        ${page_link} =    Set Variable    ${company}[1]
        Go To    ${page_link}


        ${e} =    Get WebElements    //i[@class="icon-sm icon-map-marker"]/..
        ${l} =    Get Length    ${e}
        IF    ${l} == 0
            ${company_address} =    Set Variable
        ELSE
            ${company_address} =    Get Text    ${e}[0]
        END


        ${e} =    Get WebElements    xpath://i[@class="icon-sm icon-home"]/../a
        ${l} =    Get Length    ${e}
        IF    ${l} == 0
            ${company_url} =    Set Variable
        ELSE
            ${company_url} =    Get Element Attribute    ${e}[0]    href
        END


        ${e} =    Get WebElements    xpath://i[@class="icon-sm icon-email"]/../a
        ${l} =    Get Length    ${e}
        IF    ${l} == 0
            ${company_email} =    Set Variable
        ELSE
            ${company_email} =    Get Text    ${e}[0]
        END


        ${e} =    Get WebElements    xpath://i[@class="icon-sm icon-phone"]/..
        ${l} =    Get Length    ${e}
        IF    ${l} == 0
            ${company_phone} =    Set Variable
        ELSE
            ${company_phone} =    Get Text    ${e}[0]
        END



        &{company_data} =    Set Variable    ${{{'name': '${company_name}', 'address': '${company_address}', 'url': '${company_url}', 'email': '${company_email}', 'phone': '${company_phone}'}}}
        Append Data    ${company_data}
    END
    Evaluate    print(@{output})
    [Return]    @{output}
    [Teardown]    Close Browser
