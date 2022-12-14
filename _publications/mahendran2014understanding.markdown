---
layout: publication
title: "Understanding Deep Image Representations by Inverting Them"
authors: Aravindh Mahendran, Andrea Vedaldi
conference: 
year: 2014
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1412.0035v1"}
tags: []
---
Image representations, from SIFT and Bag of Visual Words to Convolutional
Neural Networks (CNNs), are a crucial component of almost any image
understanding system. Nevertheless, our understanding of them remains limited.
In this paper we conduct a direct analysis of the visual information contained
in representations by asking the following question: given an encoding of an
image, to which extent is it possible to reconstruct the image itself? To
answer this question we contribute a general framework to invert
representations. We show that this method can invert representations such as
HOG and SIFT more accurately than recent alternatives while being applicable to
CNNs too. We then use this technique to study the inverse of recent
state-of-the-art CNN image representations for the first time. Among our
findings, we show that several layers in CNNs retain photographically accurate
information about the image, with different degrees of geometric and
photometric invariance.