---
layout: publication
title: "Interpreting Neural Networks With Nearest Neighbors"
authors: Eric Wallace, Shi Feng, Jordan Boyd-Graber
conference: 
year: 2018
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/1809.02847v2"}
tags: []
---
Local model interpretation methods explain individual predictions by
assigning an importance value to each input feature. This value is often
determined by measuring the change in confidence when a feature is removed.
However, the confidence of neural networks is not a robust measure of model
uncertainty. This issue makes reliably judging the importance of the input
features difficult. We address this by changing the test-time behavior of
neural networks using Deep k-Nearest Neighbors. Without harming text
classification accuracy, this algorithm provides a more robust uncertainty
metric which we use to generate feature importance values. The resulting
interpretations better align with human perception than baseline methods.
Finally, we use our interpretation method to analyze model predictions on
dataset annotation artifacts.