*** Settings ***
# For regular execution
Library           KubeLibrary
# For incluster execution
#Library           KubeLibrary    None    True    False
# For development
#Library           ../../src/KubeLibrary/KubeLibrary.py  ~/.kube/k3d

*** Keywords ***
List all secrets
    @{namespaces_list}=  Get Secrets
    Log  \nSecretss ${namespaces_list}:  console=True

List secrets filtered by label
    @{namespaces_list}=  Get Secrets  label_selector=test=test
    Log  \nSecrets with label test=test ${namespaces_list}:  console=True
