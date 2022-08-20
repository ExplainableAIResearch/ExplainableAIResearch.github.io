---
layout: publication
title: "Interpretable Active Learning"
authors: Richard L. Phillips, Kyu Hyun Chang, Sorelle A. Friedler
conference: 
year: 2017
additional_links: 
	- {name: "ArXiv", url: "http://arxiv.org/abs/1708.00049v2"}
tags: []
---
Active learning has long been a topic of study in machine learning. However,
as increasingly complex and opaque models have become standard practice, the
process of active learning, too, has become more opaque. There has been little
investigation into interpreting what specific trends and patterns an active
learning strategy may be exploring. This work expands on the Local
Interpretable Model-agnostic Explanations framework (LIME) to provide
explanations for active learning recommendations. We demonstrate how LIME can
be used to generate locally faithful explanations for an active learning
strategy, and how these explanations can be used to understand how different
models and datasets explore a problem space over time. In order to quantify the
per-subgroup differences in how an active learning strategy queries spatial
regions, we introduce a notion of uncertainty bias (based on disparate impact)
to measure the discrepancy in the confidence for a model's predictions between
one subgroup and another. Using the uncertainty bias measure, we show that our
query explanations accurately reflect the subgroup focus of the active learning
queries, allowing for an interpretable explanation of what is being learned as
points with similar sources of uncertainty have their uncertainty bias
resolved. We demonstrate that this technique can be applied to track
uncertainty bias over user-defined clusters or automatically generated clusters
based on the source of uncertainty.