---
layout: publication
title: "Evaluating Robustness of Counterfactual Explanations"
authors: André Artelt, Valerie Vaquet, Riza Velioglu, Fabian Hinder, Johannes Brinkrolf, Malte Schilling, Barbara Hammer
conference: 
year: 2021
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2103.02354v3"}
tags: []
---
Transparency is a fundamental requirement for decision making systems when
these should be deployed in the real world. It is usually achieved by providing
explanations of the system's behavior. A prominent and intuitive type of
explanations are counterfactual explanations. Counterfactual explanations
explain a behavior to the user by proposing actions -- as changes to the input
-- that would cause a different (specified) behavior of the system. However,
such explanation methods can be unstable with respect to small changes to the
input -- i.e. even a small change in the input can lead to huge or arbitrary
changes in the output and of the explanation. This could be problematic for
counterfactual explanations, as two similar individuals might get very
different explanations. Even worse, if the recommended actions differ
considerably in their complexity, one would consider such unstable
(counterfactual) explanations as individually unfair.
  In this work, we formally and empirically study the robustness of
counterfactual explanations in general, as well as under different models and
different kinds of perturbations. Furthermore, we propose that plausible
counterfactual explanations can be used instead of closest counterfactual
explanations to improve the robustness and consequently the individual fairness
of counterfactual explanations.