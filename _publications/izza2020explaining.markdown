---
layout: publication
title: "On Explaining Decision Trees"
authors: Yacine Izza, Alexey Ignatiev, Joao Marques-Silva
conference: 
year: 2020
additional_links: 
	- {name: "ArXiv", url: "http://arxiv.org/abs/2010.11034v1"}
tags: []
---
Decision trees (DTs) epitomize what have become to be known as interpretable
machine learning (ML) models. This is informally motivated by paths in DTs
being often much smaller than the total number of features. This paper shows
that in some settings DTs can hardly be deemed interpretable, with paths in a
DT being arbitrarily larger than a PI-explanation, i.e. a subset-minimal set of
feature values that entails the prediction. As a result, the paper proposes a
novel model for computing PI-explanations of DTs, which enables computing one
PI-explanation in polynomial time. Moreover, it is shown that enumeration of
PI-explanations can be reduced to the enumeration of minimal hitting sets.
Experimental results were obtained on a wide range of publicly available
datasets with well-known DT-learning tools, and confirm that in most cases DTs
have paths that are proper supersets of PI-explanations.