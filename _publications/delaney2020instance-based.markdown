---
layout: publication
title: "Instance-based Counterfactual Explanations for Time Series Classification"
authors: Eoin Delaney, Derek Greene, Mark T. Keane
conference: 
year: 2020
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2009.13211v2"}
tags: []
---
In recent years, there has been a rapidly expanding focus on explaining the
predictions made by black-box AI systems that handle image and tabular data.
However, considerably less attention has been paid to explaining the
predictions of opaque AI systems handling time series data. In this paper, we
advance a novel model-agnostic, case-based technique -- Native Guide -- that
generates counterfactual explanations for time series classifiers. Given a
query time series, $T_{q}$, for which a black-box classification system
predicts class, $c$, a counterfactual time series explanation shows how $T_{q}$
could change, such that the system predicts an alternative class, $c'$. The
proposed instance-based technique adapts existing counterfactual instances in
the case-base by highlighting and modifying discriminative areas of the time
series that underlie the classification. Quantitative and qualitative results
from two comparative experiments indicate that Native Guide generates
plausible, proximal, sparse and diverse explanations that are better than those
produced by key benchmark counterfactual methods.