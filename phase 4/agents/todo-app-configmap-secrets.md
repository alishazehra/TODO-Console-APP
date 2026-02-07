# 🔐 Using ConfigMaps and Secrets for Todo App on Kubernetes (Minikube)

## 📌 Introduction

ConfigMaps and Secrets are Kubernetes resources used to manage configuration data and sensitive information such as passwords, API keys, and environment variables.

This guide explains how to use ConfigMaps and Secrets in a Todo application deployed on Minikube.

---

## 🎯 Objectives

- Understand ConfigMaps and Secrets
- Create ConfigMaps for application configuration
- Create Secrets for sensitive data
- Inject them into Pods
- Verify configuration inside containers

---

## 📦 What is a ConfigMap?

A ConfigMap stores non-sensitive configuration data in key-value pairs such as:
- App environment
- App name
- Database host
- Feature flags

---

## 🧩 Step 1: Create ConfigMap

Create file `configmap.yaml`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: todo-config
data:
  APP_NAME: "Todo Kubernetes App"
  APP_ENV: "development"
