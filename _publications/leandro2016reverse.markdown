---
layout: publication
title: "Reverse Engineering and Symbolic Knowledge Extraction on Łukasiewicz Fuzzy Logics using Linear Neural Networks"
authors: Carlos Leandro
conference: 
year: 2016
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/1604.02774v1"}
tags: []
---
This work describes a methodology to combine logic-based systems and
connectionist systems. Our approach uses finite truth valued {\L}ukasiewicz
logic, where we take advantage of fact what in this type of logics every
connective can be define by a neuron in an artificial network having by
activation function the identity truncated to zero and one. This allowed the
injection of first-order formulas in a network architecture, and also
simplified symbolic rule extraction.
  Our method trains a neural network using Levenderg-Marquardt algorithm, where
we restrict the knowledge dissemination in the network structure. We show how
this reduces neural networks plasticity without damage drastically the learning
performance. Making the descriptive power of produced neural networks similar
to the descriptive power of {\L}ukasiewicz logic language, simplifying the
translation between symbolic and connectionist structures.
  This method is used in the reverse engineering problem of finding the formula
used on generation of a truth table for a multi-valued {\L}ukasiewicz logic.
For real data sets the method is particularly useful for attribute selection,
on binary classification problems defined using nominal attribute. After
attribute selection and possible data set completion in the resulting
connectionist model: neurons are directly representable using a disjunctive or
conjunctive formulas, in the {\L}ukasiewicz logic, or neurons are
interpretations which can be approximated by symbolic rules. This fact is
exemplified, extracting symbolic knowledge from connectionist models generated
for the data set Mushroom from UCI Machine Learning Repository.