---
layout: publication
title: "Convolutional Dynamic Alignment Networks for Interpretable Classifications"
authors: Moritz Böhle, Mario Fritz, Bernt Schiele
conference: 
year: 2021
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2104.00032v1"}
tags: []
---
We introduce a new family of neural network models called Convolutional
Dynamic Alignment Networks (CoDA-Nets), which are performant classifiers with a
high degree of inherent interpretability. Their core building blocks are
Dynamic Alignment Units (DAUs), which linearly transform their input with
weight vectors that dynamically align with task-relevant patterns. As a result,
CoDA-Nets model the classification prediction through a series of
input-dependent linear transformations, allowing for linear decomposition of
the output into individual input contributions. Given the alignment of the
DAUs, the resulting contribution maps align with discriminative input patterns.
These model-inherent decompositions are of high visual quality and outperform
existing attribution methods under quantitative metrics. Further, CoDA-Nets
constitute performant classifiers, achieving on par results to ResNet and VGG
models on e.g. CIFAR-10 and TinyImagenet.