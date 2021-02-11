Library           Collections
Library           RequestsLibrary
# For regular execution
Library           KubeLibrary
# For incluster execution
#Library           KubeLibrary    None    True    False
# For development
#Library           ../../src/KubeLibrary/KubeLibrary.py  ~/.kube/k3d

*** Keywords ***
List all cronjobs in namespace
    [Arguments]  ${namespace}  ${label}=${EMPTY}
    @{cronjobs_list}=  Get cronjobs In Namespace    .*  ${namespace}  ${label}
    Log  \nCronjobs in namespace ${namespace}:  console=True
    FOR  ${cronjob}  IN  @{cronjobs_list}
        Log  ${cronjob.metadata.name}  console=True
    END


