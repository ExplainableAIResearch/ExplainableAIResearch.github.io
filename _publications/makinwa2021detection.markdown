---
layout: publication
title: "Detection Accuracy for Evaluating Compositional Explanations of Units"
authors: Sayo M. Makinwa, Biagio La Rosa, Roberto Capobianco
conference: 
year: 2021
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2109.07804v2"}
tags: []
---
The recent success of deep learning models in solving complex problems and in
different domains has increased interest in understanding what they learn.
Therefore, different approaches have been employed to explain these models, one
of which uses human-understandable concepts as explanations. Two examples of
methods that use this approach are Network Dissection and Compositional
explanations. The former explains units using atomic concepts, while the latter
makes explanations more expressive, replacing atomic concepts with logical
forms. While intuitively, logical forms are more informative than atomic
concepts, it is not clear how to quantify this improvement, and their
evaluation is often based on the same metric that is optimized during the
search-process and on the usage of hyper-parameters to be tuned. In this paper,
we propose to use as evaluation metric the Detection Accuracy, which measures
units' consistency of detection of their assigned explanations. We show that
this metric (1) evaluates explanations of different lengths effectively, (2)
can be used as a stopping criterion for the compositional explanation search,
eliminating the explanation length hyper-parameter, and (3) exposes new
specialized units whose length 1 explanations are the perceptual abstractions
of their longer explanations.