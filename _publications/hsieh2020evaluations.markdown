---
layout: publication
title: "Evaluations and Methods for Explanation through Robustness Analysis"
authors: Cheng-Yu Hsieh, Chih-Kuan Yeh, Xuanqing Liu, Pradeep Ravikumar, Seungyeon Kim, Sanjiv Kumar, Cho-Jui Hsieh
conference: 
year: 2020
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2006.00442v2"}
tags: []
---
Feature based explanations, that provide importance of each feature towards
the model prediction, is arguably one of the most intuitive ways to explain a
model. In this paper, we establish a novel set of evaluation criteria for such
feature based explanations by robustness analysis. In contrast to existing
evaluations which require us to specify some way to "remove" features that
could inevitably introduces biases and artifacts, we make use of the subtler
notion of smaller adversarial perturbations. By optimizing towards our proposed
evaluation criteria, we obtain new explanations that are loosely necessary and
sufficient for a prediction. We further extend the explanation to extract the
set of features that would move the current prediction to a target class by
adopting targeted adversarial attack for the robustness analysis. Through
experiments across multiple domains and a user study, we validate the
usefulness of our evaluation criteria and our derived explanations.