*** Settings ***
Resource          ./cronjob_kw.robot

*** Test Cases ***
cronjobs test case example
    [Tags]    grafana
    List all cronjobs in namespace  default
