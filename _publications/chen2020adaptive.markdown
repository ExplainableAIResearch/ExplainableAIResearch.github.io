---
layout: publication
title: "Adaptive Explainable Neural Networks (AxNNs)"
authors: Jie Chen, Joel Vaughan, Vijayan N. Nair, Agus Sudjianto
conference: 
year: 2020
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2004.02353v2"}
tags: []
---
While machine learning techniques have been successfully applied in several
fields, the black-box nature of the models presents challenges for interpreting
and explaining the results. We develop a new framework called Adaptive
Explainable Neural Networks (AxNN) for achieving the dual goals of good
predictive performance and model interpretability. For predictive performance,
we build a structured neural network made up of ensembles of generalized
additive model networks and additive index models (through explainable neural
networks) using a two-stage process. This can be done using either a boosting
or a stacking ensemble. For interpretability, we show how to decompose the
results of AxNN into main effects and higher-order interaction effects. The
computations are inherited from Google's open source tool AdaNet and can be
efficiently accelerated by training with distributed computing. The results are
illustrated on simulated and real datasets.