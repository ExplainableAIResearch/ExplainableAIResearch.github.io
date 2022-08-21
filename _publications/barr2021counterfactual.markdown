---
layout: publication
title: "Counterfactual Explanations via Latent Space Projection and Interpolation"
authors: Brian Barr, Matthew R. Harrington, Samuel Sharpe, C. Bayan Bruss
conference: 
year: 2021
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2112.00890v1"}
tags: []
---
Counterfactual explanations represent the minimal change to a data sample
that alters its predicted classification, typically from an unfavorable initial
class to a desired target class. Counterfactuals help answer questions such as
"what needs to change for this application to get accepted for a loan?". A
number of recently proposed approaches to counterfactual generation give
varying definitions of "plausible" counterfactuals and methods to generate
them. However, many of these methods are computationally intensive and provide
unconvincing explanations. Here we introduce SharpShooter, a method for binary
classification that starts by creating a projected version of the input that
classifies as the target class. Counterfactual candidates are then generated in
latent space on the interpolation line between the input and its projection. We
then demonstrate that our framework translates core characteristics of a sample
to its counterfactual through the use of learned representations. Furthermore,
we show that SharpShooter is competitive across common quality metrics on
tabular and image datasets while being orders of magnitude faster than two
comparable methods and excels at measures of realism, making it well-suited for
high velocity machine learning applications which require timely explanations.