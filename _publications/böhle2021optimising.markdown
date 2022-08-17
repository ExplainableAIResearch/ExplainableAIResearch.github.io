---
layout: publication
title: "Optimising for Interpretability: Convolutional Dynamic Alignment Networks"
authors: Moritz Böhle, Mario Fritz, Bernt Schiele
conference: 
year: 2021
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2109.13004v1"}
tags: []
---
We introduce a new family of neural network models called Convolutional
Dynamic Alignment Networks (CoDA Nets), which are performant classifiers with a
high degree of inherent interpretability. Their core building blocks are
Dynamic Alignment Units (DAUs), which are optimised to transform their inputs
with dynamically computed weight vectors that align with task-relevant
patterns. As a result, CoDA Nets model the classification prediction through a
series of input-dependent linear transformations, allowing for linear
decomposition of the output into individual input contributions. Given the
alignment of the DAUs, the resulting contribution maps align with
discriminative input patterns. These model-inherent decompositions are of high
visual quality and outperform existing attribution methods under quantitative
metrics. Further, CoDA Nets constitute performant classifiers, achieving on par
results to ResNet and VGG models on e.g. CIFAR-10 and TinyImagenet. Lastly,
CoDA Nets can be combined with conventional neural network models to yield
powerful classifiers that more easily scale to complex datasets such as
Imagenet whilst exhibiting an increased interpretable depth, i.e., the output
can be explained well in terms of contributions from intermediate layers within
the network.