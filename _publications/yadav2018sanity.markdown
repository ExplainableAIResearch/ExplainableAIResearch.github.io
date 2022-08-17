---
layout: publication
title: "Sanity Check: A Strong Alignment and Information Retrieval Baseline for Question Answering"
authors: Vikas Yadav, Rebecca Sharp, Mihai Surdeanu
conference: 
year: 2018
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1807.01836v1"}
tags: []
---
While increasingly complex approaches to question answering (QA) have been
proposed, the true gain of these systems, particularly with respect to their
expensive training requirements, can be inflated when they are not compared to
adequate baselines. Here we propose an unsupervised, simple, and fast alignment
and information retrieval baseline that incorporates two novel contributions: a
\textit{one-to-many alignment} between query and document terms and
\textit{negative alignment} as a proxy for discriminative information. Our
approach not only outperforms all conventional baselines as well as many
supervised recurrent neural networks, but also approaches the state of the art
for supervised systems on three QA datasets. With only three hyperparameters,
we achieve 47\% P@1 on an 8th grade Science QA dataset, 32.9\% P@1 on a Yahoo!
answers QA dataset and 64\% MAP on WikiQA. We also achieve 26.56\% and 58.36\%
on ARC challenge and easy dataset respectively. In addition to including the
additional ARC results in this version of the paper, for the ARC easy set only
we also experimented with one additional parameter -- number of justifications
retrieved.