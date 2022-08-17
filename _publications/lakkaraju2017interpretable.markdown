---
layout: publication
title: "Interpretable & Explorable Approximations of Black Box Models"
authors: Himabindu Lakkaraju, Ece Kamar, Rich Caruana, Jure Leskovec
conference: 
year: 2017
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1707.01154v1"}
tags: []
---
We propose Black Box Explanations through Transparent Approximations (BETA),
a novel model agnostic framework for explaining the behavior of any black-box
classifier by simultaneously optimizing for fidelity to the original model and
interpretability of the explanation. To this end, we develop a novel objective
function which allows us to learn (with optimality guarantees), a small number
of compact decision sets each of which explains the behavior of the black box
model in unambiguous, well-defined regions of feature space. Furthermore, our
framework also is capable of accepting user input when generating these
approximations, thus allowing users to interactively explore how the black-box
model behaves in different subspaces that are of interest to the user. To the
best of our knowledge, this is the first approach which can produce global
explanations of the behavior of any given black box model through joint
optimization of unambiguity, fidelity, and interpretability, while also
allowing users to explore model behavior based on their preferences.
Experimental evaluation with real-world datasets and user studies demonstrates
that our approach can generate highly compact, easy-to-understand, yet accurate
approximations of various kinds of predictive models compared to
state-of-the-art baselines.