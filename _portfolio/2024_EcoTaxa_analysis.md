---
title: "Analysing Project 11231"
excerpt: "Example of diverity analysis using R on EcoTaxa"
collection: portfolio
date: 2024-07-20
---

These analysis were done in the context of my Ph.D. at the University of Auckland. The primary goal was to identify any effect of fine-scale oceanic features (namely chlorophyll fronts), on the diversity of the planktonic community. 

The analysis was done exclusively on R 4.0.1, using a code similar to the one available on [my github](https://github.com/AlxLhrNc/EcoTaxa-Analysis). Information on the EcoTaxa project 11231 is also [available here](https://alxlhrnc.github.io/portfolio/2024_EcoTaxa/).

While the draft images where done on R using ggplot2, the figures used in the resulting [article](https://alxlhrnc.github.io/publication/2025_12_31_Marine&FreshwaterResearch_NZ) were edited by [David Pierre Milesi-Gaches](https://www.researchgate.net/profile/David-Pierre-Milesi-Gaches) using Inkscape. This significantly improved their readability.

Pre-processing of the data
======
Considering the data was acquiered using two methods accross the three size classes selected (20-200 μm, 200-500 μm, 500+ μm), quite a bit of cleaning was requiered to obtain one global dataset that R could utilise properly.

Sampling
=====
The sampling was done accross four dates, time 16 samples, covering two seasons (summer and autumn).

<img src='/images/EcoTaxa/map.png' width="1000">
_Sampling map with bathymetry as background. Samplings blue and orange done in Summer, teal and green done in Autumn. Credit [David Pierre Milesi-Gaches](https://www.researchgate.net/profile/David-Pierre-Milesi-Gaches)_

Species composition & Species diversity (α, β, and γ)
=====
Basic species composition barplots were obtained using ggplot2, and later edited on Inkscape.
Getting the α diversity was the easiest, followed by the γ diversity, which I decided to separate based on the sampling dates. The β diversity was used using the generalised Sørensen dissimilarity index presented by [Baselga (2010)](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1466-8238.2009.00490.x), and all indexes were plotted together.
The overall result indicate a shift in species caused by the presence of chlorophyll fronts.

<img src='/images/EcoTaxa/diversity.png' width="1000">
_Species composition barplots and diversity indexes lines. Credit [David Pierre Milesi-Gaches](https://www.researchgate.net/profile/David-Pierre-Milesi-Gaches)_


For more information on the methods and results, please go to the [article](https://alxlhrnc.github.io/publication/2025_10_14_Marine&FreshwaterResearch_NZ). For the code, please go to the [github project](https://github.com/AlxLhrNc/EcoTaxa-Analysis).