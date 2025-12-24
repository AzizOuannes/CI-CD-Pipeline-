# CI/CD Pipeline for AWS EKS - Flask Application

This repository demonstrates a lightweight CI/CD pipeline that builds and deploys a Python Flask application to Amazon EKS using GitHub Actions. It covers both staging and production environments, includes Terraform for infrastructure-as-code, and uses IAM with OIDC for secure authentication.

## What This Project Shows

- Containerizing a Flask app and pushing images to Amazon ECR.
- Automating deployments to EKS via GitHub Actions (staging and production workflows).
- Using Terraform to provision the EKS cluster, node group, and IAM roles.
- Applying OIDC-based authentication so no long-lived AWS credentials are stored.
- Exposing the application with a Kubernetes LoadBalancer service.

## Components

- **Application:** Flask API with Dockerfile and requirements in `app/`.
- **Infrastructure:** Terraform configs in `terraform/` (EKS cluster, node group, IAM roles).
- **CI/CD:** GitHub Actions workflows in `.github/workflows/` for staging and production.
- **IAM:** Trust and policy documents in `IAM/` for GitHub Actions roles.

## High-Level Flow

1) Code changes are committed.
2) GitHub Actions builds a Docker image and pushes it to ECR.
3) The workflow updates kubeconfig, deploys to the target namespace (staging or production), and exposes the service via LoadBalancer.

## Project Structure

```
CICD Pipeline/
├── .github/workflows/   # staging.yml, production.yml
├── terraform/           # main.tf, variables.tf, outputs.tf, provider.tf
├── IAM/                 # IAM role policies and trust relationships
├── app/                 # Flask app, Dockerfile, requirements
└── README.md
```

## Security Notes

- Uses OIDC-based IAM roles for GitHub Actions; no long-lived AWS keys are stored in secrets.
- Terraform state files are ignored via .gitignore to avoid leaking sensitive data.

For deeper implementation details and screenshots, see `report.tex`.

