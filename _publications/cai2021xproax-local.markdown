---
layout: publication
title: "XPROAX-Local explanations for text classification with progressive neighborhood approximation"
authors: Yi Cai, Arthur Zimek, Eirini Ntoutsi
conference: 
year: 2021
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2109.15004v1"}
tags: []
---
The importance of the neighborhood for training a local surrogate model to
approximate the local decision boundary of a black box classifier has been
already highlighted in the literature. Several attempts have been made to
construct a better neighborhood for high dimensional data, like texts, by using
generative autoencoders. However, existing approaches mainly generate neighbors
by selecting purely at random from the latent space and struggle under the
curse of dimensionality to learn a good local decision boundary. To overcome
this problem, we propose a progressive approximation of the neighborhood using
counterfactual instances as initial landmarks and a careful 2-stage sampling
approach to refine counterfactuals and generate factuals in the neighborhood of
the input instance to be explained. Our work focuses on textual data and our
explanations consist of both word-level explanations from the original instance
(intrinsic) and the neighborhood (extrinsic) and factual- and
counterfactual-instances discovered during the neighborhood generation process
that further reveal the effect of altering certain parts in the input text. Our
experiments on real-world datasets demonstrate that our method outperforms the
competitors in terms of usefulness and stability (for the qualitative part) and
completeness, compactness and correctness (for the quantitative part).