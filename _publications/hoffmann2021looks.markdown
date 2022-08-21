---
layout: publication
title: "This Looks Like That... Does it? Shortcomings of Latent Space Prototype Interpretability in Deep Networks"
authors: Adrian Hoffmann, Claudio Fanconi, Rahul Rade, Jonas Kohler
conference: ICML 2021 Workshop on Theoretic Foundation, Criticism, and
  Application Trend of Explainable AI
year: 2021
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2105.02968v4"}
tags: []
---
Deep neural networks that yield human interpretable decisions by
architectural design have lately become an increasingly popular alternative to
post hoc interpretation of traditional black-box models. Among these networks,
the arguably most widespread approach is so-called prototype learning, where
similarities to learned latent prototypes serve as the basis of classifying an
unseen data point. In this work, we point to an important shortcoming of such
approaches. Namely, there is a semantic gap between similarity in latent space
and similarity in input space, which can corrupt interpretability. We design
two experiments that exemplify this issue on the so-called ProtoPNet.
Specifically, we find that this network's interpretability mechanism can be led
astray by intentionally crafted or even JPEG compression artefacts, which can
produce incomprehensible decisions. We argue that practitioners ought to have
this shortcoming in mind when deploying prototype-based models in practice.