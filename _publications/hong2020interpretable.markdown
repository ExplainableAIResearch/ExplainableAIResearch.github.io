---
layout: publication
title: "Interpretable Sequence Classification Via Prototype Trajectory"
authors: Dat Hong, Stephen S. Baek, Tong Wang
conference: 
year: 2020
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2007.01777v2"}
tags: []
---
We propose a novel interpretable deep neural network for text classification,
called ProtoryNet, based on a new concept of prototype trajectories. Motivated
by the prototype theory in modern linguistics, ProtoryNet makes a prediction by
finding the most similar prototype for each sentence in a text sequence and
feeding an RNN backbone with the proximity of each sentence to the
corresponding active prototype. The RNN backbone then captures the temporal
pattern of the prototypes, which we refer to as prototype trajectories.
Prototype trajectories enable intuitive and fine-grained interpretation of the
reasoning process of the RNN model, in resemblance to how humans analyze texts.
We also design a prototype pruning procedure to reduce the total number of
prototypes used by the model for better interpretability. Experiments on
multiple public data sets show that ProtoryNet is more accurate than the
baseline prototype-based deep neural net and reduces the performance gap
compared to state-of-the-art black-box models. In addition, after prototype
pruning, the resulting ProtoryNet models only need less than or around 20
prototypes for all datasets, which significantly benefits interpretability.
Furthermore, we report a survey result indicating that human users find
ProtoryNet more intuitive and easier to understand than other prototype-based
methods.