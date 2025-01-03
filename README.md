# EDGAR Filing Explorer Tool


## deploy to Google Cloud Run

```shell

# create Cloud Build trigger
gcloud builds triggers create github \
    --name="trigger-edgar-explorer" \
    --repo-name="edgar-explorer" \
    --repo-owner="<your_github_id>" \
    --branch-pattern="^develop$" \
    --build-config="cloudbuild.yaml"

```
The gcloud command will provide a URL in the output, asking you to install the Google Cloud Build GitHub App to your GitHub organization or user account.

```text

You need to install the Cloud Build GitHub App on your GitHub account.
Please visit this URL: https://github.com/apps/google-cloud-build/installations/new
```

Follow the instruction and open the URL:
* Open the URL provided in the output (e.g., https://github.com/apps/google-cloud-build/installations/new).
* Select the GitHub organization or account
* Choose the repository (your-github-repo-name) you want to link
* Complete the installation
