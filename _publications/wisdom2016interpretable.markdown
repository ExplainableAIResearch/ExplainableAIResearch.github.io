---
layout: publication
title: "Interpretable Recurrent Neural Networks Using Sequential Sparse Recovery"
authors: Scott Wisdom, Thomas Powers, James Pitton, Les Atlas
conference: 
year: 2016
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/1611.07252v1"}
tags: []
---
Recurrent neural networks (RNNs) are powerful and effective for processing
sequential data. However, RNNs are usually considered "black box" models whose
internal structure and learned parameters are not interpretable. In this paper,
we propose an interpretable RNN based on the sequential iterative
soft-thresholding algorithm (SISTA) for solving the sequential sparse recovery
problem, which models a sequence of correlated observations with a sequence of
sparse latent vectors. The architecture of the resulting SISTA-RNN is
implicitly defined by the computational structure of SISTA, which results in a
novel stacked RNN architecture. Furthermore, the weights of the SISTA-RNN are
perfectly interpretable as the parameters of a principled statistical model,
which in this case include a sparsifying dictionary, iterative step size, and
regularization parameters. In addition, on a particular sequential compressive
sensing task, the SISTA-RNN trains faster and achieves better performance than
conventional state-of-the-art black box RNNs, including long-short term memory
(LSTM) RNNs.