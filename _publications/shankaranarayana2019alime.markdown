---
layout: publication
title: "ALIME: Autoencoder Based Approach for Local Interpretability"
authors: Sharath M. Shankaranarayana, Davor Runje
conference: 
year: 2019
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1909.02437v1"}
tags: []
---
Machine learning and especially deep learning have garneredtremendous
popularity in recent years due to their increased performanceover other
methods. The availability of large amount of data has aidedin the progress of
deep learning. Nevertheless, deep learning models areopaque and often seen as
black boxes. Thus, there is an inherent need tomake the models interpretable,
especially so in the medical domain. Inthis work, we propose a locally
interpretable method, which is inspiredby one of the recent tools that has
gained a lot of interest, called localinterpretable model-agnostic explanations
(LIME). LIME generates singleinstance level explanation by artificially
generating a dataset aroundthe instance (by randomly sampling and using
perturbations) and thentraining a local linear interpretable model. One of the
major issues inLIME is the instability in the generated explanation, which is
caused dueto the randomly generated dataset. Another issue in these kind of
localinterpretable models is the local fidelity. We propose novel
modificationsto LIME by employing an autoencoder, which serves as a better
weightingfunction for the local model. We perform extensive comparisons
withdifferent datasets and show that our proposed method results in
bothimproved stability, as well as local fidelity.