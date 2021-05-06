---
title: "Today I learned" 
date: 2021-05-04
categories:
  - blog
toc: false
toc_sticky: false
tags:
  - blog
  - til
header:
  teaser: ""
---

**Warning!** This is a draft! This post is being written as you are reading it!  I started this post on 2021-05-04 and will be updating it regularly until I think it contains enough to be considered done.
{: .notice--warning}

## 2021-05-04

Today I learned that this... well... works. This is how I created a value based on another value from my redux store.

```javascript
const messages = useSelector((state) => state.messages); 
const found = messages.find((message) => message.date == todayString); 
const todaysMessage = found ? found : undefined;   
const allThreeDone = found ? todaysMessage.answer1 != '' && todaysMessage.answer2 != '' && todaysMessage.answer3 != '' : undefined;
```

---

Today I learned how to count the amount of trues. 

```javascript
[false,false,true,false,true].filter(x => x).length // returns 2
```

---

Today I learned how to add opacity to an image in react-native

```javascript
<Image opacity={0.2} />
```

---

Today I learned how to copy your public key to your clipboard

```bash
pbcopy < ~/.ssh/id_rsa.pub
```

---

Today I learned how to check what shell you are using

```
echo $SHELL
```

---

Today I learned how to download a node with `wget` if you are ssh'd into a server

`wget https://nodejs.org/dist/v10.5.0/node-v10.5.0-linux-x64.tar.xz` 

# 2021-05-05

TIL how to plot a confusion matrix in `matplotlib`

```python
mat = confusion_matrix(y_true=eval_labels, y_pred=predicted_eval_labels)
ConfusionMatrixDisplay(mat, display_labels=class_names).plot()
```

---

TIL if you have a list and you want to turn it in a dictionary mapping, turn it into a numpy array.

```python
class_names = np.array(class_names) # => class_names = ["apple", "pear", "banana"]
class_names[eval_labels] # => class_names[[1, 0]] = ["pear", "apple"]
```

--

TIL if you want to save whatever figure, make a new figure with `plt.subplots()` and pass the `ax` object.

```python
fig, ax = plt.subplots()
confusion_mat = confusion_matrix(y_true=labels, y_pred=predicted_labels)
ConfusionMatrixDisplay(confusion_mat, display_labels=class_names).plot(xticks_rotation='vertical', ax=ax)
fig.savefig("tmp.png")
```

---

TIL that you should use `bbox_inches=tight` if your plots are showing correctly but `fig.savefig()` is clipping your axes.

---

TIL how to remove unused axes from images in a subplot

```python
def show_img_prediction_grid(imgs, labels, predicted_labels, class_names):
    """Shows a grid of images with predictions as coloured borders."""
    n = int(np.ceil(len(imgs)**.5))
    fig , axs = plt.subplots(n, n, figsize=(3 * n, 3 * n))
    for i, (img, label, predicted_label) in enumerate(zip(imgs, labels, predicted_labels)):
        title = f"Predicted: {class_names[predicted_label]}"
        show_img_prediction(img, label, predicted_label, class_names, ax=axs[i // n][i % n], title=title)
    
    # Delete empty axes
    # This works as follows: square n^2 which gives us the grid, subtract
    # the total amount of images we have, this gives us the number of last images that
    # are empty and we need to delete from the axes
    # only works if we don't have a square
    grid_size = n**2
    if grid_size % len(imgs) != 0:
        for i in np.arange(grid_size)[-(grid_size - len(imgs)):]:
            fig.delaxes(axs.flatten()[i])
```

---

TIL that order matters when using logical and (`&`) in Python. `a & b == c` is not the same as `a & (b == c)`. Duh.

# 2021-05-06

Today I learned that there is an ideal time to review your notes:

> SuperMemo is based on the insight that there is an ideal moment to practice what you've learned. Practice too soon and you waste your time. Practice too late and you've forgotten the material and have to relearn it. The right time to practice is just at the moment you're about to forget. Unfortunately, this moment is different for every person and each bit of information. Imagine a pile of thousands of flash cards. Somewhere in this pile are the ones you should be practicing right now. Which are they?

---

Today I learned that first step in debugging is *always* can I reproduce this bug?

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
  <label for="mce-EMAIL">Liked this article and want to hear more? Join 53 others and subscribe!</label>
  <input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email address" required>
    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
    <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_92fe86c389878585bc87837e8_50543deff9" tabindex="-1" value=""></div>
    <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
    </div>
</form>
</div>
<!--End mc_embed_signup-->
