---
title: "snappet pipeline 1" 
date: 2023-03-23
---

we are building a unified architecture now for pipelines at snappet

this is cool

question to answer: what is our first output going to be? our milestone? simple model with some features

steps of the pipeline we are setting up

* data prep
* train (offline and online)
* evaluation (user trace)
* postprocessing
* deployment

some things to take into account

* we must support sequences from the start: some models use raw rows and others use sequences, we must handle this
* we want our models to work in snappet ids and have the model as part of the mapper
* we want to handle cold starts (unknown ids) gracefully with defaults or non predictions
* pad and ignore for data prep otherwise missing data becomes a thing
* model should be able to init lightweight
* after training model should have schema/translation baked in

