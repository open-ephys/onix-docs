.. _headstage_neuropix1e:

Neuropixels-1.0e Headstage
##############################
The ONIX **Neuropixels-1.0e Headstage** is a serialized, multifunction headstage
targeting `Neuropixels 1.0 probes <https://www.neuropixels.org/probe>`__.

.. image:: /_static/images/headstage-neuropix1e/headstage-np1e-with-probe.webp
    :align: center
    :alt: ONIX Headstage-Neuropixels-1.0e
    :scale: 15%

- One Neuropixels 1.0 probe
- A BNO055 9-axis IMU for real-time, 3D orientation tracking

Coaxial Link
***********************************
For details on data serialization and headstage gateware, have a look at the
:doc:`serialization` page, which describes how coax headstages operate in
general terms. The Neuropixels-1.0e Headstage has the following coaxial link
properties:

.. table::
    :widths: 50 80 50 50 50

    +------------------------+--------------------+----------+----------+----------+
    | Parameter              | Value              | Min      | Max      | Unit     |
    |                        |                    |          |          |          |
    +========================+====================+==========+==========+==========+
    | Serializer             | TI DS90UB933       |          |          |          |
    +------------------------+--------------------+----------+----------+----------+
    | Coax Voltage           | 5.0*               | 3.0      | 5.5      | Volts    |
    +------------------------+--------------------+----------+----------+----------+

.. note:: Have a look at the :doc:`tethers` page for more details on micro-coax headstage tethers

.. important:: \*If your headstage is misbehaving, have a look at the :doc:`tether-voltage` page to confirm headstage power voltages 
