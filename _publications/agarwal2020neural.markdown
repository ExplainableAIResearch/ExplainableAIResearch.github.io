---
layout: publication
title: "Neural Additive Models: Interpretable Machine Learning with Neural Nets"
authors: Rishabh Agarwal, Levi Melnick, Nicholas Frosst, Xuezhou Zhang, Ben Lengerich, Rich Caruana, Geoffrey Hinton
conference: 
year: 2020
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2004.13912v2"}
tags: []
---
Deep neural networks (DNNs) are powerful black-box predictors that have
achieved impressive performance on a wide variety of tasks. However, their
accuracy comes at the cost of intelligibility: it is usually unclear how they
make their decisions. This hinders their applicability to high stakes
decision-making domains such as healthcare. We propose Neural Additive Models
(NAMs) which combine some of the expressivity of DNNs with the inherent
intelligibility of generalized additive models. NAMs learn a linear combination
of neural networks that each attend to a single input feature. These networks
are trained jointly and can learn arbitrarily complex relationships between
their input feature and the output. Our experiments on regression and
classification datasets show that NAMs are more accurate than widely used
intelligible models such as logistic regression and shallow decision trees.
They perform similarly to existing state-of-the-art generalized additive models
in accuracy, but are more flexible because they are based on neural nets
instead of boosted trees. To demonstrate this, we show how NAMs can be used for
multitask learning on synthetic data and on the COMPAS recidivism data due to
their composability, and demonstrate that the differentiability of NAMs allows
them to train more complex interpretable models for COVID-19.