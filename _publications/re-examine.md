---
title: "Re-Examining System-Level Correlations of Automatic Summarization Evaluation Metrics"
collection: publications
permalink: /publication/re-examine
date: 2022-07-10
venue: 'The North Americal Chapter of the Association for Computational Linguistics (NAACL)'
paperurl: 'https://aclanthology.org/2022.naacl-main.442.pdf'
citation: '<b>"Re-Examining System-Level Correlations of Automatic Summarization Evaluation Metrics."</b> Dan Deutsch, Rotem Dror, and Dan Roth. <i> In Proceedings of the 2022 Annual Meeting of the North American Chapter of the Association for Computational Linguistics (NAACL).</i>'
---

<b> Abstract </b>
How reliably an automatic summarization evaluation metric replicates human judgments of summary quality is quantified by system-level correlations. We identify two ways in which the definition of the system-level correlation is inconsistent with how metrics are used to evaluate systems in practice and propose changes to rectify this disconnect. First, we calculate the system score for an automatic metric using the full test set instead of the subset of summaries judged by humans, which is currently standard practice. We demonstrate how this small change leads to more precise estimates of system-level correlations. Second, we propose to calculate correlations only on pairs of systems which are separated by differences in automatic scores that are commonly used to argue one system is of higher quality. This allows us to demonstrate that our best estimate of the correlation of ROUGE to human judgments is near 0 in realistic scenarios. The results from the analyses point to the need to collect more high-quality human judgments and to improve automatic metrics when differences in system scores are small.

