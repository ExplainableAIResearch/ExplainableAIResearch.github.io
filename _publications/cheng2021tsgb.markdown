---
layout: publication
title: "TSGB: Target-Selective Gradient Backprop for Probing CNN Visual Saliency"
authors: Lin Cheng, Pengfei Fang, Yanjie Liang, Liao Zhang, Chunhua Shen, Hanzi Wang
conference: 
year: 2021
additional_links: 
   - {name: "ArXiv", url: "http://dx.doi.org/10.1109/TIP.2022.3157149"}
tags: []
---
The explanation for deep neural networks has drawn extensive attention in the
deep learning community over the past few years. In this work, we study the
visual saliency, a.k.a. visual explanation, to interpret convolutional neural
networks. Compared to iteration based saliency methods, single backward pass
based saliency methods benefit from faster speed, and they are widely used in
downstream visual tasks. Thus, we focus on single backward pass based methods.
However, existing methods in this category struggle to uccessfully produce
fine-grained saliency maps concentrating on specific target classes. That said,
producing faithful saliency maps satisfying both target-selectiveness and
fine-grainedness using a single backward pass is a challenging problem in the
field. To mitigate this problem, we revisit the gradient flow inside the
network, and find that the entangled semantics and original weights may disturb
the propagation of target-relevant saliency. Inspired by those observations, we
propose a novel visual saliency method, termed Target-Selective Gradient
Backprop (TSGB), which leverages rectification operations to effectively
emphasize target classes and further efficiently propagate the saliency to the
image space, thereby generating target-selective and fine-grained saliency
maps. The proposed TSGB consists of two components, namely, TSGB-Conv and
TSGB-FC, which rectify the gradients for convolutional layers and
fully-connected layers, respectively. Extensive qualitative and quantitative
experiments on the ImageNet and Pascal VOC datasets show that the proposed
method achieves more accurate and reliable results than the other competitive
methods. Code is available at https://github.com/123fxdx/CNNvisualizationTSGB.