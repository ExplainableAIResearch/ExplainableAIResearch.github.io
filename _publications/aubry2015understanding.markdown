---
layout: publication
title: "Understanding deep features with computer-generated imagery"
authors: Mathieu Aubry, Bryan Russell
conference: 
year: 2015
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1506.01151v1"}
tags: []
---
We introduce an approach for analyzing the variation of features generated by
convolutional neural networks (CNNs) with respect to scene factors that occur
in natural images. Such factors may include object style, 3D viewpoint, color,
and scene lighting configuration. Our approach analyzes CNN feature responses
corresponding to different scene factors by controlling for them via rendering
using a large database of 3D CAD models. The rendered images are presented to a
trained CNN and responses for different layers are studied with respect to the
input scene factors. We perform a decomposition of the responses based on
knowledge of the input scene factors and analyze the resulting components. In
particular, we quantify their relative importance in the CNN responses and
visualize them using principal component analysis. We show qualitative and
quantitative results of our study on three CNNs trained on large image
datasets: AlexNet, Places, and Oxford VGG. We observe important differences
across the networks and CNN layers for different scene factors and object
categories. Finally, we demonstrate that our analysis based on
computer-generated imagery translates to the network representation of natural
images.