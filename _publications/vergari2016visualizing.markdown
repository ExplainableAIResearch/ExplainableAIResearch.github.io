---
layout: publication
title: "Visualizing and Understanding Sum-Product Networks"
authors: Antonio Vergari, Nicola Di Mauro, Floriana Esposito
conference: 
year: 2016
additional_links: 
   - {name: "ArXiv", url: "http://dx.doi.org/10.1007/s10994-018-5760-y"}
tags: []
---
Sum-Product Networks (SPNs) are recently introduced deep tractable
probabilistic models by which several kinds of inference queries can be
answered exactly and in a tractable time. Up to now, they have been largely
used as black box density estimators, assessed only by comparing their
likelihood scores only. In this paper we explore and exploit the inner
representations learned by SPNs. We do this with a threefold aim: first we want
to get a better understanding of the inner workings of SPNs; secondly, we seek
additional ways to evaluate one SPN model and compare it against other
probabilistic models, providing diagnostic tools to practitioners; lastly, we
want to empirically evaluate how good and meaningful the extracted
representations are, as in a classic Representation Learning framework. In
order to do so we revise their interpretation as deep neural networks and we
propose to exploit several visualization techniques on their node activations
and network outputs under different types of inference queries. To investigate
these models as feature extractors, we plug some SPNs, learned in a greedy
unsupervised fashion on image datasets, in supervised classification learning
tasks. We extract several embedding types from node activations by filtering
nodes by their type, by their associated feature abstraction level and by their
scope. In a thorough empirical comparison we prove them to be competitive
against those generated from popular feature extractors as Restricted Boltzmann
Machines. Finally, we investigate embeddings generated from random
probabilistic marginal queries as means to compare other tractable
probabilistic models on a common ground, extending our experiments to Mixtures
of Trees.