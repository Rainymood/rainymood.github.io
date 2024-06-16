---
title: "How to do cross account Sagemaker endpoint requests in AWS"
date: 2024-06-15
tags:
# Blog or how-to
- tutorial

# Work or personal?
- work

# Big themes that I write about
- engineering
- aws
- infra 
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-06-15-how-to-do-cross-account-sagemaker-endpoint-requests-in-aws/thumbnail.png"
---
<!-- ctrl + alt + v -->

In this blog post I want to show you how to do **cross-account Sagemaker endpoint requests in AWS**.

We have two accounts, a **parent** account and a **child** account. The parent account hosts the Sagemaker endpoint and we want to call it from the child account.

Based on [this blog post](https://towardsdatascience.com/sharing-your-sagemaker-model-eaa6c5d9ecb5)

## High level solution

- In parent account
    - Create a policy `SageMakerExternalInvokeEndpoint` that allows you to execute the Sagemaker endpoint
    - Create a role `SagemakerExternal` and add **child account** as trusted account
- In child account
    - Create a lambda on the child account to invoke the API with
    - Change the **execution role** of the lambda to allow `sts:AssumeRole`  on `SagemakerExternal` (which is possible because we added it as a trusted account)

## In the parent account

In the parent account we are going to do 2 things: 

1. Create a policy `SageMakerExternalInvokeEndpoint` that will give us permission to call the endpoints on this account
2. Create a role `SagemakerExternal` having this policy that can be assumed by someone else (the child account)

Log in to the parent account.

Here we configured the endpoint(s) we want to hit cross-account. 

Copy the ARN of the endpoint we want to hit.

![](/../assets/2024-06-15-how-to-do-cross-account-sagemaker-endpoint-requests-in-aws/2024-06-16-08-33-27.png)

Make a new policy that allows someone to invoke Sagemaker endpoints in this account.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": ["sagemaker:InvokeEndpoint"],
            "Effect": "Allow",
            "Resource": "arn:aws:sagemaker:eu-west-1:<parent account id>:endpoint/*"
        }
    ]
}
```

Log in to IAM.

Go to policies.

Click on create policy.

![](/../assets/2024-06-15-how-to-do-cross-account-sagemaker-endpoint-requests-in-aws/2024-06-16-08-34-47.png)

Paste the json above.

![](/../assets/2024-06-15-how-to-do-cross-account-sagemaker-endpoint-requests-in-aws/2024-06-16-08-34-34.png)

If you want to, make the policy more generic with wildcards `*`.

![](/../assets/2024-06-15-how-to-do-cross-account-sagemaker-endpoint-requests-in-aws/2024-06-16-08-35-18.png)

Name it `SageMakerExternalInvokeEndpoint.`

![](/../assets/2024-06-15-how-to-do-cross-account-sagemaker-endpoint-requests-in-aws/2024-06-16-08-36-54.png)

Now we want to make a new role `SageMakerExternal`

![](/../assets/2024-06-15-how-to-do-cross-account-sagemaker-endpoint-requests-in-aws/2024-06-16-08-37-08.png)

Click on **Trusted Account** and paste **child id account** here

![](/../assets/2024-06-15-how-to-do-cross-account-sagemaker-endpoint-requests-in-aws/2024-06-16-08-37-55.png)

Add the new policy you just made.

![](/../assets/2024-06-15-how-to-do-cross-account-sagemaker-endpoint-requests-in-aws/2024-06-16-08-38-27.png)

Give it a name. 

![](/../assets/2024-06-15-how-to-do-cross-account-sagemaker-endpoint-requests-in-aws/2024-06-16-08-39-50.png)

Now the child account is a trusted entity in the parent account.

![](/../assets/2024-06-15-how-to-do-cross-account-sagemaker-endpoint-requests-in-aws/2024-06-16-08-44-44.png)

What did we just do? 

We created a new role `SagemakerExternal` that allows us to invoke the specific sagemaker endpoints on this account with the **child account** as a trusted account.

Now all that is left to do is to assume this role from the child account.

## In the child account: Grant assume role to child account

Now what we need to do is get the child account to allow to assume this role.

Then we need to make a lambda to test it and change the execution role of that lambda to allow `sts:AssumeRole`.

Log in to child account.

Create new policy `AllowAssumeSagemakerExternalRole`

This policy will allow the child account to assume this new role.

![](/../assets/2024-06-15-how-to-do-cross-account-sagemaker-endpoint-requests-in-aws/2024-06-16-08-47-40.png)

Give it a nice name 

![](/../assets/2024-06-15-how-to-do-cross-account-sagemaker-endpoint-requests-in-aws/2024-06-16-08-48-19.png)

Now create a new lambda.

This is what we want to paste in.

```python
import json
import boto3
import os

