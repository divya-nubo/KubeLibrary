Library           KubeLibrary
# For incluster execution
#Library           KubeLibrary    None    True    False
# For development
#Library           ../../src/KubeLibrary/KubeLibrary.py  ~/.kube/k3d

*** Keywords ***
List all replicasets in namespace
    [Arguments]  ${namespace}  ${label}=${EMPTY}
    @{replicasets_list}=  Get Replicasets In Namespace    .*  ${namespace}  ${label}
    Log  \nReplicasets in namespace ${namespace}:  console=True
    FOR  ${replica}  IN  @{replicasets_list}
        Log  ${replica.metadata.name}  console=True
    END

