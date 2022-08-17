---
layout: publication
title: "Efficient Saliency Maps for Explainable AI"
authors: T. Nathan Mundhenk, Barry Y. Chen, Gerald Friedland
conference: 
year: 2019
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1911.11293v2"}
tags: []
---
We describe an explainable AI saliency map method for use with deep
convolutional neural networks (CNN) that is much more efficient than popular
fine-resolution gradient methods. It is also quantitatively similar or better
in accuracy. Our technique works by measuring information at the end of each
network scale which is then combined into a single saliency map. We describe
how saliency measures can be made more efficient by exploiting Saliency Map
Order Equivalence. We visualize individual scale/layer contributions by using a
Layer Ordered Visualization of Information. This provides an interesting
comparison of scale information contributions within the network not provided
by other saliency map methods. Using our method instead of Guided Backprop,
coarse-resolution class activation methods such as Grad-CAM and Grad-CAM++ seem
to yield demonstrably superior results without sacrificing speed. This will
make fine-resolution saliency methods feasible on resource limited platforms
such as robots, cell phones, low-cost industrial devices, astronomy and
satellite imagery.