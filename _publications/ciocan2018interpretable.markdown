---
layout: publication
title: "Interpretable Optimal Stopping"
authors: Dragos Florin Ciocan, Velibor V. Mišić
conference: 
year: 2018
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1812.07211v2"}
tags: []
---
Optimal stopping is the problem of deciding when to stop a stochastic system
to obtain the greatest reward, arising in numerous application areas such as
finance, healthcare and marketing. State-of-the-art methods for
high-dimensional optimal stopping involve approximating the value function or
the continuation value, and then using that approximation within a greedy
policy. Although such policies can perform very well, they are generally not
guaranteed to be interpretable; that is, a decision maker may not be able to
easily see the link between the current system state and the policy's action.
In this paper, we propose a new approach to optimal stopping, wherein the
policy is represented as a binary tree, in the spirit of naturally
interpretable tree models commonly used in machine learning. We show that the
class of tree policies is rich enough to approximate the optimal policy. We
formulate the problem of learning such policies from observed trajectories of
the stochastic system as a sample average approximation (SAA) problem. We prove
that the SAA problem converges under mild conditions as the sample size
increases, but that computationally even immediate simplifications of the SAA
problem are theoretically intractable. We thus propose a tractable heuristic
for approximately solving the SAA problem, by greedily constructing the tree
from the top down. We demonstrate the value of our approach by applying it to
the canonical problem of option pricing, using both synthetic instances and
instances using real S&P-500 data. Our method obtains policies that (1)
outperform state-of-the-art non-interpretable methods, based on
simulation-regression and martingale duality, and (2) possess a remarkably
simple and intuitive structure.