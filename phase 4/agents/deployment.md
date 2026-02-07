# 🚀 Deploying a Todo App on Kubernetes using Minikube

## 📌 Introduction

Kubernetes is a container orchestration platform used to automate deployment, scaling, and management of containerized applications.  
Minikube allows you to run a local Kubernetes cluster for development and testing purposes.

In this guide, we will deploy a simple **Todo Application** on Kubernetes using Minikube. The Todo app will be containerized using Docker and then deployed to a local Kubernetes cluster.

---

## 🎯 Objectives

By the end of this guide, you will be able to:
- Build a Docker image for a Todo application
- Start and configure Minikube
- Create Kubernetes Deployment and Service
- Access the Todo application from a browser
- Manage pods and services
- Scale the application
- Clean up resources

---

## 🛠️ Prerequisites

- Docker installed
- Minikube installed
- kubectl installed
- Basic knowledge of Docker and Kubernetes
- A simple Todo application (Node.js or Python example)

Check installations:

```bash
docker --version
minikube version
kubectl version --client
