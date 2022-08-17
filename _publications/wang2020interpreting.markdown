---
layout: publication
title: "Interpreting Interpretations: Organizing Attribution Methods by Criteria"
authors: Zifan Wang, Piotr Mardziel, Anupam Datta, Matt Fredrikson
conference: 
year: 2020
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2002.07985v2"}
tags: []
---
Motivated by distinct, though related, criteria, a growing number of
attribution methods have been developed tointerprete deep learning. While each
relies on the interpretability of the concept of "importance" and our ability
to visualize patterns, explanations produced by the methods often differ. As a
result, input attribution for vision models fail to provide any level of human
understanding of model behaviour. In this work we expand the foundationsof
human-understandable concepts with which attributionscan be interpreted beyond
"importance" and its visualization; we incorporate the logical concepts of
necessity andsufficiency, and the concept of proportionality. We definemetrics
to represent these concepts as quantitative aspectsof an attribution. This
allows us to compare attributionsproduced by different methods and interpret
them in novelways: to what extent does this attribution (or this
method)represent the necessity or sufficiency of the highlighted inputs, and to
what extent is it proportional? We evaluate our measures on a collection of
methods explaining convolutional neural networks (CNN) for image
classification. We conclude that some attribution methods are more appropriate
for interpretation in terms of necessity while others are in terms of
sufficiency, while no method is always the most appropriate in terms of both.