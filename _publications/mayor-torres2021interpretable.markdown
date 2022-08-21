---
layout: publication
title: "Interpretable SincNet-based Deep Learning for Emotion Recognition from EEG brain activity"
authors: Juan Manuel Mayor-Torres, Mirco Ravanelli, Sara E. Medina-DeVilliers, Matthew D. Lerner, Giuseppe Riccardi
conference: 
year: 2021
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2107.10790v1"}
tags: []
---
Machine learning methods, such as deep learning, show promising results in
the medical domain. However, the lack of interpretability of these algorithms
may hinder their applicability to medical decision support systems. This paper
studies an interpretable deep learning technique, called SincNet. SincNet is a
convolutional neural network that efficiently learns customized band-pass
filters through trainable sinc-functions. In this study, we use SincNet to
analyze the neural activity of individuals with Autism Spectrum Disorder (ASD),
who experience characteristic differences in neural oscillatory activity. In
particular, we propose a novel SincNet-based neural network for detecting
emotions in ASD patients using EEG signals. The learned filters can be easily
inspected to detect which part of the EEG spectrum is used for predicting
emotions. We found that our system automatically learns the high-$\alpha$ (9-13
Hz) and $\beta$ (13-30 Hz) band suppression often present in individuals with
ASD. This result is consistent with recent neuroscience studies on emotion
recognition, which found an association between these band suppressions and the
behavioral deficits observed in individuals with ASD. The improved
interpretability of SincNet is achieved without sacrificing performance in
emotion recognition.