# Toxic Comment Challenge

---------------------------------------------------------------------------

HOW TO ADD LAYERS TO LAMBDA VIA GITHUB ACTIONS

LAYER DEFINITION
- include into requirements txt as library and version
- for instance name as: layer_sacremoses.txt
- within txt: scikit-learn==1.2.0

DEPLOYMENT
- within root/.github/workflows
- there is a .yaml file called 'build-lambda-layer.yaml'
- searches for 'layer_' then installs and zips dependencies.

AUTHENTICATION
- 'Configure aws credentials: Sets up AWS credentials by assuming a specific IAM
- Setup 'secret key' in settings -> secrets and variables -> actions.
- Attain access keys from: IAM -> Security credentials
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

---------------------------------------------------------------------------

Activate virtual environment locally

```bash
source .venv/bin/activate
```
