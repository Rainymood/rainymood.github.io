---
title: "Building a REST API with AWS API Gateway and AWS Lambda in Python (AWS tutorial)"
date: 2023-12-18
tags:
- work
- engineering
- aws 
- tutorial
- architecture
categories: blog
toc: true
toc_sticky: true
header:
    teaser: "/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/thumbnail.png"
---
<!-- ctrl + alt + v -->

In this little tutorial you will learn how to build out this infrastructure on AWS.

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-40-51.png)

Specifically we will: 

- Create an [AWS API gateway service]() that can forward and return our requests and responses
- Create a [Serverless AWS Lambda]() that will process our request and send a response back
- Test our API manually with [Postman]()

Let's get started!

# Step 1: Creating the API Gateway

Let's create an API gateway

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-44-32.png)

Now click on rest API 

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-45-02.png)

And give it a name

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-45-25.png)

Now click on `Create Resource` and create a new resource. I call mine `tmp-resource`

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-46-13.png)

This is what it should look like now

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-47-04.png)

# Step 2: Creating the Lambda

Let's create a new Lambda

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-48-24.png)

Make sure to set the runtime to Python. Give it a nice name. I call mine `tmp-lambda-jan`

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-49-22.png)

Great job! You now have a lambda running!

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-49-53.png)

Paste this code in the body of the lambda [(taken from here)](https://www.moesif.com/blog/technical/api-development/Building-Rest-API-With-AWS-Gateway-And-Python/)

```python
import json
# Example data

data = {
    "items": [
        {"id": 1, "name": "Item 1", "price": 10.99},
        {"id": 2, "name": "Item 2", "price": 15.99},
        {"id": 3, "name": "Item 3", "price": 20.99},
    ]
}

def lambda_handler(event, context):
    # Determine the HTTP method of the request
    http_method = event["httpMethod"]
    # Handle GET request
    if http_method == "GET":
        # Return the data in the response
        response = {
            "statusCode": 200,
            "body": json.dumps(data)
        }
        return response

    # Handle POST request
    elif http_method == "POST":
        # Retrieve the request's body and parse it as JSON
        body = json.loads(event["body"])
        # Add the received data to the example data
        data["items"].append(body)
        # Return the updated data in the response
        response = {
            "statusCode": 200,
            "body": json.dumps(data)
        }
        return response

    # Handle PUT request
    elif http_method == "PUT":
        # Retrieve the request's body and parse it as JSON
        body = json.loads(event["body"])
        # Update the example data with the received data
        for item in data["items"]:
            if item["id"] == body["id"]:
                item.update(body)
                break
        # Return the updated data in the response
        response = {
            "statusCode": 200,
            "body": json.dumps(data)
        }
        return response

         # Handle DELETE request
    elif http_method == "DELETE":
        # Retrieve the request's body and parse it as JSON
        body = json.loads(event["body"])
        # Find the item with the specified id in the example data
        for i, item in enumerate(data["items"]):
            if item["id"] == body["id"]:
                # Remove the item from the example data
                del data["items"][i]
                break
        # Return the updated data in the response
        response = {
            "statusCode": 200,
            "body": json.dumps(data)
        }
        return response

    else:
        # Return an error message for unsupported methods
        response = {
            "statusCode": 405,
            "body": json.dumps({"error": "Method not allowed"})
        }
        return response
```

And make sure to click on **Deploy**

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-51-18.png)

Now you have updated the code in the lambda and re-deployed it! Good job!

Now all that is left is that we must hook the lambda into our API because as it stands right now the API is a bit empty.

# Step 3: Adding the lambda and testing

Going back to our API we can now create a method

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-52-13.png)

Use `Method Type` ANY and set the lambda to the name that you just created.

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-52-43.png)

This is what you should see right now. 

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-54-39.png)

There's one important setting that you must change and that is the **Lambda proxy integration must be set to true**

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-55-07.png)

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-55-26.png)


What this setting does is that it allows your API gateway to actually forward the requests it gets. If you don't set this to true then the Lambda won't get the event that we need. Now you can deploy the API!

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-55-46.png)

Create a new stage. Dev is fine.

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-56-06.png)

# Step 4: Testing

Now copy the `Invoke URL` 

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-56-41.png)

And use it to test it on postman.

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-58-11.png)

If you for example, try to hit this URL

```https://ho2f55mvv2.execute-api.eu-west-1.amazonaws.com/dev/my-resource```

And you get 

```json
{
    "message": "Missing Authentication Token"
}
```

Make sure to use the right resource, which in my case is `tmp-resource` and not `my-resource`

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-57-42.png)

Try again... and boom!

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-58-37.png)

# Step 5: Cleanup


Remove the API 

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-59-02.png)

Remove the Lambda

![](/../assets/2023-12-18-building-a-rest-api-with-aws-api-gateway-and-aws-lambda-in-python-aws-tutorial/2023-12-18-15-59-32.png)

# Wrapping up

In this tiny tutorial we implemented a small system on the cloud that combines the **AWS API Gateway** and a **Serverless AWS Lambda**. I hope you had as much fun as I did making this tutorial. While the system itself is simple and straightforward, I urge and encourage you to try and experiment with different setups, because this is the first stepping stone to building systems on the cloud that scale.

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
    