from data import body2

def lambda_handler(event, context):
    # Assume the cross-account role (allowed because of sts:AssumeRole)
    sts_client = boto3.client('sts')
    assumed_role = sts_client.assume_role(
        RoleArn='arn:aws:iam::<parent account id>:role/SageMakerExternal',  # add parent id here
        RoleSessionName='SageMakerInvokeSession',
        ExternalId='<parent account id>', # add parent id here
    )
    
    # Create a new session using the assumed role credentials
    credentials = assumed_role['Credentials']
    sagemaker_client = boto3.client(
        'sagemaker-runtime',
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken'],
    )

    # Add the endpoint you want to call cross-account here
    endpoint_name = "f73559-..." 

    # Invoke the SageMaker endpoint
    response = sagemaker_client.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='application/json',
        Body=json.dumps({}),
    )

    # Parse the response
    result = json.loads(response['Body'].read().decode())

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
```

If you try to run this now you get the following error

> "errorMessage": "An error occurred (AccessDenied) when calling the AssumeRole operation: User: arn:aws:sts::<child account id>:assumed-role/ is not authorized to perform: sts:AssumeRole on resource: arn:aws:iam::<parent account id>:role/SageMakerExternal",

What we need to do is **change the lambda execution role.**

Remember we made **this policy:** `AllowAssumeSagemakerExternalRole`

We need to add this policy to the lambda execution role.

Go to the lambda and click on edit.

![](/../assets/2024-06-15-how-to-do-cross-account-sagemaker-endpoint-requests-in-aws/2024-06-16-08-51-45.png)

Go to the bottom and click on edit

![](/../assets/2024-06-15-how-to-do-cross-account-sagemaker-endpoint-requests-in-aws/2024-06-16-08-52-13.png)

Add this piece

```python
{
    "Effect": "Allow",
    "Action": "sts:AssumeRole",
    "Resource": "arn:aws:iam::<parent account id>:role/SageMakerExternal"
},
```

That's it now you can run cross account sagemaker endpoint requests on AWS!

# Conclusion

In this blog posted I showed you how to do cross account Sagemaker requests.

Summary:

1. In the parent account with create a policy for invocations and a role with the child account as a trusted account
2. In the child account allow that account to assume the role from step 1.

# Subscribe

<!-- Begin Mailchimp Signup Form -->
<link href="//cdn-images.mailchimp.com/embedcode/horizontal-slim-10_7.css" rel="stylesheet" type="text/css">
<style type="text/css">
#mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif; width:100%;}
/* Add your own Mailchimp form style overrides in your site stylesheet or in this style block.
    We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */
</style>
<div id="mc_embed_signup">
<form action="https://gmail.us3.list-manage.com/subscribe/post?u=92fe86c389878585bc87837e8&amp;id=50543deff9" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
    <div id="mc_embed_signup_scroll">
<label for="mce-EMAIL">I blog about how to grow as a machine learning engineer! Liked this article and want to hear more? Join 40+ others and subscribe!</label>
<input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->
    