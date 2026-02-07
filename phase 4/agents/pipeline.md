# 🔄 CI/CD Pipeline Implementation for Todo App on Kubernetes (Minikube)

## 📌 Introduction

A CI/CD (Continuous Integration and Continuous Deployment) pipeline automates the process of:
- Building application code
- Testing the application
- Creating Docker images
- Pushing images to a container registry
- Deploying the application to Kubernetes

In this document, we implement a complete CI/CD pipeline for a Todo application deployed on Kubernetes using Minikube.

---

## 🎯 Objectives

By the end of this guide, you will:
- Understand CI/CD pipeline architecture
- Create a Docker image automatically
- Push image to Docker Hub
- Deploy application to Kubernetes
- Perform rolling updates
- Verify deployment
- Handle failures and rollbacks

---

## 🏗️ Pipeline Architecture

