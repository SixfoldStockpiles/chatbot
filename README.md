# DialogFlow agent

* Assumes GCP is set up with a DialogFlow agent associated with a project. Billing enabled.

# Credentials

* Create a service account in GCP. Give it client API access to DialogFlow. Generate a key and save it as a JSON file.
* The location of the key should be stored in the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.