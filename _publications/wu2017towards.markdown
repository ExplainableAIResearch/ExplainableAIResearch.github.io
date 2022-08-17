---
layout: publication
title: "Towards Interpretable R-CNN by Unfolding Latent Structures"
authors: Tianfu Wu, Wei Sun, Xilai Li, Xi Song, Bo Li
conference: 
year: 2017
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1711.05226v2"}
tags: []
---
This paper first proposes a method of formulating model interpretability in
visual understanding tasks based on the idea of unfolding latent structures. It
then presents a case study in object detection using popular two-stage
region-based convolutional network (i.e., R-CNN) detection systems. We focus on
weakly-supervised extractive rationale generation, that is learning to unfold
latent discriminative part configurations of object instances automatically and
simultaneously in detection without using any supervision for part
configurations. We utilize a top-down hierarchical and compositional grammar
model embedded in a directed acyclic AND-OR Graph (AOG) to explore and unfold
the space of latent part configurations of regions of interest (RoIs). We
propose an AOGParsing operator to substitute the RoIPooling operator widely
used in R-CNN. In detection, a bounding box is interpreted by the best parse
tree derived from the AOG on-the-fly, which is treated as the qualitatively
extractive rationale generated for interpreting detection. We propose a
folding-unfolding method to train the AOG and convolutional networks
end-to-end. In experiments, we build on R-FCN and test our method on the PASCAL
VOC 2007 and 2012 datasets. We show that the method can unfold promising latent
structures without hurting the performance.