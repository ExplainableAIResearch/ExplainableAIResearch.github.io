---
layout: publication
title: "Explanatory Graphs for CNNs"
authors: Quanshi Zhang, Xin Wang, Ruiming Cao, Ying Nian Wu, Feng Shi, Song-Chun Zhu
conference: 
year: 2018
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1812.07997v1"}
tags: []
---
This paper introduces a graphical model, namely an explanatory graph, which
reveals the knowledge hierarchy hidden inside conv-layers of a pre-trained CNN.
Each filter in a conv-layer of a CNN for object classification usually
represents a mixture of object parts. We develop a simple yet effective method
to disentangle object-part pattern components from each filter. We construct an
explanatory graph to organize the mined part patterns, where a node represents
a part pattern, and each edge encodes co-activation relationships and spatial
relationships between patterns. More crucially, given a pre-trained CNN, the
explanatory graph is learned without a need of annotating object parts.
Experiments show that each graph node consistently represented the same object
part through different images, which boosted the transferability of CNN
features. We transferred part patterns in the explanatory graph to the task of
part localization, and our method significantly outperformed other approaches.