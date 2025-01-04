# EDGAR Filing Explorer Tool


## deploy to Google Cloud Run

Use Google Cloud Console. I can't figure out what's the command line equivalent.

The steps below may or may not work for you.

```shell

# Go to Cloud Build Console  and manually create a repository there
# linked to a Github repository. Make sure the use the 2nd gen repository.

# create Cloud Build trigger (2nd gen)
gcloud beta builds triggers create github \
    --service-account="<server_account_email>" \
    --name=trigger-edgar-explorer \
    --repository=<repo_connected_in_prev_step> \
    --region=us-central1 \
    --branch-pattern="^develop$" \
    --build-config=cloudbuild.yaml


# check the URL of the service
gcloud run services describe edgar-explorer --region us-central1 --format json | jq -r ".status.url"

# point your browser to the above URL

```
