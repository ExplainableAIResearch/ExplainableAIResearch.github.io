---
layout: publication
title: "Benchmarking Attribution Methods with Relative Feature Importance"
authors: Mengjiao Yang, Been Kim
conference: 
year: 2019
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1907.09701v2"}
tags: []
---
Interpretability is an important area of research for safe deployment of
machine learning systems. One particular type of interpretability method
attributes model decisions to input features. Despite active development,
quantitative evaluation of feature attribution methods remains difficult due to
the lack of ground truth: we do not know which input features are in fact
important to a model. In this work, we propose a framework for Benchmarking
Attribution Methods (BAM) with a priori knowledge of relative feature
importance. BAM includes 1) a carefully crafted dataset and models trained with
known relative feature importance and 2) three complementary metrics to
quantitatively evaluate attribution methods by comparing feature attributions
between pairs of models and pairs of inputs. Our evaluation on several
widely-used attribution methods suggests that certain methods are more likely
to produce false positive explanations---features that are incorrectly
attributed as more important to model prediction. We open source our dataset,
models, and metrics.