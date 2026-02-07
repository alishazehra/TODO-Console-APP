# 🤖 Agent Spec-Driven Helm Deployment

## Spec Overview

Agent is tasked to:
- Deploy Todo App to Minikube
- Use Helm chart `todo-app`
- Support dev and prod environments
- Configure service, ingress, and replicas
- Apply config maps and secrets automatically

---

## Step 1: Fetch Latest Helm Chart

Agent action:

```bash
git clone https://github.com/example/todo-app-helm.git
cd todo-app-helm
