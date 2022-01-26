---
title: "A Statistical Analysis of Summarization Evaluation Metrics using Resampling Methods"
collection: publications
permalink: /publication/summarizationeval
date: 2021-04-01
venue: 'Transactions of the Association for Computational Linguistics (TACL)'
paperurl: 'https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00417/107833/A-Statistical-Analysis-of-Summarization-Evaluation'
citation: '<b> A Statistical Analysis of Summarization Evaluation Metrics Using Resampling Methods."</b> Daniel Deutsch, Rotem Dror, Dan Roth. <i> of the Association for Computational Linguistics 2021; 9 1132–1146.</i>'
---

<b> Abstract </b>
The quality of a summarization evaluation metric is quantified by calculating the correlation between its scores and human annotations across a large number of summaries. Currently, it is not clear how precise these correlation estimates are, nor whether differences between two metrics' correlations reflects a true difference or if it is due to random chance. In this work, we address these two problems by proposing methods for calculating confidence intervals and running hypothesis tests for correlations using two resampling methods, bootstrapping and permutation. After evaluating which of the proposed methods is most appropriate for summarization through two simulation experiments, we analyze the results of applying these methods to several different automatic evaluation metrics across three sets of human annotations. We find that the confidence intervals are rather wide, demonstrating high uncertainty in how reliable automatic metrics truly are. Further, although many metrics fail to show statistical improvements over ROUGE, two recent works, QAEval and BERTScore, do in some evaluation settings.

<b> Github </b>
https://github.com/CogComp/stat-analysis-experiments
