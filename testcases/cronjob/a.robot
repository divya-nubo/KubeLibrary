*** Settings ***
Resource          ./b.robot

*** Test Cases ***
Job test case example
    [Tags]    other
    List all cron jobs in namespace  kubelib-tests
    List labels of cron job  ${cron_job_name}  kubelib-tests

Jobs by label
    [Tags]    prerelease
    List cron jobs with label  .*  kubelib-tests  TestLabel=mytestlabel
