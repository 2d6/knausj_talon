from talon import Context, Module

mod = Module()
mod.tag("kubectl", desc="tag for enabling kubectl commands in your terminal")
kubectl = "kubectl"

ctx = Context()
ctx.matches = r"""
tag: user.kubectl
"""

mod.list("kubectl_action", desc="actions performed by kubectl")
ctx.lists["self.kubectl_action"] = (
    "get",
#     "delete",
    "describe",
    "label",
    "top"
)

kubectl_objects_singular = {
    "node": "node",
    "job": "job",
    "pod": "pod",
    "namespace": "namespace",
    "service": "service",
    "event": "event",
    "deployment": "deployment",
    "replicaset": "replicaset",
    "daemonset": "daemonset",
    "secret": "secret",
    "configmap": "configmap",
    "horizontal pod auto scaler": "hpa"
}

giant_swarm_api_objects = {
    "cluster": "cluster",
    "app": "app",
    "control plane": "g8scontrolplane",
    "air control plane": "awscontrolplane",
    "machine deploy": "machinedeployment",
    "air machine deploy": "machinedeployment"
}

kubectl_objects_singular.update(giant_swarm_api_objects)

kubectl_objects_plural = { k + 's': v for k, v in kubectl_objects_singular.items()}

mod.list("kubectl_object", desc="objects performed by kubectl")
ctx.lists["self.kubectl_object"] = kubectl_objects_singular | kubectl_objects_plural