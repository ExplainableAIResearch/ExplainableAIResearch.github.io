---
layout: publication
title: "Understanding intermediate layers using linear classifier probes"
authors: Guillaume Alain, Yoshua Bengio
conference: 
year: 2016
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/1610.01644v4"}
tags: []
---
Neural network models have a reputation for being black boxes. We propose to
monitor the features at every layer of a model and measure how suitable they
are for classification. We use linear classifiers, which we refer to as
"probes", trained entirely independently of the model itself.
  This helps us better understand the roles and dynamics of the intermediate
layers. We demonstrate how this can be used to develop a better intuition about
models and to diagnose potential problems.
  We apply this technique to the popular models Inception v3 and Resnet-50.
Among other things, we observe experimentally that the linear separability of
features increase monotonically along the depth of the model.