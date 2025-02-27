---
title: "How to refer to a file in Azure Devops"
date: 2025-02-27
tags:
# Blog or how-to
- tutorial
# Work or personal?
- work
# Start here themes
- systems
- devops

categories: blog
toc: false
toc_sticky: false
header:
    teaser: "/../assets/2025-02-27-how-to-refer-to-a-file-in-azure-devops/thumbnail.png"
---
<!-- ctrl + alt + v -->

Azure Devops is a necessary evil. I mean someone or something has to run my code, and I prefer it not being me. 

Last week, I ran into the case where I had to pull up a config from a file and load it into my pipeline. I asked ChatGPT and this is what I was told to do. 

To reference a specific file in Azure Devops, use the  `Build.SourcesDirectory` variable that is available for each build.

Say we want to refer to the file `models/active_models.json` which is input for `src/run.py` like this:

```json
$ tree
models
├── active_models.json
src
├── run.py
```

Then we can simply do this:

```bash
- task: AWSShellScript@1
  inputs:
    scriptType: 'inline'
    inlineScript: |
      python ./src/run.py --path $(Build.SourcesDirectory)/models/active_models.json
```


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
    