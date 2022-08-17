---
layout: publication
title: "Learning Deep Features for Discriminative Localization"
authors: Bolei Zhou, Aditya Khosla, Agata Lapedriza, Aude Oliva, Antonio Torralba
conference: 
year: 2015
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1512.04150v1"}
tags: []
---
In this work, we revisit the global average pooling layer proposed in [13],
and shed light on how it explicitly enables the convolutional neural network to
have remarkable localization ability despite being trained on image-level
labels. While this technique was previously proposed as a means for
regularizing training, we find that it actually builds a generic localizable
deep representation that can be applied to a variety of tasks. Despite the
apparent simplicity of global average pooling, we are able to achieve 37.1%
top-5 error for object localization on ILSVRC 2014, which is remarkably close
to the 34.2% top-5 error achieved by a fully supervised CNN approach. We
demonstrate that our network is able to localize the discriminative image
regions on a variety of tasks despite not being trained for them