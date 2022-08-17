---
layout: publication
title: "A Simple Saliency Method That Passes the Sanity Checks"
authors: Arushi Gupta, Sanjeev Arora
conference: 
year: 2019
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1905.12152v2"}
tags: []
---
There is great interest in "saliency methods" (also called "attribution
methods"), which give "explanations" for a deep net's decision, by assigning a
"score" to each feature/pixel in the input. Their design usually involves
credit-assignment via the gradient of the output with respect to input.
Recently Adebayo et al. [arXiv:1810.03292] questioned the validity of many of
these methods since they do not pass simple *sanity checks* which test whether
the scores shift/vanish when layers of the trained net are randomized, or when
the net is retrained using random labels for inputs.
  We propose a simple fix to existing saliency methods that helps them pass
sanity checks, which we call "competition for pixels". This involves computing
saliency maps for all possible labels in the classification task, and using a
simple competition among them to identify and remove less relevant pixels from
the map. The simplest variant of this is "Competitive Gradient $\odot$ Input
(CGI)": it is efficient, requires no additional training, and uses only the
input and gradient. Some theoretical justification is provided for it
(especially for ReLU networks) and its performance is empirically demonstrated.