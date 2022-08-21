---
layout: publication
title: "Locality Guided Neural Networks for Explainable Artificial Intelligence"
authors: Randy Tan, Naimul Khan, Ling Guan
conference: 
year: 2020
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2007.06131v1"}
tags: []
---
In current deep network architectures, deeper layers in networks tend to
contain hundreds of independent neurons which makes it hard for humans to
understand how they interact with each other. By organizing the neurons by
correlation, humans can observe how clusters of neighbouring neurons interact
with each other. In this paper, we propose a novel algorithm for back
propagation, called Locality Guided Neural Network(LGNN) for training networks
that preserves locality between neighbouring neurons within each layer of a
deep network. Heavily motivated by Self-Organizing Map (SOM), the goal is to
enforce a local topology on each layer of a deep network such that neighbouring
neurons are highly correlated with each other. This method contributes to the
domain of Explainable Artificial Intelligence (XAI), which aims to alleviate
the black-box nature of current AI methods and make them understandable by
humans. Our method aims to achieve XAI in deep learning without changing the
structure of current models nor requiring any post processing. This paper
focuses on Convolutional Neural Networks (CNNs), but can theoretically be
applied to any type of deep learning architecture. In our experiments, we train
various VGG and Wide ResNet (WRN) networks for image classification on
CIFAR100. In depth analyses presenting both qualitative and quantitative
results demonstrate that our method is capable of enforcing a topology on each
layer while achieving a small increase in classification accuracy