---
layout: publication
title: "Learning Interpretable Shapelets for Time Series Classification through Adversarial Regularization"
authors: Yichang Wang, Rémi Emonet, Elisa Fromont, Simon Malinowski, Etienne Menager, Loïc Mosser, Romain Tavenard
conference: 
year: 2019
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/1906.00917v2"}
tags: []
---
Times series classification can be successfully tackled by jointly learning a
shapelet-based representation of the series in the dataset and classifying the
series according to this representation. However, although the learned
shapelets are discriminative, they are not always similar to pieces of a real
series in the dataset. This makes it difficult to interpret the decision, i.e.
difficult to analyze if there are particular behaviors in a series that
triggered the decision. In this paper, we make use of a simple convolutional
network to tackle the time series classification task and we introduce an
adversarial regularization to constrain the model to learn more interpretable
shapelets. Our classification results on all the usual time series benchmarks
are comparable with the results obtained by similar state-of-the-art algorithms
but our adversarially regularized method learns shapelets that are, by design,
interpretable.