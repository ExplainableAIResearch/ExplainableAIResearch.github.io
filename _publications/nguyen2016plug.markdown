---
layout: publication
title: "Plug & Play Generative Networks: Conditional Iterative Generation of Images in Latent Space"
authors: Anh Nguyen, Jeff Clune, Yoshua Bengio, Alexey Dosovitskiy, Jason Yosinski
conference: 
year: 2016
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1612.00005v2"}
tags: []
---
Generating high-resolution, photo-realistic images has been a long-standing
goal in machine learning. Recently, Nguyen et al. (2016) showed one interesting
way to synthesize novel images by performing gradient ascent in the latent
space of a generator network to maximize the activations of one or multiple
neurons in a separate classifier network. In this paper we extend this method
by introducing an additional prior on the latent code, improving both sample
quality and sample diversity, leading to a state-of-the-art generative model
that produces high quality images at higher resolutions (227x227) than previous
generative models, and does so for all 1000 ImageNet categories. In addition,
we provide a unified probabilistic interpretation of related activation
maximization methods and call the general class of models "Plug and Play
Generative Networks". PPGNs are composed of 1) a generator network G that is
capable of drawing a wide range of image types and 2) a replaceable "condition"
network C that tells the generator what to draw. We demonstrate the generation
of images conditioned on a class (when C is an ImageNet or MIT Places
classification network) and also conditioned on a caption (when C is an image
captioning network). Our method also improves the state of the art of
Multifaceted Feature Visualization, which generates the set of synthetic inputs
that activate a neuron in order to better understand how deep neural networks
operate. Finally, we show that our model performs reasonably well at the task
of image inpainting. While image models are used in this paper, the approach is
modality-agnostic and can be applied to many types of data.