---
layout: publication
title: "Concept Whitening for Interpretable Image Recognition"
authors: Zhi Chen, Yijie Bei, Cynthia Rudin
conference: Nature Machine Intelligence, Vol 2, Dec 2020, 772-782
year: 2020
additional_links: 
    - {name: "ArXiv", url: "http://dx.doi.org/10.1038/s42256-020-00265-z"}
tags: []
---
What does a neural network encode about a concept as we traverse through the
layers? Interpretability in machine learning is undoubtedly important, but the
calculations of neural networks are very challenging to understand. Attempts to
see inside their hidden layers can either be misleading, unusable, or rely on
the latent space to possess properties that it may not have. In this work,
rather than attempting to analyze a neural network posthoc, we introduce a
mechanism, called concept whitening (CW), to alter a given layer of the network
to allow us to better understand the computation leading up to that layer. When
a concept whitening module is added to a CNN, the axes of the latent space are
aligned with known concepts of interest. By experiment, we show that CW can
provide us a much clearer understanding for how the network gradually learns
concepts over layers. CW is an alternative to a batch normalization layer in
that it normalizes, and also decorrelates (whitens) the latent space. CW can be
used in any layer of the network without hurting predictive performance.