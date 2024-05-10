---
title: "Deploying your first AWS CloudFormation stack"
date: 2024-05-10
tags:
# Blog or how-to
- tutorial
# Work or personal?
- work
# Big themes that I write about
- engineering
- aws
categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2024-05-10-deploying-your-first-aws-cloudformation-stack/thumbnail.png"
---
<!-- ctrl + alt + v -->

<!-- Checklist:
Title = insight
Interesting 1st sentence
Short and concise -->

As a machine learning engineer, deploying automated infrastructure-as-code is basically 80% of the job.

We are responsible for building scalable, maintainable, and reliable systems and for that we need to have our infrastructure defined in code.

This makes our system easy to deploy and more importantly easy to *re-deploy* if something goes wrong.

In this blog post I want to run you through a simple deployment of a single s3 bucket. 

Although deploying a single s3 bucket is fairly trivial, getting comfortable with cloudformation is super important if you want to grow in your career. 

It's a bit like wax-on-wax off in the karate kid, you just have to do it a bunch of times to get good at it.

Please note that following along for this tutorial requires you to have a valid AWS profile with the right credentials, which I won't get into

# Setup

Install the [aws-cli](https://aws.amazon.com/cli/)

```
pip install aws-cli
```

Verify correct installation

```
$ aws --version
aws-cli/2.2.26
```

# Adding a main stack

Now we are going to add our main stack and in that stack we will add a substack.

Make a new file at the following location `infra/main.yml`

```yml
# infra/main.yml
AWSTemplateFormatVersion: '2010-09-09'
Description: A basic cloudformation template

Parameters:
  Environment:
    Type: String

Resources:
  ModelData:
    Type: AWS::CloudFormation::Stack
    Properties:
      Parameters:
        ServiceName: !Ref AWS::StackName
        Environment: !Ref Environment
      TemplateURL: model-data.substack.yml
```

This is our main stack and this is the one we will deploy. We see the `Parameters` which are parameters that we can pass and we see `Resources` which are the AWS resources we want to deploy.

In this case the resource that we want to deploy is another `AWS::CloudFormation::Stack`, a substack.

Note that the `TemplateURL` points to `model-data.substack.yml`, this is the file we are going to make now.

Make a new file `model-data.substack.yml`

```yml
# infra/model-data.substack.yml
AWSTemplateFormatVersion: '2010-09-09'

Parameters:
  ServiceName:
    Type: String
  Environment:
    Type: String

Resources:
  Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub "${ServiceName}.${AWS::AccountId}.${AWS::Region}.${Environment}.org"
      OwnershipControls:
        Rules:
          - ObjectOwnership: ObjectWriter
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
```

Again, we have some `Parameters` and `Resources` and for now you can Ignore the settings on the s3 bucket.

Now we are ready to deploy.

If we did not have any substacks we could deploy directly.

```
$ aws cloudformation deploy ...
``` 

But because we have substacks in our main stack, we first need to package this deployment. 

The reason for this is that when we try to deploy the main stack, it starts looking for `model-data.substack.yml`, but this doesn't exist on AWS.

We first need to turn all local references into references that are also understandable in the cloud, this is what the packaging step does. 

Let's do that.

```bash
aws cloudformation package 
  --template-file infra/main.yml 
  --s3-bucket tmp-bucket
  --s3-prefix tmp-prefix
  --output-template-file packaged-template.json 
  --use-json 
  --force-upload 
  --profile=profile
  --region=eu-west-1
```

```
Uploading to tmp/115d6216e2ba888dfb9ea95c58b7e420.template  685 / 685.0  (100.00%)
Successfully packaged artifacts and wrote output template to file packaged-template.json.
Execute the following command to deploy the packaged template
aws cloudformation deploy --template-file C:\Users\JanMeppe\Documents\example-cf-deploy\packaged-template.json --stack-name <YOUR STACK NAME>
```

Taking a look in the template we see this

```json
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Example cf deploy",
    "Parameters": {
        "Environment": {
            "Type": "String"
        }
    },
    "Resources": {
        "ModelData": {
            "Type": "AWS::CloudFormation::Stack",
            "Properties": {
                "Parameters": {
                    "ServiceName": {
                        "Ref": "AWS::StackName"
                    },
                    "Environment": {
                        "Ref": "Environment"
                    }
                },
                "TemplateURL": "https://s3.eu-west-1.amazonaws.com/tmp-bucket/tmp-prefix/115d6216e2ba888dfb9ea95c58b7e420.template"
            }
        }
    }
}
```

See how this `TemplateURL` no longer references to a file in our local storage, but to some file on s3? 

Now we can deploy this in the cloud and `TemplateURL` will be read from that s3 location.

```bash
aws cloudformation deploy 
  --template-file packaged-template.json 
  --stack-name tmp-jan-foo
  --parameter-overrides Environment=master 
  --region=eu-west-1 
  --profile=profile
```

Resulting in 

```
Waiting for changeset to be created..
Waiting for stack create/update to complete
Successfully created/updated stack - tmp-jan-foo
```

Inspect the stack

```bash
aws cloudformation describe-stack-events 
  --stack-name tmp-jan-foo 
  --region=eu-west-1 
  --profile=profile
```

Results in 

```
{
    "StackEvents": [
        {
            "StackId": "arn:aws:cloudformation:eu-west-1:12345:stack/tmp-jan-foo/...",
            "EventId": "...",
            "StackName": "tmp-jan-foo",
            "LogicalResourceId": "tmp-jan-foo",
            "PhysicalResourceId": "arn:aws:cloudformation:eu-west-1:12345:stack/tmp-jan-foo/...",
            "ResourceType": "AWS::CloudFormation::Stack",
            "Timestamp": "2024-05-10T11:45:49.820000+00:00",
            "ResourceStatus": "CREATE_COMPLETE"
        },
        ...
```

That's it! Everything works.

But we can also see it in the cloud console!

![](/../assets/2024-05-10-deploying-your-first-aws-cloudformation-stack/2024-05-10-18-04-13.png)

So cool! Your first cloudformation stack! 

And that's it! That's your first deployment! You are officially now a machine learning *engineer*.

Now, don't forget to delete your stack when you are done with it!

Usually, in production systems we have certain protections in place that forbid us to manually remove these stacks, so that we can never accidentally delete production.

```bash
aws cloudformation delete-stack 
  --stack-name tmp-jan-foo 
  --region=eu-west-1 
  --profile=profile
```

The fact that we need to upload our other templates to s3 first also means that we need a **deployment bucket** where we store our deployment artifacts. 

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
    