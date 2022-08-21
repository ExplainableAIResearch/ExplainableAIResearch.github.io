---
layout: publication
title: "Quantifying Attention Flow in Transformers"
authors: Samira Abnar, Willem Zuidema
conference: 
year: 2020
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2005.00928v2"}
tags: []
---
In the Transformer model, "self-attention" combines information from attended
embeddings into the representation of the focal embedding in the next layer.
Thus, across layers of the Transformer, information originating from different
tokens gets increasingly mixed. This makes attention weights unreliable as
explanations probes. In this paper, we consider the problem of quantifying this
flow of information through self-attention. We propose two methods for
approximating the attention to input tokens given attention weights, attention
rollout and attention flow, as post hoc methods when we use attention weights
as the relative relevance of the input tokens. We show that these methods give
complementary views on the flow of information, and compared to raw attention,
both yield higher correlations with importance scores of input tokens obtained
using an ablation method and input gradients.