---
title: "Our Amazon Sagemaker Processing job setup"
date: 2021-12-06
categories:
  - blog
toc: false
toc_sticky: false
tags:
  - update
header:
  teaser: "/../assets/2021-12-06-our-sagemaker-processing-jobs-setup/thumbnail.png"
---

At [Snappet](https://us.snappet.org/) (we're [hiring](https://jobs.snappet.org/)!) we use Sagemaker processing jobs to power most of our machine learning workflow. 

Processing jobs create our data, train our models, and hypertune our parameters.

I think it is interesting enough to share about and show you how it works.

As of writing this, most of machine learning models still ran from Jupyter notebooks, but we are working hard turning them into robust ML pipelines.

![](/../assets/2021-12-06-our-sagemaker-processing-jobs-setup/thumbnail.png)

## 1. Creating the processing job

The first step in this whole process is creating the processing job. Usually this gets called from a Jupyter notebook.

We pass the input path (`input_path`), output path (`output_path`), and the arguments (`foo`) to the processing job. We turn them into a stringified list that Sagemaker understands.

```bash
args = {
    'input_path': '/opt/ml/processing/input', 
    'output_path': '/opt/ml/processing/output', 
    'foo': 'bar',
}
args_list = []
_ = [args_list.extend([f"--{key}", value]) for key, value in args.items()]
```

Creating a processing job is as easy as importing the `Processor` and specifying an entrypoint (`entrypoint`) and a docker image uri (`image_uri`). For brevity I ommitted some of the other parameters.

```python
from sagemaker.processing import Processor

proc = Processor(
    entrypoint=["python", "-u", "src/entrypoint.py"], 
    base_job_name=...,  # some descriptive name
    role=...,  # aws role
    image_uri=image_uri, # docker image pushed to ECR
    instance_type='ml.r5.24xlarge',  # for example
)
```

## 2. Running the processing job

After creating the processing job, we can run it. For this we use `ProcessingInput` and `ProcessingOutput`.

```python
from sagemaker.processing import ProcessingInput, ProcessingOutput

proc.run(
    inputs = [
        ProcessingInput(
            source=f"s3://{model_name}/{run_name}/input/",
            destination=args['input_path']
        )
    ],
    outputs = [
        ProcessingOutput(
            source=args['output_path'],
            destination=f"s3://{model_name}/{run_name}/output/",
            s3_upload_mode='EndOfJob'
        )
    ],
    arguments=args_list
)
```

`ProcessingInput` allows us to download the data to the `input_path` and `ProcessingOutput` allows us to upload the results to the `output_path`. For example, input data could be the training data, and the output data could be the model weights.

## 3. Building the docker

That's cool, but where does this entrypoint come from? The entrypoint is part of an image that we build using a `dockerfile`. 

Our docker files are quite basic, but we clearly separate the source code from the entrypoints, and we use `poetry` as our package manager.

```dockerfile
FROM python:3.8-slim-buster

WORKDIR "/opt"

# Dependencies
COPY poetry.lock .
COPY pyproject.toml .
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Entrypoints
COPY /entrypoints/ /opt/src/

# Core
COPY /src/ /opt/src/

# Git
RUN echo "SOURCE_COMMIT: $SOURCE_COMMIT"

# Entrypoint (doesn't do anything)
ENTRYPOINT ["python", "-u", "src/entrypoint.py"]
```

Using a build script we build the docker and push it to our image repository, for which we use [Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/). The `image_uri` is then passed as a parameter to the processing job when creating it.

Note that the `ENTRYPOINT` in the last line gets overwritten by the Sagemaker's entrypoint and is effectively useless.

## 4. Entering the entrypoint

The last piece of the puzzle is the actual entrypoint. The entrypoint is a simple `argparse` that parses the input arguments. 

By clearly defining the entrypoint of the program we have a strong and clean interface to the code. The code is like a black box, you can run it by just looking at the entrypoint.

Most of our entrypoints look something like this:

```python
import argparse
import json
import logging 

from src.models.data.handlers import PreprocessingHandler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--input_path', type=str, default='/opt/ml/processing/input/', help='path to save input data to ')
    parser.add_argument('--output_path', type=str, default='/opt/ml/processing/output/', help='path to save output data to')
    parser.add_argument('--foo', type=str, default='bar', help="all other parameters")

    args, _ = parser.parse_known_args()
    param_dict = copy.copy(vars(args))

    logging.info(f"Using arguments {json.dumps(param_dict, indent=2)}")

    preprocessing_handler = PreprocessingHandler(
        input_path=param_dict["input_path"],
        foo=param_dict["bar"],
    )
    preprocessing_handler.run(output_path=param_dict['output_path'])
```

## Conclusion

This is the rough structure that our pipelines follow at the moment. The structure has served us quite well and we are in the process of turning them into robust pipelines using either Airflow or Sagemaker Pipelines. 

To recap: 

* We run a a `ProcessingJob` from an `image_uri` located in our Amazon ECR
* Data comes in through `ProcessingInput` and exits through `ProcessingOutput` 
* We have a well-defined `ENTRYPOINT` in the form of an `argparse`

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
