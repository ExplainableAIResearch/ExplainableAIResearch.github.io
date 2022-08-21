---
layout: publication
title: "Efficient Decompositional Rule Extraction for Deep Neural Networks"
authors: Mateo Espinosa Zarlenga, Zohreh Shams, Mateja Jamnik
conference: 
year: 2021
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2111.12628v1"}
tags: []
---
In recent years, there has been significant work on increasing both
interpretability and debuggability of a Deep Neural Network (DNN) by extracting
a rule-based model that approximates its decision boundary. Nevertheless,
current DNN rule extraction methods that consider a DNN's latent space when
extracting rules, known as decompositional algorithms, are either restricted to
single-layer DNNs or intractable as the size of the DNN or data grows. In this
paper, we address these limitations by introducing ECLAIRE, a novel
polynomial-time rule extraction algorithm capable of scaling to both large DNN
architectures and large training datasets. We evaluate ECLAIRE on a wide
variety of tasks, ranging from breast cancer prognosis to particle detection,
and show that it consistently extracts more accurate and comprehensible rule
sets than the current state-of-the-art methods while using orders of magnitude
less computational resources. We make all of our methods available, including a
rule set visualisation interface, through the open-source REMIX library
(https://github.com/mateoespinosa/remix).