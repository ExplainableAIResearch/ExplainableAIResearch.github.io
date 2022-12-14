---
layout: publication
title: "Understanding Learned Models by Identifying Important Features at the Right Resolution"
authors: Kyubin Lee, Akshay Sood, Mark Craven
conference: 
year: 2018
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/1811.07279v2"}
tags: []
---
In many application domains, it is important to characterize how complex
learned models make their decisions across the distribution of instances. One
way to do this is to identify the features and interactions among them that
contribute to a model's predictive accuracy. We present a model-agnostic
approach to this task that makes the following specific contributions. Our
approach (i) tests feature groups, in addition to base features, and tries to
determine the level of resolution at which important features can be
determined, (ii) uses hypothesis testing to rigorously assess the effect of
each feature on the model's loss, (iii) employs a hierarchical approach to
control the false discovery rate when testing feature groups and individual
base features for importance, and (iv) uses hypothesis testing to identify
important interactions among features and feature groups. We evaluate our
approach by analyzing random forest and LSTM neural network models learned in
two challenging biomedical applications.