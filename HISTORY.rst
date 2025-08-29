Version History
===============

v0.6.4 (2025-08-26)
-------------------

Changes
^^^^^^^

* Fix config. Allow duplicate keys (#185).
* Updated notebooks for CMIP6 and atlas v2.

v0.6.3 (2024-07-25)
-------------------

Changes
^^^^^^^

* Pin intake<2.0 (#165).
* Update notebooks for regrid operator (#166).

v0.6.2 (2024-05-15)
-------------------

Changes
^^^^^^^

* Fix usage of signal in birdy (#163).
* Added notebooks for atlas.

v0.6.1 (2023-11-10)
-------------------

Changes
^^^^^^^

* Clean up setup (#146).
* Updated notebooks for weighted average and cmip6-decadal (#148).

v0.6.0 (2023-11-03)
-------------------

New Features
^^^^^^^^^^^^

* Added operator and notebook for `Regrid` (#133).
* Added operator and notebook for `WeightedAverage` (#132).

Changes
^^^^^^^

* Support only Python >= 3.9
* Added cf-xarray dependency (#143)
* Updated to birdy >= 0.8.2 (#124)
* Added notebook for atlas
* Updated notebooks (subset, cmip6-decadal, intake).

v0.5.0 (2022-09-28)
-------------------

New Features
^^^^^^^^^^^^

* Added operator and notebook for `Concat` demo (#104).

Changes
^^^^^^^

* Updated notebooks (subset, cmip6-decadal, intake).

v0.4.0 (2022-04-14)
-------------------

New Features
^^^^^^^^^^^^

* Added operator for `AverageByTime` (#93, #96).

Changes
^^^^^^^

* Added notebooks for CMIP6 decadal (#89, #91).
* Added notebooks for "subset by point" (#87).
* Updated notebooks for c4i demo (#86, #94, #95).
* Updated notebooks for "average" operator (#93, #96).


v0.3.3 (2021-08-12)
-------------------

New Features
^^^^^^^^^^^^

* Use reinit internally to update config from environment variables ... e.g. update access token (#81).
* Added wps lineage option (#80).
* Using environment variable ACCESS_TOKEN for OAuth access token (#80).

Changes
^^^^^^^

* Updated notebooks for c4i and dashboard demo.


v0.3.2 (2021-03-21)
-------------------

Changes
^^^^^^^

Notebooks:

* Added tests (#55, #58, #59)
* Added c4i demo (#54).
* Added intake example (#56).

Bug Fixes
^^^^^^^^^

* Quick fix for missing cancel function (#57).
* Allow metalink download from unverified https end-point (#52).

v0.3.1 (2021-02-24)
-------------------

Changes
^^^^^^^

* Updated notebooks (#45, #46, #47, #48).
* Updated requirements (birdy>=0.7.0).

v0.3.0 (2020-12-18)
-------------------

New Features
^^^^^^^^^^^^

* Configure output folder for metalink downloads (#41).
* Access provenance document (#38).
* Added provenance notebook (#39).
* Added test notebook with execution time measure (#40).


v0.2.3 (2020-11-05)
-------------------

New Features
^^^^^^^^^^^^

* Allow Python 3.6 (#36)
* Run travis tests on multiple Python versions >= 3.6.
* Run doc build test on travis.

v0.2.2 (2020-11-02)
-------------------

Bug Fixes
^^^^^^^^^

* Using pymetalink package from pypi (#34).

v0.2.1 (2020-10-28)
-------------------

Bug Fixes
^^^^^^^^^

* Fixed pymetalink requirement (#33).


v0.2.0 (2020-10-26)
-------------------

New Features
^^^^^^^^^^^^

* Lightweight wrapper for birdy WPS client.
* Operators to build workflow.
* Configuration to overwrite default settings.
* Result object to access MetaLink outputs.
* Notebooks with usage examples.

v0.1.0 (2020-03-19)
-------------------

* First release.
