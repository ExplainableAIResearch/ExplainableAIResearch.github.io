---
layout: publication
title: "Invertible Attention"
authors: Jiajun Zha, Yiran Zhong, Jing Zhang, Richard Hartley, Liang Zheng
conference: 
year: 2021
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2106.09003v2"}
tags: []
---
Attention has been proved to be an efficient mechanism to capture long-range
dependencies. However, so far it has not been deployed in invertible networks.
This is due to the fact that in order to make a network invertible, every
component within the network needs to be a bijective transformation, but a
normal attention block is not. In this paper, we propose invertible attention
that can be plugged into existing invertible models. We mathematically and
experimentally prove that the invertibility of an attention model can be
achieved by carefully constraining its Lipschitz constant. We validate the
invertibility of our invertible attention on image reconstruction task with 3
popular datasets: CIFAR-10, SVHN, and CelebA. We also show that our invertible
attention achieves similar performance in comparison with normal non-invertible
attention on dense prediction tasks. The code is available at
https://github.com/Schwartz-Zha/InvertibleAttention