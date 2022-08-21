---
layout: publication
title: "Evaluating Explanations: How much do explanations from the teacher aid students?"
authors: Danish Pruthi, Rachit Bansal, Bhuwan Dhingra, Livio Baldini Soares, Michael Collins, Zachary C. Lipton, Graham Neubig, William W. Cohen
conference: 
year: 2020
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2012.00893v2"}
tags: []
---
While many methods purport to explain predictions by highlighting salient
features, what aims these explanations serve and how they ought to be evaluated
often go unstated. In this work, we introduce a framework to quantify the value
of explanations via the accuracy gains that they confer on a student model
trained to simulate a teacher model. Crucially, the explanations are available
to the student during training, but are not available at test time. Compared to
prior proposals, our approach is less easily gamed, enabling principled,
automatic, model-agnostic evaluation of attributions. Using our framework, we
compare numerous attribution methods for text classification and question
answering, and observe quantitative differences that are consistent (to a
moderate to high degree) across different student model architectures and
learning strategies.