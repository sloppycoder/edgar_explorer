# EDGAR Filing Explorer Tool


## deploy to Google Cloud Run

```shell

# create Cloud Build trigger
gcloud builds triggers create github \
    --name="trigger-edgar-explorer" \
    --repo-name="edgar-explorer" \
    --repo-owner="sloppycoder" \
    --branch-pattern="^develop$" \
    --build-config="cloudbuild.yaml"

```
