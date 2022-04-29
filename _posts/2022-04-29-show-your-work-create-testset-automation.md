---
title: "Show your work: Automating cloud infrastructure using infrastructure-as-code"
date: 2022-04-29
tags:
  - python
  - aws
  - infrastructure
  - show-your-work
categories: blog
toc: false
toc_sticky: false
header:
  teaser: "/../assets/2022-04-29-show-your-work-create-testset-automation/thumbnail2.png"
---

I want to share a little piece of work that I recently completed. Hope you enjoy!

![](/../assets/2022-04-29-show-your-work-create-testset-automation/img.png)

**What I did**

* Using infrastructure-as-code and AWS I built a system that automatically creates testsets for our algorithms every month
* Now, every month a cron job (*EventsRule*) triggers a piece of code (*Lambda*) that runs a computational routine (*Sagemaker job*) that creates the new testset in a new table in our Athena warehouse (*Athena table/S3 bucket*)

**Why I am proud of it** 

* This was my first time setting up automated infrastructure-as-code and it was a real pain in the ass, but once I got it, it was very satisfying
* I found it particularly interesting to build a new system by piecing together different services of AWS 
* It adds repeated business value by automating something we previously did manually

**Technical details**

Most of the work involved updating our infra-as-code `cloudformation.yaml`. I had to provision the following new infrastructure:

* `CreateTestsetLambda` ([`AWS::Serverless::Function`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html)): This is the actual code in the form of a lambda that triggers the Sagemaker job using `boto3`. We do it this way because currently (as of writing this) there is no way to start a Sagemaker job directly from a lambda
* `AWSLambdaCreateTestsetLambdaRole` ([`AWS::IAM::Role`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html)): This is the role  that the lambda needs to get executed
* `AWSSageMakerExecutorRole` ([`AWS::IAM::Role`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html)): This is another role  that we give to the lambda so that it has rights to start the Sagemaker job
* `ScheduleMonthlyEventsRule` ([`AWS::Events::Rule`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html)): This is the cron job  that runs triggers the lambda every month 
* `PermissionForEventsRuleToInvokeLambda` ([`AWS::Lambda::Permission`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html)): Finally, we need to give the cron job this permission to be allowed to trigger the lambda 

That's it! I have to admit, it was a real pain in the ass sometimes, but once everything started working together it was *sooooo satisfying.*

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
  <label for="mce-EMAIL">Liked this article and want to hear more? Join 40+ others and subscribe!</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->
