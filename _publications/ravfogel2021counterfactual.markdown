---
layout: publication
title: "Counterfactual Interventions Reveal the Causal Effect of Relative Clause Representations on Agreement Prediction"
authors: Shauli Ravfogel, Grusha Prasad, Tal Linzen, Yoav Goldberg
conference: 
year: 2021
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2105.06965v3"}
tags: []
---
When language models process syntactically complex sentences, do they use
their representations of syntax in a manner that is consistent with the grammar
of the language? We propose AlterRep, an intervention-based method to address
this question. For any linguistic feature of a given sentence, AlterRep
generates counterfactual representations by altering how the feature is
encoded, while leaving intact all other aspects of the original representation.
By measuring the change in a model's word prediction behavior when these
counterfactual representations are substituted for the original ones, we can
draw conclusions about the causal effect of the linguistic feature in question
on the model's behavior. We apply this method to study how BERT models of
different sizes process relative clauses (RCs). We find that BERT variants use
RC boundary information during word prediction in a manner that is consistent
with the rules of English grammar; this RC boundary information generalizes to
a considerable extent across different RC types, suggesting that BERT
represents RCs as an abstract linguistic category.