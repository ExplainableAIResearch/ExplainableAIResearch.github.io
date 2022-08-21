---
layout: publication
title: "Towards Interpretable ANNs: An Exact Transformation to Multi-Class Multivariate Decision Trees"
authors: Duy T. Nguyen, Kathryn E. Kasmarik, Hussein A. Abbass
conference: 
year: 2020
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2003.04675v4"}
tags: []
---
On the one hand, artificial neural networks (ANNs) are commonly labelled as
black-boxes, lacking interpretability; an issue that hinders human
understanding of ANNs' behaviors. A need exists to generate a meaningful
sequential logic of the ANN for interpreting a production process of a specific
output. On the other hand, decision trees exhibit better interpretability and
expressive power due to their representation language and the existence of
efficient algorithms to transform the trees into rules. However, growing a
decision tree based on the available data could produce larger than necessary
trees or trees that do not generalise well. In this paper, we introduce two
novel multivariate decision tree (MDT) algorithms for rule extraction from
ANNs: an Exact-Convertible Decision Tree (EC-DT) and an Extended C-Net
algorithm. They both transform a neural network with Rectified Linear Unit
activation functions into a representative tree, which can further be used to
extract multivariate rules for reasoning. While the EC-DT translates an ANN in
a layer-wise manner to represent exactly the decision boundaries implicitly
learned by the hidden layers of the network, the Extended C-Net combines the
decompositional approach from EC-DT with a C5 tree learning algorithm to form
decision rules. The results suggest that while EC-DT is superior in preserving
the structure and the fidelity of ANN, Extended C-Net generates the most
compact and highly effective trees from ANN. Both proposed MDT algorithms
generate rules including combinations of multiple attributes for precise
interpretations for decision-making.