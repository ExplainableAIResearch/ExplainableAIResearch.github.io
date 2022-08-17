---
layout: publication
title: "Explanation-Based Auditing"
authors: Daniel Fabbri, Kristen LeFevre
conference: Proceedings of the VLDB Endowment (PVLDB), Vol. 5, No. 1, pp. 1-12
  (2011)
year: 2011
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1109.6880v1"}
tags: []
---
To comply with emerging privacy laws and regulations, it has become common
for applications like electronic health records systems (EHRs) to collect
access logs, which record each time a user (e.g., a hospital employee) accesses
a piece of sensitive data (e.g., a patient record). Using the access log, it is
easy to answer simple queries (e.g., Who accessed Alice's medical record?), but
this often does not provide enough information. In addition to learning who
accessed their medical records, patients will likely want to understand why
each access occurred. In this paper, we introduce the problem of generating
explanations for individual records in an access log. The problem is motivated
by user-centric auditing applications, and it also provides a novel approach to
misuse detection. We develop a framework for modeling explanations which is
based on a fundamental observation: For certain classes of databases, including
EHRs, the reason for most data accesses can be inferred from data stored
elsewhere in the database. For example, if Alice has an appointment with Dr.
Dave, this information is stored in the database, and it explains why Dr. Dave
looked at Alice's record. Large numbers of data accesses can be explained using
general forms called explanation templates. Rather than requiring an
administrator to manually specify explanation templates, we propose a set of
algorithms for automatically discovering frequent templates from the database
(i.e., those that explain a large number of accesses). We also propose
techniques for inferring collaborative user groups, which can be used to
enhance the quality of the discovered explanations. Finally, we have evaluated
our proposed techniques using an access log and data from the University of
Michigan Health System. Our results demonstrate that in practice we can provide
explanations for over 94% of data accesses in the log.