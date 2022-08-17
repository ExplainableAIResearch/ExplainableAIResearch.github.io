---
layout: publication
title: "Deep Unsupervised Learning of Visual Similarities"
authors: Artsiom Sanakoyeu, Miguel A. Bautista, Björn Ommer
conference: Pattern Recognition Volume 78, June 2018, Pages 331-343
year: 2018
additional_links: 
   - {name: "ArXiv", url: "http://dx.doi.org/10.1016/j.patcog.2018.01.036"}
tags: []
---
Exemplar learning of visual similarities in an unsupervised manner is a
problem of paramount importance to Computer Vision. In this context, however,
the recent breakthrough in deep learning could not yet unfold its full
potential. With only a single positive sample, a great imbalance between one
positive and many negatives, and unreliable relationships between most samples,
training of Convolutional Neural networks is impaired. In this paper we use
weak estimates of local similarities and propose a single optimization problem
to extract batches of samples with mutually consistent relations. Conflicting
relations are distributed over different batches and similar samples are
grouped into compact groups. Learning visual similarities is then framed as a
sequence of categorization tasks. The CNN then consolidates transitivity
relations within and between groups and learns a single representation for all
samples without the need for labels. The proposed unsupervised approach has
shown competitive performance on detailed posture analysis and object
classification.