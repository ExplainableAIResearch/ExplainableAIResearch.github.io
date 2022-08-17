---
layout: publication
title: "Towards Understanding Knowledge Distillation"
authors: Mary Phuong, Christoph H. Lampert
conference: 
year: 2021
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2105.13093v1"}
tags: []
---
Knowledge distillation, i.e., one classifier being trained on the outputs of
another classifier, is an empirically very successful technique for knowledge
transfer between classifiers. It has even been observed that classifiers learn
much faster and more reliably if trained with the outputs of another classifier
as soft labels, instead of from ground truth data. So far, however, there is no
satisfactory theoretical explanation of this phenomenon. In this work, we
provide the first insights into the working mechanisms of distillation by
studying the special case of linear and deep linear classifiers. Specifically,
we prove a generalization bound that establishes fast convergence of the
expected risk of a distillation-trained linear classifier. From the bound and
its proof we extract three key factors that determine the success of
distillation: * data geometry -- geometric properties of the data distribution,
in particular class separation, has a direct influence on the convergence speed
of the risk; * optimization bias -- gradient descent optimization finds a very
favorable minimum of the distillation objective; and * strong monotonicity --
the expected risk of the student classifier always decreases when the size of
the training set grows.