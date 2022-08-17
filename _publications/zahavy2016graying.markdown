---
layout: publication
title: "Graying the black box: Understanding DQNs"
authors: Tom Zahavy, Nir Ben Zrihem, Shie Mannor
conference: 
year: 2016
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1602.02658v4"}
tags: []
---
In recent years there is a growing interest in using deep representations for
reinforcement learning. In this paper, we present a methodology and tools to
analyze Deep Q-networks (DQNs) in a non-blind matter. Moreover, we propose a
new model, the Semi Aggregated Markov Decision Process (SAMDP), and an
algorithm that learns it automatically. The SAMDP model allows us to identify
spatio-temporal abstractions directly from features and may be used as a
sub-goal detector in future work. Using our tools we reveal that the features
learned by DQNs aggregate the state space in a hierarchical fashion, explaining
its success. Moreover, we are able to understand and describe the policies
learned by DQNs for three different Atari2600 games and suggest ways to
interpret, debug and optimize deep neural networks in reinforcement learning.