---
layout: publication
title: "Interpretable Neural Network Decoupling"
authors: Yuchao Li, Rongrong Ji, Shaohui Lin, Baochang Zhang, Chenqian Yan, Yongjian Wu, Feiyue Huang, Ling Shao
conference: 
year: 2019
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1906.01166v2"}
tags: []
---
The remarkable performance of convolutional neural networks (CNNs) is
entangled with their huge number of uninterpretable parameters, which has
become the bottleneck limiting the exploitation of their full potential.
Towards network interpretation, previous endeavors mainly resort to the single
filter analysis, which however ignores the relationship between filters. In
this paper, we propose a novel architecture decoupling method to interpret the
network from a perspective of investigating its calculation paths. More
specifically, we introduce a novel architecture controlling module in each
layer to encode the network architecture by a vector. By maximizing the mutual
information between the vectors and input images, the module is trained to
select specific filters to distill a unique calculation path for each input.
Furthermore, to improve the interpretability and compactness of the decoupled
network, the output of each layer is encoded to align the architecture encoding
vector with the constraint of sparsity regularization. Unlike conventional
pixel-level or filter-level network interpretation methods, we propose a
path-level analysis to explore the relationship between the combination of
filter and semantic concepts, which is more suitable to interpret the working
rationale of the decoupled network. Extensive experiments show that the
decoupled network achieves several applications, i.e., network interpretation,
network acceleration, and adversarial samples detection.