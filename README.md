# Git Push & Pull triggered AWS workflows

### Using GitHub Actions to create triggered workflows to automate manual processes.

## The Problem

### Legacy software is stuck in the past working for months to create the best version of an app only to eventually deploy it and realise many improvements are required.
This process can be improved by using DevOps & CICD, Uuilising small continuous iterations & automation.
The results is you get a faster time to market with a more complete product for the end user through a combination of improved reliability, increased scalability & collaboration within the team. 
This is looped back to the start of the development process for continuous improvement, continuous delivery, continuous deployment.

## What I Built

### This process has 2 workflows:

1. GitHub Actions to trigger on a push that creates a Lambda package to deploy on AWS & updates.

<img width="1624" height="969" alt="image" src="https://github.com/user-attachments/assets/c35fd79c-1dfa-4aa0-be76-0e02ecc1dd92" />

### Workflow 1 - Git Push triggered workflow to update Lambda function with latest code
- Push code to GitHub, which triggers the workflow
- GitHub secrets stores credentials for AWS access keys to deploy Lambda package
- GitHub Actions uses runner to checkout the code from repo, sets up Python environment
- Configures credentials & packages up Lambda to deploy to AWS

2. GitHub Actions to trigger a pull event that uses a CloudFormation yaml file to deploy an S3 bucket in AWS.

<img width="1580" height="995" alt="CICD Pull Architecture enhanced" src="https://github.com/user-attachments/assets/448dc38a-7f25-46be-8324-1ddbfc57ac6b" />

### Workflow 2 - Git Pull triggered workflow - Every time a pull request is opened in GitHub, the workflow will validate & test the CloudFormation template then create an S3 bucket, achieved by:
- Pushing code to GitHub & triggering the pull request
- Triggers GitHub Actions workflow
- Select runner, set up & configure AWS credentials
- Validates CloudFormation template
- Once validated a test bucket will be deployed in AWS
- GitHub Actions bot comments on pull request & CloudFormation stack created
- User verifies in AWS the creation of CloudFormation stack & S3 bucket
- Merge stack into main via GitHub
- Stack is automatically deleted after pull request is merged

## Decisions I made

### Automation Automation Automation
Rather than manually having to repeatedly upload code I wanted to automate this using GitHub Actions.
This involved creating a workflow to reduce the amount of manual intervention required.
Automating the clean up of resources in AWS also meant no ongoing running costs once the pull request was merged.

### Testing resources
To test each workflow was running correctly I used a CloudFormation template:
Workflow 1 - that when triggered created Lambda function, updating the code within the file, the updated code being viewable within AWS.
Workflow 2 - that when successfully validated would deploy the stack and create an S3 bucket in AWS.

## What broke and how I fixed it

### Clean up didn’t work
Resolution - the trigger was only for a pull request, this required a merge & close.
Specifying the types of requests to listen for and adding to the if statement on a merge that the event must also be closed as a condition then caused the clean up to trigger.

### Syntax issues
The upper and lower casing of letters, hyphens where they're not needed, the odd spelling error are all part of the debugging process.
This always puts attention to detail at the front of my mind when moving forwards.

## Result

### Workflow 1 - Push trigger
Once successfully ran the push on change to file caused a Lambda function to deploy with the updated message inside that had been saved locally within the code.

### Workflow 2 - Pull trigger
Once all syntax issues were resolved and the added code for the operation clean up was put in, I had the triggered workflow. 
The pull request caused GitHub Secrets to use my AWS credentials to provide access to the AWS CLI to validate the CloudFormation template and deploy the stack and the test bucket. 
GitHub Actions comments on the pull request with the result. I then verified the CloudFormation stack and S3 bucket had been created in AWS console. 
Once verified I merged the pull request in GitHub which triggered the clean up workflow to delete the test S3 bucket and CloudFormation stack.
