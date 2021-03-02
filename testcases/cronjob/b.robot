*** Settings ***
Library           Collections
Library           RequestsLibrary
# For regular execution
Library           KubeLibrary
# For incluster execution
#Library           KubeLibrary    None    True    False
# For development
#Library           ../../src/KubeLibrary/KubeLibrary.py  ~/.kube/k3d

*** Keywords ***
List all cron jobs in namespace
    [Arguments]  ${namespace}
    @{namespace_cron_jobs}=  Get Cron Jobs In Namespace    ${namespace}
	Log  \nCron Jobs @{namespace_cron_jobs}:  console=True
    Log  \nCron Jobs in namespace ${namespace}:  console=True
    FOR  ${cron_job}  IN  @{namespace_cron_jobs}
	    ${cronjob_details}=  Get Cron Job Details In Namespace  ${cron_job}  ${namespace}
        Log  ${cronjob_details.metadata.name}  console=True
        Set Global Variable    ${cron_job_name}    ${cronjob_details.metadata.name}
    END

List labels of cron job
    [Arguments]  ${cron_job_name}  ${namespace}
    @{namespace_cron_jobs}=  Get Cron Jobs In Namespace    ${namespace}
    Log  \nList labels in cron job ${cron_job_name}:  console=True
	Log  \n:::::::::::::::::::::::::::::::::::::: @{namespace_cron_jobs}:  console=True
    FOR  ${cron_job}  IN  @{namespace_cron_jobs} 
	    ${cron_job_details}=  Get Cron Job Details In Namespace  ${cron_job}  ${namespace}
		Log  \n:::::::::::::::::::::::::::::::::::::: ${cron_job_details}:  console=True
        Log  Labels in ${cron_job_details.metadata.labels}  console=True
        Dictionary Should Contain Item    ${cron_job_details.metadata.labels}    TestLabel    mytestlabel
        ...  msg=Expected labels do not match.
    END

List cron jobs with label
    [Arguments]  ${cron_job_name}  ${namespace}  ${label}
    @{namespace_cron_jobs}=  Get Cron Jobs In Namespace    ${namespace}  ${label}
    Log  \nList labels in cron job ${cron_job_name}:  console=True
    FOR  ${cron_job}  IN  @{namespace_cron_jobs}
	    ${cron_job_details}=  Get Cron Job Details In Namespace  ${cron_job}  ${namespace}
		
        Log  Labels in ${cron_job_details.metadata.labels}  console=True
        Dictionary Should Contain Item    ${cron_job_details.metadata.labels}    TestLabel    mytestlabel
        ...  msg=Expected labels do not match.
    END

