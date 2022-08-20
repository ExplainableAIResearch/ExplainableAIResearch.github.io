---
layout: publication
title: "Evolutionary learning of interpretable decision trees"
authors: Leonardo Lucio Custode, Giovanni Iacca
conference: 
year: 2020
additional_links: 
	- {name: "ArXiv", url: "http://arxiv.org/abs/2012.07723v3"}
tags: []
---
Reinforcement learning techniques achieved human-level performance in several
tasks in the last decade. However, in recent years, the need for
interpretability emerged: we want to be able to understand how a system works
and the reasons behind its decisions. Not only we need interpretability to
assess the safety of the produced systems, we also need it to extract knowledge
about unknown problems. While some techniques that optimize decision trees for
reinforcement learning do exist, they usually employ greedy algorithms or they
do not exploit the rewards given by the environment. This means that these
techniques may easily get stuck in local optima. In this work, we propose a
novel approach to interpretable reinforcement learning that uses decision
trees. We present a two-level optimization scheme that combines the advantages
of evolutionary algorithms with the advantages of Q-learning. This way we
decompose the problem into two sub-problems: the problem of finding a
meaningful and useful decomposition of the state space, and the problem of
associating an action to each state. We test the proposed method on three
well-known reinforcement learning benchmarks, on which it results competitive
with respect to the state-of-the-art in both performance and interpretability.
Finally, we perform an ablation study that confirms that using the two-level
optimization scheme gives a boost in performance in non-trivial environments
with respect to a one-layer optimization technique.