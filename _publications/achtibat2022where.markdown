---
layout: publication
title: "From \"Where\" to \"What\": Towards Human-Understandable Explanations through Concept Relevance Propagation"
authors: Reduan Achtibat, Maximilian Dreyer, Ilona Eisenbraun, Sebastian Bosse, Thomas Wiegand, Wojciech Samek, Sebastian Lapuschkin
conference: 
year: 2022
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2206.03208v1"}
tags: []
---
The emerging field of eXplainable Artificial Intelligence (XAI) aims to bring
transparency to today's powerful but opaque deep learning models. While local
XAI methods explain individual predictions in form of attribution maps, thereby
identifying where important features occur (but not providing information about
what they represent), global explanation techniques visualize what concepts a
model has generally learned to encode. Both types of methods thus only provide
partial insights and leave the burden of interpreting the model's reasoning to
the user. Only few contemporary techniques aim at combining the principles
behind both local and global XAI for obtaining more informative explanations.
Those methods, however, are often limited to specific model architectures or
impose additional requirements on training regimes or data and label
availability, which renders the post-hoc application to arbitrarily pre-trained
models practically impossible. In this work we introduce the Concept Relevance
Propagation (CRP) approach, which combines the local and global perspectives of
XAI and thus allows answering both the "where" and "what" questions for
individual predictions, without additional constraints imposed. We further
introduce the principle of Relevance Maximization for finding representative
examples of encoded concepts based on their usefulness to the model. We thereby
lift the dependency on the common practice of Activation Maximization and its
limitations. We demonstrate the capabilities of our methods in various
settings, showcasing that Concept Relevance Propagation and Relevance
Maximization lead to more human interpretable explanations and provide deep
insights into the model's representations and reasoning through concept
atlases, concept composition analyses, and quantitative investigations of
concept subspaces and their role in fine-grained decision making.