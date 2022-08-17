---
layout: publication
title: "Towards Accountable AI: Hybrid Human-Machine Analyses for Characterizing System Failure"
authors: Besmira Nushi, Ece Kamar, Eric Horvitz
conference: AAAI Conference on Human Computation and Crowdsourcing 2018
year: 2018
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1809.07424v1"}
tags: []
---
As machine learning systems move from computer-science laboratories into the
open world, their accountability becomes a high priority problem.
Accountability requires deep understanding of system behavior and its failures.
Current evaluation methods such as single-score error metrics and confusion
matrices provide aggregate views of system performance that hide important
shortcomings. Understanding details about failures is important for identifying
pathways for refinement, communicating the reliability of systems in different
settings, and for specifying appropriate human oversight and engagement.
Characterization of failures and shortcomings is particularly complex for
systems composed of multiple machine learned components. For such systems,
existing evaluation methods have limited expressiveness in describing and
explaining the relationship among input content, the internal states of system
components, and final output quality. We present Pandora, a set of hybrid
human-machine methods and tools for describing and explaining system failures.
Pandora leverages both human and system-generated observations to summarize
conditions of system malfunction with respect to the input content and system
architecture. We share results of a case study with a machine learning pipeline
for image captioning that show how detailed performance views can be beneficial
for analysis and debugging.