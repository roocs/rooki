Usage
=====

.. code-block:: python

  # Optional: set ROOK_URL ... or use default
  import os
  os.environ['ROOK_URL'] = http://localhost:5000/wps
  # import rooki
  from rooki import rooki
  # run subset on c3s-cmip5 dataset with time selection
  response = rooki.subset(
    collection='c3s-cmip5.output1.ICHEC.EC-EARTH.historical.day.atmos.day.r1i1p1.tas.latest',
    time='1860-01-01/1900-12-30')
  # successful?
  response.ok
  # show links to result files
  response.download_urls()
