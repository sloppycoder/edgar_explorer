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

# check the URL of the service
gcloud run services describe edgar-explorer --region us-central1 --format json | jq -r ".status.url"

# point your browser to the above URL

```
