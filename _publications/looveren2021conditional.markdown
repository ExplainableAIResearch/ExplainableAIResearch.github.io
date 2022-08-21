---
layout: publication
title: "Conditional Generative Models for Counterfactual Explanations"
authors: Arnaud Van Looveren, Janis Klaise, Giovanni Vacanti, Oliver Cobb
conference: 
year: 2021
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2101.10123v1"}
tags: []
---
Counterfactual instances offer human-interpretable insight into the local
behaviour of machine learning models. We propose a general framework to
generate sparse, in-distribution counterfactual model explanations which match
a desired target prediction with a conditional generative model, allowing
batches of counterfactual instances to be generated with a single forward pass.
The method is flexible with respect to the type of generative model used as
well as the task of the underlying predictive model. This allows
straightforward application of the framework to different modalities such as
images, time series or tabular data as well as generative model paradigms such
as GANs or autoencoders and predictive tasks like classification or regression.
We illustrate the effectiveness of our method on image (CelebA), time series
(ECG) and mixed-type tabular (Adult Census) data.