---
layout: publication
title: "Gray-box Adversarial Training"
authors: Vivek B. S., Konda Reddy Mopuri, R. Venkatesh Babu
conference: 
year: 2018
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1808.01753v1"}
tags: []
---
Adversarial samples are perturbed inputs crafted to mislead the machine
learning systems. A training mechanism, called adversarial training, which
presents adversarial samples along with clean samples has been introduced to
learn robust models. In order to scale adversarial training for large datasets,
these perturbations can only be crafted using fast and simple methods (e.g.,
gradient ascent). However, it is shown that adversarial training converges to a
degenerate minimum, where the model appears to be robust by generating weaker
adversaries. As a result, the models are vulnerable to simple black-box
attacks. In this paper we, (i) demonstrate the shortcomings of existing
evaluation policy, (ii) introduce novel variants of white-box and black-box
attacks, dubbed gray-box adversarial attacks" based on which we propose novel
evaluation method to assess the robustness of the learned models, and (iii)
propose a novel variant of adversarial training, named Graybox Adversarial
Training" that uses intermediate versions of the models to seed the
adversaries. Experimental evaluation demonstrates that the models trained using
our method exhibit better robustness compared to both undefended and
adversarially trained model