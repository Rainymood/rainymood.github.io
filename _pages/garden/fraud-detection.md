---
title: "fraud detection" 
date: 2023-03-24
---

building a small model for fraud detection now

usually very imbalanced datasets

think about how you want to split the dataset, scale it, and then resample the dataset

train the model on the undersampled or oversampled dataset

then get the train/validation/test predictions on the complete dataset

sampling:

* sample stratified and on the train set
* split train/test stratified as well

metrics:

* never use acccuracy
* AUC/ROC/F1/precision/recall

