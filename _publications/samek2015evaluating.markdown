---
layout: publication
title: "Evaluating the visualization of what a Deep Neural Network has learned"
authors: Wojciech Samek, Alexander Binder, Grégoire Montavon, Sebastian Bach, Klaus-Robert Müller
conference: 
year: 2015
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1509.06321v1"}
tags: []
---
Deep Neural Networks (DNNs) have demonstrated impressive performance in
complex machine learning tasks such as image classification or speech
recognition. However, due to their multi-layer nonlinear structure, they are
not transparent, i.e., it is hard to grasp what makes them arrive at a
particular classification or recognition decision given a new unseen data
sample. Recently, several approaches have been proposed enabling one to
understand and interpret the reasoning embodied in a DNN for a single test
image. These methods quantify the ''importance'' of individual pixels wrt the
classification decision and allow a visualization in terms of a heatmap in
pixel/input space. While the usefulness of heatmaps can be judged subjectively
by a human, an objective quality measure is missing. In this paper we present a
general methodology based on region perturbation for evaluating ordered
collections of pixels such as heatmaps. We compare heatmaps computed by three
different methods on the SUN397, ILSVRC2012 and MIT Places data sets. Our main
result is that the recently proposed Layer-wise Relevance Propagation (LRP)
algorithm qualitatively and quantitatively provides a better explanation of
what made a DNN arrive at a particular classification decision than the
sensitivity-based approach or the deconvolution method. We provide theoretical
arguments to explain this result and discuss its practical implications.
Finally, we investigate the use of heatmaps for unsupervised assessment of
neural network performance.