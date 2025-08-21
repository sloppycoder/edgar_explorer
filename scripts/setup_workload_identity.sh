#!/bin/bash

GCP_PROJECT=edgar-ai-dev
GITHUB_REPO_OWNER=sloppycoder
GITHUB_REPO=edgar_explorer
SERVICE_ACCOUNT=cloud-run-deploy@edgar-ai-dev.iam.gserviceaccount.com

# Get project ID from project name
GCP_PROJECT_ID=$(gcloud projects describe $GCP_PROJECT --format="value(projectNumber)")

# 3. Allow GitHub Repository to Impersonate Service Account
gcloud iam service-accounts add-iam-policy-binding \
    "$SERVICE_ACCOUNT" \
    --project="$GCP_PROJECT" \
    --role="roles/iam.workloadIdentityUser" \
    --member="principalSet://iam.googleapis.com/projects/$GCP_PROJECT_ID/locations/global/workloadIdentityPools/github-pool/attribute.repository/$GITHUB_REPO_OWNER/$GITHUB_REPO"

