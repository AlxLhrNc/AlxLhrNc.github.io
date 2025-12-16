---
title: "pyBOA"
excerpt: "Frontal detection using chlorophyll<br/><img src='/images/pyBOA/raw_chl.png' width='500'>"
collection: portfolio
date: 2022-12-19
citation: "Lhériau-Nice, A. (2023). pyBOA: Contextual front detection (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.8135921."
---

Detection algorithm for oceanographic data (specifically chlorophyl / temperature but can be used for others) accessible on [Zenodo](https://doi.org/10.5281/zenodo.8135921).

Original pseudo-code: Belkin, I.M., O’Reilly, J.E., 2009. An algorithm for oceanic front detection in chlorophyll and SST satellite imagery. Journal of Marine Systems, Special Issue on Observational Studies of Oceanic Fronts 78, 319–326_ ([doi](https://doi.org/10.1016/j.jmarsys.2008.11.018)).

Transcription of the work from: Lin et al. (2019) - Matlab, Lin, L., Liu, D., Luo, C., Xie, L., 2019. Double fronts in the Yellow Sea in summertime identified using sea surface temperature data of multi-scale ultra-high resolution analysis. Continental Shelf Research 175, 76–86. ([doi](https://doi.org/10.1016/j.csr.2019.02.004)). Ben Galuardi, [boaR](https://rdrr.io/github/galuardi/boaR/man/boaR-package.html) - R package.

Additions: Generalized contextual filter, rolling percentile selection, morphological thinning for single lines.

What to get: The sample netcdf file, the stnd_alone file, and pyBOA.py.

Important This works as an extension of the xarray packages and was built under python 3.9.

<img src='/images/pyBOA/example_pyBOA.png' width="1000">
_Example of output, overlaying chlorophyll-a (viridis collormap) and fronts (red)_
