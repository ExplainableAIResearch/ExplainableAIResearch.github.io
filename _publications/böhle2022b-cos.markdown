---
layout: publication
title: "B-cos Networks: Alignment is All We Need for Interpretability"
authors: Moritz Böhle, Mario Fritz, Bernt Schiele
conference: 
year: 2022
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2205.10268v1"}
tags: []
---
We present a new direction for increasing the interpretability of deep neural
networks (DNNs) by promoting weight-input alignment during training. For this,
we propose to replace the linear transforms in DNNs by our B-cos transform. As
we show, a sequence (network) of such transforms induces a single linear
transform that faithfully summarises the full model computations. Moreover, the
B-cos transform introduces alignment pressure on the weights during
optimisation. As a result, those induced linear transforms become highly
interpretable and align with task-relevant features. Importantly, the B-cos
transform is designed to be compatible with existing architectures and we show
that it can easily be integrated into common models such as VGGs, ResNets,
InceptionNets, and DenseNets, whilst maintaining similar performance on
ImageNet. The resulting explanations are of high visual quality and perform
well under quantitative metrics for interpretability. Code available at
https://www.github.com/moboehle/B-cos.