---
layout: publication
title: "Towards Interpretable Deep Neural Networks by Leveraging Adversarial Examples"
authors: Yinpeng Dong, Fan Bao, Hang Su, Jun Zhu
conference: 
year: 2019
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/1901.09035v1"}
tags: []
---
Sometimes it is not enough for a DNN to produce an outcome. For example, in
applications such as healthcare, users need to understand the rationale of the
decisions. Therefore, it is imperative to develop algorithms to learn models
with good interpretability (Doshi-Velez 2017). An important factor that leads
to the lack of interpretability of DNNs is the ambiguity of neurons, where a
neuron may fire for various unrelated concepts. This work aims to increase the
interpretability of DNNs on the whole image space by reducing the ambiguity of
neurons. In this paper, we make the following contributions:
  1) We propose a metric to evaluate the consistency level of neurons in a
network quantitatively.
  2) We find that the learned features of neurons are ambiguous by leveraging
adversarial examples.
  3) We propose to improve the consistency of neurons on adversarial example
subset by an adversarial training algorithm with a consistent loss.