---
layout: publication
title: "Learning Interpretable Models with Causal Guarantees"
authors: Carolyn Kim, Osbert Bastani
conference: 
year: 2019
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1901.08576v2"}
tags: []
---
Machine learning has shown much promise in helping improve the quality of
medical, legal, and financial decision-making. In these applications, machine
learning models must satisfy two important criteria: (i) they must be causal,
since the goal is typically to predict individual treatment effects, and (ii)
they must be interpretable, so that human decision makers can validate and
trust the model predictions. There has recently been much progress along each
direction independently, yet the state-of-the-art approaches are fundamentally
incompatible. We propose a framework for learning interpretable models from
observational data that can be used to predict individual treatment effects
(ITEs). In particular, our framework converts any supervised learning algorithm
into an algorithm for estimating ITEs. Furthermore, we prove an error bound on
the treatment effects predicted by our model. Finally, in an experiment on
real-world data, we show that the models trained using our framework
significantly outperform a number of baselines.