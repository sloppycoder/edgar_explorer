# EDGAR Filing Explorer Tool


## deploy to Google Cloud Run

Use Google Cloud Console. I can't figure out what's the command line equivalent.

The steps below may or may not work for you.

```shell

# connect github repo with Cloud Build
# browse to https://console.cloud.google.com/cloud-build/triggers;region=global/connect?project=YOUR_PROJECT_ID

# create Cloud Build trigger
gcloud builds triggers create github \
    --name="trigger-edgar-explorer" \
    --repo-name="edgar-explorer" \
    --repo-owner="<your_github_id>" \
    --branch-pattern="^develop$" \
    --build-config="cloudbuild.yaml"


```
