---
layout: publication
title: "Interpreting Language Models Through Knowledge Graph Extraction"
authors: Vinitra Swamy, Angelika Romanou, Martin Jaggi
conference: 
year: 2021
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2111.08546v1"}
tags: []
---
Transformer-based language models trained on large text corpora have enjoyed
immense popularity in the natural language processing community and are
commonly used as a starting point for downstream tasks. While these models are
undeniably useful, it is a challenge to quantify their performance beyond
traditional accuracy metrics. In this paper, we compare BERT-based language
models through snapshots of acquired knowledge at sequential stages of the
training process. Structured relationships from training corpora may be
uncovered through querying a masked language model with probing tasks. We
present a methodology to unveil a knowledge acquisition timeline by generating
knowledge graph extracts from cloze "fill-in-the-blank" statements at various
stages of RoBERTa's early training. We extend this analysis to a comparison of
pretrained variations of BERT models (DistilBERT, BERT-base, RoBERTa). This
work proposes a quantitative framework to compare language models through
knowledge graph extraction (GED, Graph2Vec) and showcases a part-of-speech
analysis (POSOR) to identify the linguistic strengths of each model variant.
Using these metrics, machine learning practitioners can compare models,
diagnose their models' behavioral strengths and weaknesses, and identify new
targeted datasets to improve model performance.