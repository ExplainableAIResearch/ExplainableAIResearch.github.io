---
layout: publication
title: "The Solvability of Interpretability Evaluation Metrics"
authors: Yilun Zhou, Julie Shah
conference: 
year: 2022
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2205.08696v1"}
tags: []
---
Feature attribution methods are popular for explaining neural network
predictions, and they are often evaluated on metrics such as comprehensiveness
and sufficiency, which are motivated by the principle that more important
features -- as judged by the explanation -- should have larger impacts on model
prediction. In this paper, we highlight an intriguing property of these
metrics: their solvability. Concretely, we can define the problem of optimizing
an explanation for a metric and solve it using beam search. This brings up the
obvious question: given such solvability, why do we still develop other
explainers and then evaluate them on the metric? We present a series of
investigations showing that this beam search explainer is generally comparable
or favorable to current choices such as LIME and SHAP, suggest rethinking the
goals of model interpretability, and identify several directions towards better
evaluations of new method proposals.