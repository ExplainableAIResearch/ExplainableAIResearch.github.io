---
layout: publication
title: "Explaining Recurrent Neural Network Predictions in Sentiment Analysis"
authors: Leila Arras, Grégoire Montavon, Klaus-Robert Müller, Wojciech Samek
conference: 
year: 2017
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/1706.07206v2"}
tags: []
---
Recently, a technique called Layer-wise Relevance Propagation (LRP) was shown
to deliver insightful explanations in the form of input space relevances for
understanding feed-forward neural network classification decisions. In the
present work, we extend the usage of LRP to recurrent neural networks. We
propose a specific propagation rule applicable to multiplicative connections as
they arise in recurrent network architectures such as LSTMs and GRUs. We apply
our technique to a word-based bi-directional LSTM model on a five-class
sentiment prediction task, and evaluate the resulting LRP relevances both
qualitatively and quantitatively, obtaining better results than a
gradient-based related method which was used in previous work.