---
layout: publication
title: "Interpretation of Neural Networks is Fragile"
authors: Amirata Ghorbani, Abubakar Abid, James Zou
conference: 
year: 2017
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/1710.10547v2"}
tags: []
---
In order for machine learning to be deployed and trusted in many
applications, it is crucial to be able to reliably explain why the machine
learning algorithm makes certain predictions. For example, if an algorithm
classifies a given pathology image to be a malignant tumor, then the doctor may
need to know which parts of the image led the algorithm to this classification.
How to interpret black-box predictors is thus an important and active area of
research. A fundamental question is: how much can we trust the interpretation
itself? In this paper, we show that interpretation of deep learning predictions
is extremely fragile in the following sense: two perceptively indistinguishable
inputs with the same predicted label can be assigned very different
interpretations. We systematically characterize the fragility of several
widely-used feature-importance interpretation methods (saliency maps, relevance
propagation, and DeepLIFT) on ImageNet and CIFAR-10. Our experiments show that
even small random perturbation can change the feature importance and new
systematic perturbations can lead to dramatically different interpretations
without changing the label. We extend these results to show that
interpretations based on exemplars (e.g. influence functions) are similarly
fragile. Our analysis of the geometry of the Hessian matrix gives insight on
why fragility could be a fundamental challenge to the current interpretation
approaches.