---
title: "8-Step Machine Learning Checklist"
date: 2020-11-20
categories:
  - blog
tags:
  - machine learning
  - checklist 
  - blog
header:
  teaser: "/../assets/2020-11-20-machine-learning-checklist/2020-11-20-14-01-26.png"
---

![](/../assets/2020-11-20-machine-learning-checklist/2020-11-20-14-01-26.png)

<!-- What is the value for the user/reader?  -->

Use this 8-step machine learning checklist to guide you through your machine learning projects.

I found this checklist the appendix of [Hands-On Machine Learning with Scikit-Learn and TensorFlow](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1491962291).
Every machine learning project should use this checklist, or at least part of
it.

The checklist: 

1. Frame the problem and look at the big picture.
2. Get the data.
3. Explore the data to gain insights.
4. Prepare the data to better expose the underlying data patterns to machine learning algorithms.
5. Explore many different models and shortlist the best ones.
6. Fine-tune your models and combine them into a great solution.
7. Present your solution.
8. Launch, monitor, and maintain your system.

# Step 1: Frame the problem and look at the big picture.

![](/../assets/2020-11-20-machine-learning-checklist/2020-11-20-13-58-51.png)

In this step you frame the problem and try to look at the big picture. This
step answers questions such as: What problem are we solving? What business
objective does it solve? Who is going to consume my solution? What is the
current solution? At the end of this step you'll have a solid grasp of the
big picture of what you're solving.

Checklist: 

1. Define the objective in business terms.
2. How will your solution be used?
3. What are the current solutions/workarounds (if any)?
4. How should you frame this problem (supervised/unsupervised, online/offline, etc.)?
5. How should performance be measured?
6. Is the performance measure aligned with the business objective?
7. What would be the minimum performance needed to reach the business objective?
8. What are comparable problems? Can you reuse experience or tools?
9. Is human expertise available?
10. How would you solve the problem manually?
11. List the assumptions you (or others) have made so far.
12. Verify assumptions if possible.

# Step 2: Get the data

![](/../assets/2020-11-20-machine-learning-checklist/2020-11-20-13-59-17.png)

In the second step we fetch the data. Try to automate as much as possible so
you always have the freshest data. At the end of this step you will have a
raw dataset.

Checklist: 

1. List the data you need and how much you need.
2. Find and document where you can get that data.
3. Create a workspace (with enough storage space).
4. Get the data.
5. Convert the data to a format you can easily manipulate (without changing the data itself).
6. Ensure sensitive information is deleted or protected.
7. Check the size and type of data (time series, sample, geographical, etc.).
8. Sample a test set, put it aside, and never look at it.

# Step 3: Explore the data

![](/../assets/2020-11-20-machine-learning-checklist/2020-11-20-13-59-30.png)

In the third step do exploratory data analysis (EDA). We explore the data and
try to figure out the "health" and "shape" of the data (missing values,
distributions, etc.) At the end of this step you'll have a solid
understanding and feel of the dataset.

Checklist: 

1. Create a copy of the data for exploration (sampling it down to a manageable size if necessary).
2. Create a Jupyter notebook to keep a record of your data exploration.
3. Study each attribute and its characteristics:
    - Name
    - Type (categorical, int/float, bounded/unbounded, text, structured, etc.)
    - % of missing values
    - Noisiness and type of noise (stochastic, outliers, rounding errors, etc.)
    - Usefulness for the task
    - Type of distribution (Gaussian, uniform, logarithmic, etc.)
4. For supervised learning tasks, identify the target attribute(s).
5. Visualize the data.
6. Study the correlations between attributes.
7. Study how you would solve the problem manually.
8. Identify the promising transformations you may want to apply.
9. Identify extra data that would be useful. 
10. Document what you have learned.

# Step 4: Prepare the data

![](/../assets/2020-11-20-machine-learning-checklist/2020-11-20-13-59-50.png)

