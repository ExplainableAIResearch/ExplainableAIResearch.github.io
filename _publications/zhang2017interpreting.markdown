---
layout: publication
title: "Interpreting CNN Knowledge via an Explanatory Graph"
authors: Quanshi Zhang, Ruiming Cao, Feng Shi, Ying Nian Wu, Song-Chun Zhu
conference: 
year: 2017
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1708.01785v3"}
tags: []
---
This paper learns a graphical model, namely an explanatory graph, which
reveals the knowledge hierarchy hidden inside a pre-trained CNN. Considering
that each filter in a conv-layer of a pre-trained CNN usually represents a
mixture of object parts, we propose a simple yet efficient method to
automatically disentangles different part patterns from each filter, and
construct an explanatory graph. In the explanatory graph, each node represents
a part pattern, and each edge encodes co-activation relationships and spatial
relationships between patterns. More importantly, we learn the explanatory
graph for a pre-trained CNN in an unsupervised manner, i.e., without a need of
annotating object parts. Experiments show that each graph node consistently
represents the same object part through different images. We transfer part
patterns in the explanatory graph to the task of part localization, and our
method significantly outperforms other approaches.