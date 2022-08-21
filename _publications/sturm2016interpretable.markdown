---
layout: publication
title: "Interpretable Deep Neural Networks for Single-Trial EEG Classification"
authors: Irene Sturm, Sebastian Bach, Wojciech Samek, Klaus-Robert Müller
conference: 
year: 2016
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/1604.08201v1"}
tags: []
---
Background: In cognitive neuroscience the potential of Deep Neural Networks
(DNNs) for solving complex classification tasks is yet to be fully exploited.
The most limiting factor is that DNNs as notorious 'black boxes' do not provide
insight into neurophysiological phenomena underlying a decision. Layer-wise
Relevance Propagation (LRP) has been introduced as a novel method to explain
individual network decisions. New Method: We propose the application of DNNs
with LRP for the first time for EEG data analysis. Through LRP the single-trial
DNN decisions are transformed into heatmaps indicating each data point's
relevance for the outcome of the decision. Results: DNN achieves classification
accuracies comparable to those of CSP-LDA. In subjects with low performance
subject-to-subject transfer of trained DNNs can improve the results. The
single-trial LRP heatmaps reveal neurophysiologically plausible patterns,
resembling CSP-derived scalp maps. Critically, while CSP patterns represent
class-wise aggregated information, LRP heatmaps pinpoint neural patterns to
single time points in single trials. Comparison with Existing Method(s): We
compare the classification performance of DNNs to that of linear CSP-LDA on two
data sets related to motor-imaginery BCI. Conclusion: We have demonstrated that
DNN is a powerful non-linear tool for EEG analysis. With LRP a new quality of
high-resolution assessment of neural activity can be reached. LRP is a
potential remedy for the lack of interpretability of DNNs that has limited
their utility in neuroscientific applications. The extreme specificity of the
LRP-derived heatmaps opens up new avenues for investigating neural activity
underlying complex perception or decision-related processes.