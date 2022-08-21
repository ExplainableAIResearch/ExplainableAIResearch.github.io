---
layout: publication
title: "Counterfactual Shapley Additive Explanations"
authors: Emanuele Albini, Jason Long, Danial Dervovic, Daniele Magazzeni
conference: 
year: 2021
additional_links: 
    - {name: "ArXiv", url: "http://dx.doi.org/10.1145/3531146.3533168"}
tags: []
---
Feature attributions are a common paradigm for model explanations due to
their simplicity in assigning a single numeric score for each input feature to
a model. In the actionable recourse setting, wherein the goal of the
explanations is to improve outcomes for model consumers, it is often unclear
how feature attributions should be correctly used. With this work, we aim to
strengthen and clarify the link between actionable recourse and feature
attributions. Concretely, we propose a variant of SHAP, Counterfactual SHAP
(CF-SHAP), that incorporates counterfactual information to produce a background
dataset for use within the marginal (a.k.a. interventional) Shapley value
framework. We motivate the need within the actionable recourse setting for
careful consideration of background datasets when using Shapley values for
feature attributions with numerous synthetic examples. Moreover, we demonstrate
the efficacy of CF-SHAP by proposing and justifying a quantitative score for
feature attributions, counterfactual-ability, showing that as measured by this
metric, CF-SHAP is superior to existing methods when evaluated on public
datasets using tree ensembles.