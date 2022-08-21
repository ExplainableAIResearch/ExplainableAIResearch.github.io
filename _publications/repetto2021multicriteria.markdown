---
layout: publication
title: "Multicriteria interpretability driven Deep Learning"
authors: Marco Repetto
conference: 
year: 2021
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2111.14088v1"}
tags: []
---
Deep Learning methods are renowned for their performances, yet their lack of
interpretability prevents them from high-stakes contexts. Recent model agnostic
methods address this problem by providing post-hoc interpretability methods by
reverse-engineering the model's inner workings. However, in many regulated
fields, interpretability should be kept in mind from the start, which means
that post-hoc methods are valid only as a sanity check after model training.
Interpretability from the start, in an abstract setting, means posing a set of
soft constraints on the model's behavior by injecting knowledge and
annihilating possible biases. We propose a Multicriteria technique that allows
to control the feature effects on the model's outcome by injecting knowledge in
the objective function. We then extend the technique by including a non-linear
knowledge function to account for more complex effects and local lack of
knowledge. The result is a Deep Learning model that embodies interpretability
from the start and aligns with the recent regulations. A practical empirical
example based on credit risk, suggests that our approach creates performant yet
robust models capable of overcoming biases derived from data scarcity.