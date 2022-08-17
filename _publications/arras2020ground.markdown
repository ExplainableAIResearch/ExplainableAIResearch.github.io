---
layout: publication
title: "Ground Truth Evaluation of Neural Network Explanations with CLEVR-XAI"
authors: Leila Arras, Ahmed Osman, Wojciech Samek
conference: 
year: 2020
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2003.07258v2"}
tags: []
---
The rise of deep learning in today's applications entailed an increasing need
in explaining the model's decisions beyond prediction performances in order to
foster trust and accountability. Recently, the field of explainable AI (XAI)
has developed methods that provide such explanations for already trained neural
networks. In computer vision tasks such explanations, termed heatmaps,
visualize the contributions of individual pixels to the prediction. So far XAI
methods along with their heatmaps were mainly validated qualitatively via
human-based assessment, or evaluated through auxiliary proxy tasks such as
pixel perturbation, weak object localization or randomization tests. Due to the
lack of an objective and commonly accepted quality measure for heatmaps, it was
debatable which XAI method performs best and whether explanations can be
trusted at all. In the present work, we tackle the problem by proposing a
ground truth based evaluation framework for XAI methods based on the CLEVR
visual question answering task. Our framework provides a (1) selective, (2)
controlled and (3) realistic testbed for the evaluation of neural network
explanations. We compare ten different explanation methods, resulting in new
insights about the quality and properties of XAI methods, sometimes
contradicting with conclusions from previous comparative studies. The CLEVR-XAI
dataset and the benchmarking code can be found at
https://github.com/ahmedmagdiosman/clevr-xai.