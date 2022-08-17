---
layout: publication
title: "A First Look: Towards Explainable TextVQA Models via Visual and Textual Explanations"
authors: Varun Nagaraj Rao, Xingjian Zhen, Karen Hovsepian, Mingwei Shen
conference: 
year: 2021
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2105.02626v1"}
tags: []
---
Explainable deep learning models are advantageous in many situations. Prior
work mostly provide unimodal explanations through post-hoc approaches not part
of the original system design. Explanation mechanisms also ignore useful
textual information present in images. In this paper, we propose MTXNet, an
end-to-end trainable multimodal architecture to generate multimodal
explanations, which focuses on the text in the image. We curate a novel dataset
TextVQA-X, containing ground truth visual and multi-reference textual
explanations that can be leveraged during both training and evaluation. We then
quantitatively show that training with multimodal explanations complements
model performance and surpasses unimodal baselines by up to 7% in CIDEr scores
and 2% in IoU. More importantly, we demonstrate that the multimodal
explanations are consistent with human interpretations, help justify the
models' decision, and provide useful insights to help diagnose an incorrect
prediction. Finally, we describe a real-world e-commerce application for using
the generated multimodal explanations.