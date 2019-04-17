Compatibility
=============

The following define the WPS process requirements to be compatible with
the ESGF end-user API. Included are various examples of the WPS process 
inputs_ and output_.

Original document_.

.. _Document: https://docs.google.com/document/d/1GSLwSJPUCfs-ZrYCG1n7BcWyldvb4pT9nYD3zkPCwao

Full examples_.

Inputs
------

.. _Inputs:

The **datainputs** parameter will consist of the following three types.

- Domain_
- Variable_
- Operation_

Domain
^^^^^^

.. _Domain:

This WPS input should use the identifier **domain**. The input will be passed
an array of domains that are comprised of one or more dimensions_.

- id *[Required]*
- mask_ *[Optional]*
- One ore more dimensions_ keyed using a descriptive identifier. *[Required]*

Example::
  
  domain=[{"id":"d0", ...}, {"id":"d1", ...}]

Domain Example::

  {
    "id":"d0",
    "latitude": {
      "start": 0.0,
      "end": 45.0,
      "step": 1.5,
      "crs": "values",
    },
    "longitude": {
      "start": 10,
      "end": 20,
      "crs": "indices",
    },
    "time": {
      "start": 1981,
      "end": 2016,
      "crs": "values",
    },
  }

Dimension
"""""""""

.. _Dimensions:

Dimensions describe either a spatial or temporal space.

- start *[Required]*
- stop *[Required]*
- step *[Optional]*
- crs *[Required]*

Example::

  {"start": 0.0, "end": 90.0, "step": 1, "crs": "indices"}

Mask
""""

.. _Mask:

Defines a mask to be applied to the variable_. The acceptable values for
operation are constants, *mask_data*, *var_data* and any function implemented
by the server. i.e. sin(*var_data*), etc

- uri *[Required]*
- id *[Required]*
- operation *[Required]*

Example:

  {"uri": "http://.../tas_mask.nc", "id": "tas", "operation": "mask_data>0.5"}

Variable
^^^^^^^^

.. _Variable:

This WPS input should use the identifier **variable**. The input will be passed
an array of variables that define all inputs for the process.

- id *[Required]* - Can be extended with a **|** followed by an identifier that will be used to reference the *Variable*
- uri *[Required]*
- domain *[Optional]*

Example::

  variable=[{"id": "tas|v0", ...}, {"id": "tas|v1", ...}]

Variable Example::

  {"id": "tas|v0", "uri": "http://.../test.nc", "domain": "d0"}

Operation
^^^^^^^^^

.. _Operation:

This WPS input should use the identifier **operation**. The input will be passed
an array of operations.

- name *[Required]*
- input *[Required]* - List of inputs
- result *[Optional]* - Name that can be referenced by other operations when creating workflows
- domain *[Optional]*
- axes *[Optional]*
- gridder_ *[Optional]*
- Zero or more additional parameters *[Optional]*

**Notes:**
Axes and additional parameter values can be a single value or multiple separated
by a \|.

Example::
  
  operation=[{"name":"CDS.timeBin", ...},{"name": "CDS.diff2", ...}]

Operation Example::

  {
    "name": "CDS.timeBin",
    "input": ["v0"],
    "result": "cycle",
    "domain": "d0",
    "axes": "time",
    "bins": "t|month|ave|year",
  }

Gridder
"""""""

.. _Gridder:

Defines the regridder to use for the operation it's passed to.

- tool *[Required]*
- method *[Required]*
- grid *[Required]*

Example::

  {"tool": "esmf", "method": "linear", "grid": "T42"}

Operation Example::

  {
    "name": "averager.multi_model_ensemble_mv",
    "gridder": {
      "tool": "esmf",
      "method": "linear",
      "grid": "T42",
    },
    ...
  }

Output
------

.. _Output:

The WPS process should only have a single output_ whose identifier is **output**. It
should have an application/json mimetype and contain an list of Variable like objects.

- uri *[Required]*
- id *[Optional]*
- domain *[Optional]*
- mime-type *[Optional]*

Example::

  [{
    "uri": "http://..../output.nc",
    "id": "tas_avg_mon",
    "domain": {"id":"d0", ...},
    "mime-type": "x-application/netcdf",
  }]

Full Examples
-------------

.. _Examples:

::

  import esgf

  NH = esgf.Domain(dimensions=[
    esgf.Dimension(0.0, 90.0, esgf.Dimension.values, name='latitude'),
  ],
  name = 'd0')

  tas = esgf.Variable('http://.../tas.nc', 'tas', name='v0', domains=[NH])

  wps = esgf.WPS('http://.../wps')

  avg = wps.get_process('averager.mv')

  parameters = [
    esgf.NamedParameter('axes', 'latitude'),
  ]

  avg.execute([tas], domain=None, parameters)

Formed Url::

  http://.../wps?service=WPS&version=1.0.0&request=execute&identifier=averager.mv&datainputs=
    domain=[{"id":"d0","latitude":{"start":0.0,"end":90.0,"step":1.0,"crs":"values"}}];
    variable=[{"id":"tas|tas","uri":"http://.../tas.nc",domain="d0"}];
    operation=[{"name":"averager.mv","input":["v0"],"axes":"latitude"}]
    &storeexecuteresponse=false&status=&false
