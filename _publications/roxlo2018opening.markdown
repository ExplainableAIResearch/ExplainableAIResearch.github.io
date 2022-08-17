---
layout: publication
title: "Opening the black box of neural nets: case studies in stop/top discrimination"
authors: Thomas Roxlo, Matthew Reece
conference: 
year: 2018
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1804.09278v1"}
tags: []
---
We introduce techniques for exploring the functionality of a neural network
and extracting simple, human-readable approximations to its performance. By
performing gradient ascent on the input space of the network, we are able to
produce large populations of artificial events which strongly excite a given
classifier. By studying the populations of these events, we then directly
produce what are essentially contour maps of the network's classification
function. Combined with a suite of tools for identifying the input dimensions
deemed most important by the network, we can utilize these maps to efficiently
interpret the dominant criteria by which the network makes its classification.
  As a test case, we study networks trained to discriminate supersymmetric stop
production in the dilepton channel from Standard Model backgrounds. In the case
of a heavy stop decaying to a light neutralino, we find individual neurons with
large mutual information with $m_{T2}^{\ell\ell}$, a human-designed variable
for optimizing the analysis. The network selects events with significant
missing $p_T$ oriented azimuthally away from both leptons, efficiently
rejecting $t\overline{t}$ background. In the case of a light stop with
three-body decays to $Wb{\widetilde \chi}$ and little phase space, we find
neurons that smoothly interpolate between a similar top-rejection strategy and
an ISR-tagging strategy allowing for more missing momentum. We also find that a
neural network trained on a stealth stop parameter point learns novel angular
correlations.