In this step you're going to prepare the data. At the end of this step you'll
have a set of functions/transformers that perform data transformations. These
transformers turn your raw data into preprocessed cleaned data, ready to be
used by machine learning algorithms.

**Set yourself up for success by writing functions for your data
transformations!**
{: .notice--success}

Write functions for all data transformations you apply, for five reasons:
  - So you can easily prepare the data the next time you get a fresh dataset 
  - So you can apply these transformations in future projects
  - To clean and prepare the test set
  - To clean and prepare new data instances once your solution is live
  - To make it easy to treat your preparation choices as hyperparameters

Checklist: 

1. Data cleaning:
  - Fix or remove outliers (optional).
  - Fill in missing values (e.g., with zero, mean, median...) or drop their rows (or columns).
2. Feature selection (optional):
  - Drop the attributes that provide no useful information for the task.
3. Feature engineering, where appropriate: 
  - Discretize continuous features.
  - Decompose features (e.g., categorical, date/time, etc.).
  - Add promising transformations of features (e.g., log(x), sqrt(x), x2, etc.).
  - Aggregate features into promising new features.
4. Feature scaling:
  - Standardize or normalize features.


# Step 5: Explore different models 

![](/../assets/2020-11-20-machine-learning-checklist/2020-11-20-14-00-02.png)

Checklist: 

1. Train many quick-and-dirty models from different categories (e.g., linear,
   naive Bayes, SVM, Random Forest, neural net, etc.) using standard
   parameters.
2. Measure and compare their performance.
  - For each model, use N-fold cross-validation and compute the mean and standard deviation of the performance measure on the N folds.
3. Analyze the most significant variables for each algorithm.
4. Analyze the types of errors the models make.
  - What data would a human have used to avoid these errors?
5. Perform a quick round of feature selection and engineering.
6. Perform one or two more quick iterations of the five previous steps.
7. Shortlist the top three to five most promising models, preferring models
   that make different types of errors.

# Step 6: Fine-tune your models and combine them into a great solution.

![](/../assets/2020-11-20-machine-learning-checklist/2020-11-20-14-00-12.png)

Don’t tweak your model after measuring the generalization error: you would just
start overfitting the test set.
{: .notice--warning}

Checklist: 

1. Fine-tune the hyperparameters using cross-validation:
  - Treat your data transformation choices as hyperparameters, especially when
    you are not sure about them (e.g., if you’re not sure whether to replace
    missing values with zeros or with the median value, or to just drop the
    rows).
  - Unless there are very few hyperparameter values to explore, prefer random
    search over grid search. If training is very long, you may prefer a
    Bayesian optimization approach (e.g., using Gaussian process priors, as
    described by Jasper Snoek et al.).1
2. Try Ensemble methods. Combining your best models will often produce better
   performance than running them individually.
3. Once you are confident about your final model, measure its performance on
   the test set to estimate the generalization error.

# Step 7: Present your solution.

![](/../assets/2020-11-20-machine-learning-checklist/2020-11-20-14-00-22.png)

Checklist: 

1. Document what you have done.
2. Create a nice presentation.
  - Make sure you highlight the big picture first.
3. Explain why your solution achieves the business objective.
4. Don’t forget to present interesting points you noticed along the way.
  - Describe what worked and what did not.
  - List your assumptions and your system’s limitations.
5. Ensure your key findings are communicated through beautiful visualizations
   or easy-to-remember statements (e.g., "the median income is the number-one
   predictor of housing prices").

# Step 8: Launch, monitor, and maintain your system.

![](/../assets/2020-11-20-machine-learning-checklist/2020-11-20-14-02-21.png)

Checklist: 

1. Get your solution ready for production (plug into production data inputs,
   write unit tests, etc.).
2. Write monitoring code to check your system’s live performance at regular
   intervals and trigger alerts when it drops.
  - Beware of slow degradation: models tend to "rot" as data evolves.
  - Measuring performance may require a human pipeline.
  - Also monitor your input's quality.
3. Retrain your models on a regular basis on fresh data (automate as much as possible).
