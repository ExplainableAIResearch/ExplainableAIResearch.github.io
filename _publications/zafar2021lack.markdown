---
layout: publication
title: "On the Lack of Robust Interpretability of Neural Text Classifiers"
authors: Muhammad Bilal Zafar, Michele Donini, Dylan Slack, Cédric Archambeau, Sanjiv Das, Krishnaram Kenthapadi
conference: 
year: 2021
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2106.04631v1"}
tags: []
---
With the ever-increasing complexity of neural language models, practitioners
have turned to methods for understanding the predictions of these models. One
of the most well-adopted approaches for model interpretability is feature-based
interpretability, i.e., ranking the features in terms of their impact on model
predictions. Several prior studies have focused on assessing the fidelity of
feature-based interpretability methods, i.e., measuring the impact of dropping
the top-ranked features on the model output. However, relatively little work
has been conducted on quantifying the robustness of interpretations. In this
work, we assess the robustness of interpretations of neural text classifiers,
specifically, those based on pretrained Transformer encoders, using two
randomization tests. The first compares the interpretations of two models that
are identical except for their initializations. The second measures whether the
interpretations differ between a model with trained parameters and a model with
random parameters. Both tests show surprising deviations from expected
behavior, raising questions about the extent of insights that practitioners may
draw from interpretations.