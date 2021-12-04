import os
import time
import yaml
from kubernetes import client, config, utils
from kubernetes.client.api import core_v1_api
from kubernetes.client.exceptions import ApiException


def new_prep_pod():
    if os.getenv('KUBERNETES_SERVICE_HOST'): config.load_incluster_config()
    
    pod_name = "renter-test"
    namespace = "orchestrator"
    
    with open(os.path.join(os.path.dirname(__file__), "render-pod.yaml")) as f:
        dep = yaml.safe_load(f)

        print(f'POD MANIFEST:\n{dep}')

        api_response = core_v1_api.CoreV1Api().create_namespaced_pod(body=dep,namespace=namespace)
 
        print(f'From {os.path.basename(__file__)}: Pod {pod_name} in {namespace} created.')
        return api_response