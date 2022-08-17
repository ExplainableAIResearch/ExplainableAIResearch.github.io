---
layout: publication
title: "The (Un)reliability of saliency methods"
authors: Pieter-Jan Kindermans, Sara Hooker, Julius Adebayo, Maximilian Alber, Kristof T. Schütt, Sven Dähne, Dumitru Erhan, Been Kim
conference: 
year: 2017
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1711.00867v1"}
tags: []
---
Saliency methods aim to explain the predictions of deep neural networks.
These methods lack reliability when the explanation is sensitive to factors
that do not contribute to the model prediction. We use a simple and common
pre-processing step ---adding a constant shift to the input data--- to show
that a transformation with no effect on the model can cause numerous methods to
incorrectly attribute. In order to guarantee reliability, we posit that methods
should fulfill input invariance, the requirement that a saliency method mirror
the sensitivity of the model with respect to transformations of the input. We
show, through several examples, that saliency methods that do not satisfy input
invariance result in misleading attribution.