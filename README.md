# Getting started with Hashicorp CDK for Terraform and IBM Cloud

A simple example showing integration of the [IBM Cloud provider for Terraform](https://github.com/IBM-Cloud/terraform-provider-ibm) with [Hashicorp CDK for Terraform](https://www.terraform.io/cdktf).

## Prerequisites

For CDK for Terraform, you will need:
* Node.js and npm v16+.
* Terraform CLI (1.1+).

For the project, you will need:
* Python v3.7
* pipenv v2021.5.29 with `pip install --user pipenv`

## Install CDK for Terraform

1. Install CDK for Terraform
   ```
   npm install --global cdktf-cli@latest
   ```
1. Verify installation
   ```
   cdktf help
   ```

## Deploy resources

* This project creates [one resource group](./main.py) as a proof of concept.
* It was initialized with the command `cdktf init --template=python --local`.
* It is [pre-configured](./cdktf.json) to use the IBM Cloud provider for Terraform 1.44 and later. The provider was added with the command `cdktf provider add "IBM-Cloud/ibm@~> 1.44"`.

1. Retrieve the IBM Cloud provider and generate **python** constructs in the output directory `imports`:

   ```sh
   cdftk get
   ```

1. Set the environment variable `IBMCLOUD_API_KEY`

   ```sh
   export IBMCLOUD_API_KEY=...
   ```

1. Optionally set a prefix to name the resources that will be created. The example has a default value `cdktf-gs`.

   ```sh
   export TF_VAR_basename=uniqueprefix
   ```

1. Deploy the stack

   ```sh
   cdktf deploy
   ```

## Destroy the resources

1. Destroy the stack

   ```sh
   cdktf destroy
   ```

## License

See [LICENSE](LICENSE) for license information.