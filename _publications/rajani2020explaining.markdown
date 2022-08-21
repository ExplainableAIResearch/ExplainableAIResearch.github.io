---
layout: publication
title: "Explaining and Improving Model Behavior with k Nearest Neighbor Representations"
authors: Nazneen Fatema Rajani, Ben Krause, Wengpeng Yin, Tong Niu, Richard Socher, Caiming Xiong
conference: 
year: 2020
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2010.09030v1"}
tags: []
---
Interpretability techniques in NLP have mainly focused on understanding
individual predictions using attention visualization or gradient-based saliency
maps over tokens. We propose using k nearest neighbor (kNN) representations to
identify training examples responsible for a model's predictions and obtain a
corpus-level understanding of the model's behavior. Apart from
interpretability, we show that kNN representations are effective at uncovering
learned spurious associations, identifying mislabeled examples, and improving
the fine-tuned model's performance. We focus on Natural Language Inference
(NLI) as a case study and experiment with multiple datasets. Our method deploys
backoff to kNN for BERT and RoBERTa on examples with low model confidence
without any update to the model parameters. Our results indicate that the kNN
approach makes the finetuned model more robust to adversarial inputs.