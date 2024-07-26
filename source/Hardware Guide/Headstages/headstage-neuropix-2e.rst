.. _headstage_neuropix2e:

Neuropixels-2.0e Headstage
##############################
The ONIX **Neuropixels-2.0e Headstage** is a serialized, multifunction headstage
targeting `Neuropixels 2.0 probes <https://www.neuropixels.org/>`__.

.. image:: /_static/images/headstage-neuropix2e/headstage-np2e-with-probes.png
    :align: center
    :alt: ONIX Headstage-Neuropixels-2.0e
    :scale: 15%

- Two Neuropixels 2.0 probes
- A BNO055 9-axis IMU for real-time, 3D orientation tracking
- 0.640 g, 10.2 x 14.2 mm

.. csv-table::
   :widths: 18, 80

   "*PCIe host firmware compatibility*", "v 1.0 and above"

Coaxial Link
***********************************
For details on data serialization and headstage gateware, have a look at the
:doc:`serialization` page, which describes how coax headstages operate in
general terms. The Neuropixels-2.0e Headstage has the following coaxial link
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

Probe connector identification
***********************************

The connector for Probe A is on the same side as the tether connector, while the connector for Probe B is on the opposite side.

.. image:: /_static/images/headstage-neuropix2e/headstage-np2e-probe-connectors.png
    :align: center
    :alt: ONIX Headstage-Neuropixels-2.0e probe connectors

