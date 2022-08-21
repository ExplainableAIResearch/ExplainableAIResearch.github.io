---
layout: publication
title: "Contrastive Explanations for Model Interpretability"
authors: Alon Jacovi, Swabha Swayamdipta, Shauli Ravfogel, Yanai Elazar, Yejin Choi, Yoav Goldberg
conference: 
year: 2021
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2103.01378v3"}
tags: []
---
Contrastive explanations clarify why an event occurred in contrast to
another. They are more inherently intuitive to humans to both produce and
comprehend. We propose a methodology to produce contrastive explanations for
classification models by modifying the representation to disregard
non-contrastive information, and modifying model behavior to only be based on
contrastive reasoning. Our method is based on projecting model representation
to a latent space that captures only the features that are useful (to the
model) to differentiate two potential decisions. We demonstrate the value of
contrastive explanations by analyzing two different scenarios, using both
high-level abstract concept attribution and low-level input token/span
attribution, on two widely used text classification tasks. Specifically, we
produce explanations for answering: for which label, and against which
alternative label, is some aspect of the input useful? And which aspects of the
input are useful for and against particular decisions? Overall, our findings
shed light on the ability of label-contrastive explanations to provide a more
accurate and finer-grained interpretability of a model's decision.