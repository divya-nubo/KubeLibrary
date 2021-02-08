*** Settings ***
Resource          ./secrets_kw.robot

*** Test Cases ***
Secrets test case example
    [Tags]    other
    List all secrets
    List secrets filtered by label		
	
