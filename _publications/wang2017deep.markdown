---
layout: publication
title: "Deep Visual Attention Prediction"
authors: Wenguan Wang, Jianbing Shen
conference: IEEE Transactions on Image Processing, Vol. 27, No. 5, pp
  2368-2378, 2018
year: 2017
additional_links: 
   - {name: "ArXiv", url: "http://dx.doi.org/10.1109/TIP.2017.2787612"}
tags: []
---
In this work, we aim to predict human eye fixation with view-free scenes
based on an end-to-end deep learning architecture. Although Convolutional
Neural Networks (CNNs) have made substantial improvement on human attention
prediction, it is still needed to improve CNN based attention models by
efficiently leveraging multi-scale features. Our visual attention network is
proposed to capture hierarchical saliency information from deep, coarse layers
with global saliency information to shallow, fine layers with local saliency
response. Our model is based on a skip-layer network structure, which predicts
human attention from multiple convolutional layers with various reception
fields. Final saliency prediction is achieved via the cooperation of those
global and local predictions. Our model is learned in a deep supervision
manner, where supervision is directly fed into multi-level layers, instead of
previous approaches of providing supervision only at the output layer and
propagating this supervision back to earlier layers. Our model thus
incorporates multi-level saliency predictions within a single network, which
significantly decreases the redundancy of previous approaches of learning
multiple network streams with different input scales. Extensive experimental
analysis on various challenging benchmark datasets demonstrate our method
yields state-of-the-art performance with competitive inference time.