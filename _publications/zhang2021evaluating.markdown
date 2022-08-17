---
layout: publication
title: "Evaluating Deep Graph Neural Networks"
authors: Wentao Zhang, Zeang Sheng, Yuezihan Jiang, Yikuan Xia, Jun Gao, Zhi Yang, Bin Cui
conference: 
year: 2021
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2108.00955v1"}
tags: []
---
Graph Neural Networks (GNNs) have already been widely applied in various
graph mining tasks. However, they suffer from the shallow architecture issue,
which is the key impediment that hinders the model performance improvement.
Although several relevant approaches have been proposed, none of the existing
studies provides an in-depth understanding of the root causes of performance
degradation in deep GNNs. In this paper, we conduct the first systematic
experimental evaluation to present the fundamental limitations of shallow
architectures. Based on the experimental results, we answer the following two
essential questions: (1) what actually leads to the compromised performance of
deep GNNs; (2) when we need and how to build deep GNNs. The answers to the
above questions provide empirical insights and guidelines for researchers to
design deep and well-performed GNNs. To show the effectiveness of our proposed
guidelines, we present Deep Graph Multi-Layer Perceptron (DGMLP), a powerful
approach (a paradigm in its own right) that helps guide deep GNN designs.
Experimental results demonstrate three advantages of DGMLP: 1) high accuracy --
it achieves state-of-the-art node classification performance on various
datasets; 2) high flexibility -- it can flexibly choose different propagation
and transformation depths according to graph size and sparsity; 3) high
scalability and efficiency -- it supports fast training on large-scale graphs.
Our code is available in https://github.com/zwt233/DGMLP.