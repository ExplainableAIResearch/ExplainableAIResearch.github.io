---
layout: publication
title: "Attention-like feature explanation for tabular data"
authors: Andrei V. Konstantinov, Lev V. Utkin
conference: 
year: 2021
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2108.04855v1"}
tags: []
---
A new method for local and global explanation of the machine learning
black-box model predictions by tabular data is proposed. It is implemented as a
system called AFEX (Attention-like Feature EXplanation) and consisting of two
main parts. The first part is a set of the one-feature neural subnetworks which
aim to get a specific representation for every feature in the form of a basis
of shape functions. The subnetworks use shortcut connections with trainable
parameters to improve the network performance. The second part of AFEX produces
shape functions of features as the weighted sum of the basis shape functions
where weights are computed by using an attention-like mechanism. AFEX
identifies pairwise interactions between features based on pairwise
multiplications of shape functions corresponding to different features. A
modification of AFEX with incorporating an additional surrogate model which
approximates the black-box model is proposed. AFEX is trained end-to-end on a
whole dataset only once such that it does not require to train neural networks
again in the explanation stage. Numerical experiments with synthetic and real
data illustrate AFEX.