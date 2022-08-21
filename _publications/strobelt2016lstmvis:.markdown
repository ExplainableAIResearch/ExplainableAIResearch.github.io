---
layout: publication
title: "LSTMVis: A Tool for Visual Analysis of Hidden State Dynamics in Recurrent Neural Networks"
authors: Hendrik Strobelt, Sebastian Gehrmann, Hanspeter Pfister, Alexander M. Rush
conference: 
year: 2016
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/1606.07461v2"}
tags: []
---
Recurrent neural networks, and in particular long short-term memory (LSTM)
networks, are a remarkably effective tool for sequence modeling that learn a
dense black-box hidden representation of their sequential input. Researchers
interested in better understanding these models have studied the changes in
hidden state representations over time and noticed some interpretable patterns
but also significant noise. In this work, we present LSTMVIS, a visual analysis
tool for recurrent neural networks with a focus on understanding these hidden
state dynamics. The tool allows users to select a hypothesis input range to
focus on local state changes, to match these states changes to similar patterns
in a large data set, and to align these results with structural annotations
from their domain. We show several use cases of the tool for analyzing specific
hidden state properties on dataset containing nesting, phrase structure, and
chord progressions, and demonstrate how the tool can be used to isolate
patterns for further statistical analysis. We characterize the domain, the
different stakeholders, and their goals and tasks.