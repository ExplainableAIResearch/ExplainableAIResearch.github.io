---
layout: publication
title: "Network Dissection: Quantifying Interpretability of Deep Visual Representations"
authors: David Bau, Bolei Zhou, Aditya Khosla, Aude Oliva, Antonio Torralba
conference: 
year: 2017
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1704.05796v1"}
tags: []
---
We propose a general framework called Network Dissection for quantifying the
interpretability of latent representations of CNNs by evaluating the alignment
between individual hidden units and a set of semantic concepts. Given any CNN
model, the proposed method draws on a broad data set of visual concepts to
score the semantics of hidden units at each intermediate convolutional layer.
The units with semantics are given labels across a range of objects, parts,
scenes, textures, materials, and colors. We use the proposed method to test the
hypothesis that interpretability of units is equivalent to random linear
combinations of units, then we apply our method to compare the latent
representations of various networks when trained to solve different supervised
and self-supervised training tasks. We further analyze the effect of training
iterations, compare networks trained with different initializations, examine
the impact of network depth and width, and measure the effect of dropout and
batch normalization on the interpretability of deep visual representations. We
demonstrate that the proposed method can shed light on characteristics of CNN
models and training methods that go beyond measurements of their discriminative
power.