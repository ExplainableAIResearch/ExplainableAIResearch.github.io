---
layout: publication
title: "Growing Interpretable Part Graphs on ConvNets via Multi-Shot Learning"
authors: Quanshi Zhang, Ruiming Cao, Ying Nian Wu, Song-Chun Zhu
conference: 
year: 2016
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1611.04246v2"}
tags: []
---
This paper proposes a learning strategy that extracts object-part concepts
from a pre-trained convolutional neural network (CNN), in an attempt to 1)
explore explicit semantics hidden in CNN units and 2) gradually grow a
semantically interpretable graphical model on the pre-trained CNN for
hierarchical object understanding. Given part annotations on very few (e.g.,
3-12) objects, our method mines certain latent patterns from the pre-trained
CNN and associates them with different semantic parts. We use a four-layer
And-Or graph to organize the mined latent patterns, so as to clarify their
internal semantic hierarchy. Our method is guided by a small number of part
annotations, and it achieves superior performance (about 13%-107% improvement)
in part center prediction on the PASCAL VOC and ImageNet datasets.