---
layout: publication
title: "Contextual Semantic Interpretability"
authors: Diego Marcos, Ruth Fong, Sylvain Lobry, Remi Flamary, Nicolas Courty, Devis Tuia
conference: ACCV 2020
year: 2020
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2009.08720v1"}
tags: []
---
Convolutional neural networks (CNN) are known to learn an image
representation that captures concepts relevant to the task, but do so in an
implicit way that hampers model interpretability. However, one could argue that
such a representation is hidden in the neurons and can be made explicit by
teaching the model to recognize semantically interpretable attributes that are
present in the scene. We call such an intermediate layer a \emph{semantic
bottleneck}. Once the attributes are learned, they can be re-combined to reach
the final decision and provide both an accurate prediction and an explicit
reasoning behind the CNN decision. In this paper, we look into semantic
bottlenecks that capture context: we want attributes to be in groups of a few
meaningful elements and participate jointly to the final decision. We use a
two-layer semantic bottleneck that gathers attributes into interpretable,
sparse groups, allowing them contribute differently to the final output
depending on the context. We test our contextual semantic interpretable
bottleneck (CSIB) on the task of landscape scenicness estimation and train the
semantic interpretable bottleneck using an auxiliary database (SUN Attributes).
Our model yields in predictions as accurate as a non-interpretable baseline
when applied to a real-world test set of Flickr images, all while providing
clear and interpretable explanations for each prediction.