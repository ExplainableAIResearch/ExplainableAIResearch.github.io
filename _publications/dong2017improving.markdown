---
layout: publication
title: "Improving Interpretability of Deep Neural Networks with Semantic Information"
authors: Yinpeng Dong, Hang Su, Jun Zhu, Bo Zhang
conference: 
year: 2017
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/1703.04096v2"}
tags: []
---
Interpretability of deep neural networks (DNNs) is essential since it enables
users to understand the overall strengths and weaknesses of the models, conveys
an understanding of how the models will behave in the future, and how to
diagnose and correct potential problems. However, it is challenging to reason
about what a DNN actually does due to its opaque or black-box nature. To
address this issue, we propose a novel technique to improve the
interpretability of DNNs by leveraging the rich semantic information embedded
in human descriptions. By concentrating on the video captioning task, we first
extract a set of semantically meaningful topics from the human descriptions
that cover a wide range of visual concepts, and integrate them into the model
with an interpretive loss. We then propose a prediction difference maximization
algorithm to interpret the learned features of each neuron. Experimental
results demonstrate its effectiveness in video captioning using the
interpretable features, which can also be transferred to video action
recognition. By clearly understanding the learned features, users can easily
revise false predictions via a human-in-the-loop procedure.