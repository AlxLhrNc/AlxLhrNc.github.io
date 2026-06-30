---
title: "pyBOA"
excerpt: "Frontal detection using chlorophyll<br/><img src='/images/pyBOA/raw_chl.png' width='500'>"
collection: portfolio
date: 2022-12-19
citation: "Lhériau-Nice, A. (2023). pyBOA: Contextual front detection (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.8135921."
---
Science suggest that not ocean fronts are alike when considering biological standpoints. That gradients can be just as valid given the signature of some active fronts. But the histogram method can miss them, hence the creation of the pyBOA to generalise a gradient based algorithm to the larger community.

This detection algorithm is for oceanographic data (specifically chlorophyl / temperature but can be used for others), and is accessible on [Zenodo](https://doi.org/10.5281/zenodo.8135921) and through my [Github](https://github.com/AlxLhrNc/pyBOA).

Original pseudo-code: Belkin, I.M., O’Reilly, J.E., 2009. An algorithm for oceanic front detection in chlorophyll and SST satellite imagery. Journal of Marine Systems, Special Issue on Observational Studies of Oceanic Fronts 78, 319–326_ ([doi](https://doi.org/10.1016/j.jmarsys.2008.11.018)).

Transcription of the work from: Lin et al. (2019) - Matlab, Lin, L., Liu, D., Luo, C., Xie, L., 2019. Double fronts in the Yellow Sea in summertime identified using sea surface temperature data of multi-scale ultra-high resolution analysis. Continental Shelf Research 175, 76–86. ([doi](https://doi.org/10.1016/j.csr.2019.02.004)). Ben Galuardi, [boaR](https://rdrr.io/github/galuardi/boaR/man/boaR-package.html) - R package.

Additions: Generalized contextual filter, rolling percentile selection, morphological thinning for single lines. Expended to use lazy loading, dask, and xarray methods.

<img src='/images/pyBOA/example_pyBOA.png' width="1000">

_Example of output, overlaying chlorophyll-a (viridis collormap) and fronts (red)_
