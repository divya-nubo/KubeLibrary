*** Settings ***
Resource          ./replicaset_kw.robot

*** Test Cases ***
Replicasets test case example
    [Tags]    grafana
    List all replicasets in namespace  default
