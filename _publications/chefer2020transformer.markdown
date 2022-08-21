---
layout: publication
title: "Transformer Interpretability Beyond Attention Visualization"
authors: Hila Chefer, Shir Gur, Lior Wolf
conference: 
year: 2020
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2012.09838v2"}
tags: []
---
Self-attention techniques, and specifically Transformers, are dominating the
field of text processing and are becoming increasingly popular in computer
vision classification tasks. In order to visualize the parts of the image that
led to a certain classification, existing methods either rely on the obtained
attention maps or employ heuristic propagation along the attention graph. In
this work, we propose a novel way to compute relevancy for Transformer
networks. The method assigns local relevance based on the Deep Taylor
Decomposition principle and then propagates these relevancy scores through the
layers. This propagation involves attention layers and skip connections, which
challenge existing methods. Our solution is based on a specific formulation
that is shown to maintain the total relevancy across layers. We benchmark our
method on very recent visual Transformer networks, as well as on a text
classification problem, and demonstrate a clear advantage over the existing
explainability methods.