---
layout: publication
title: "Sanity Checks for Saliency Maps"
authors: Julius Adebayo, Justin Gilmer, Michael Muelly, Ian Goodfellow, Moritz Hardt, Been Kim
conference: 
year: 2018
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1810.03292v3"}
tags: []
---
Saliency methods have emerged as a popular tool to highlight features in an
input deemed relevant for the prediction of a learned model. Several saliency
methods have been proposed, often guided by visual appeal on image data. In
this work, we propose an actionable methodology to evaluate what kinds of
explanations a given method can and cannot provide. We find that reliance,
solely, on visual assessment can be misleading. Through extensive experiments
we show that some existing saliency methods are independent both of the model
and of the data generating process. Consequently, methods that fail the
proposed tests are inadequate for tasks that are sensitive to either data or
model, such as, finding outliers in the data, explaining the relationship
between inputs and outputs that the model learned, and debugging the model. We
interpret our findings through an analogy with edge detection in images, a
technique that requires neither training data nor model. Theory in the case of
a linear model and a single-layer convolutional neural network supports our
experimental findings.