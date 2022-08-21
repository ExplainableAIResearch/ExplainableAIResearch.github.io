---
layout: publication
title: "Exploring Conditioning for Generative Music Systems with Human-Interpretable Controls"
authors: Nicholas Meade, Nicholas Barreyre, Scott C. Lowe, Sageev Oore
conference: International Conference on Computational Creativity, 2019
year: 2019
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/1907.04352v3"}
tags: []
---
Performance RNN is a machine-learning system designed primarily for the
generation of solo piano performances using an event-based (rather than audio)
representation. More specifically, Performance RNN is a long short-term memory
(LSTM) based recurrent neural network that models polyphonic music with
expressive timing and dynamics (Oore et al., 2018). The neural network uses a
simple language model based on the Musical Instrument Digital Interface (MIDI)
file format. Performance RNN is trained on the e-Piano Junior Competition
Dataset (International Piano e-Competition, 2018), a collection of solo piano
performances by expert pianists. As an artistic tool, one of the limitations of
the original model has been the lack of useable controls. The standard form of
Performance RNN can generate interesting pieces, but little control is provided
over what specifically is generated. This paper explores a set of
conditioning-based controls used to influence the generation process.