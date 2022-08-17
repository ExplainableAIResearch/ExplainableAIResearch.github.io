---
layout: publication
title: "One pixel attack for fooling deep neural networks"
authors: Jiawei Su, Danilo Vasconcellos Vargas, Sakurai Kouichi
conference: IEEE Transactions on Evolutionary Computation
year: 2017
additional_links: 
   - {name: "ArXiv", url: "http://dx.doi.org/10.1109/TEVC.2019.2890858"}
tags: []
---
Recent research has revealed that the output of Deep Neural Networks (DNN)
can be easily altered by adding relatively small perturbations to the input
vector. In this paper, we analyze an attack in an extremely limited scenario
where only one pixel can be modified. For that we propose a novel method for
generating one-pixel adversarial perturbations based on differential evolution
(DE). It requires less adversarial information (a black-box attack) and can
fool more types of networks due to the inherent features of DE. The results
show that 67.97% of the natural images in Kaggle CIFAR-10 test dataset and
16.04% of the ImageNet (ILSVRC 2012) test images can be perturbed to at least
one target class by modifying just one pixel with 74.03% and 22.91% confidence
on average. We also show the same vulnerability on the original CIFAR-10
dataset. Thus, the proposed attack explores a different take on adversarial
machine learning in an extreme limited scenario, showing that current DNNs are
also vulnerable to such low dimension attacks. Besides, we also illustrate an
important application of DE (or broadly speaking, evolutionary computation) in
the domain of adversarial machine learning: creating tools that can effectively
generate low-cost adversarial attacks against neural networks for evaluating
robustness.