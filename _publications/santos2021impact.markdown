---
layout: publication
title: "On the Impact of Interpretability Methods in Active Image Augmentation Method"
authors: Flavio Santos, Cleber Zanchettin, Leonardo Matos, Paulo Novais
conference: Logic Journal of the IGPL, 2021, jzab006
year: 2021
additional_links: 
   - {name: "ArXiv", url: "http://dx.doi.org/10.1093/jigpal/jzab006"}
tags: []
---
Robustness is a significant constraint in machine learning models. The
performance of the algorithms must not deteriorate when training and testing
with slightly different data. Deep neural network models achieve awe-inspiring
results in a wide range of applications of computer vision. Still, in the
presence of noise or region occlusion, some models exhibit inaccurate
performance even with data handled in training. Besides, some experiments
suggest deep learning models sometimes use incorrect parts of the input
information to perform inference. Activate Image Augmentation (ADA) is an
augmentation method that uses interpretability methods to augment the training
data and improve its robustness to face the described problems. Although ADA
presented interesting results, its original version only used the Vanilla
Backpropagation interpretability to train the U-Net model. In this work, we
propose an extensive experimental analysis of the interpretability method's
impact on ADA. We use five interpretability methods: Vanilla Backpropagation,
Guided Backpropagation, GradCam, Guided GradCam, and InputXGradient. The
results show that all methods achieve similar performance at the ending of
training, but when combining ADA with GradCam, the U-Net model presented an
impressive fast convergence.