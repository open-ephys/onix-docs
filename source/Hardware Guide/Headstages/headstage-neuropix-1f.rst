.. _headstage_neuropix1:

Neuropixels-1.0f Headstage
##############################
The ONIX **Neuropixels-1.0f Headstage** is a serialized, multifunction headstage
targeting `Neuropixels 1.0 probes <https://www.neuropixels.org/>`__.

.. image:: /_static/images/headstage-neuropix1/headstage-neuropix1_1r2_side-with-probes.jpg
    :align: center
    :alt: ONIX Headstage-Neuropixels-1.0f v1.2.

- Two Neuropixels 1.0 probes
- A BNO055 9-axis IMU for real-time, 3D orientation tracking
- Three TS4231 light to digital converters for real-time, 3D position tracking
  with HTC Vive base stations
- An Intel MAX10 FPGA for real-time probe data correction (offset removal and
  gain correction) and data arbitration

Coaxial Link
***********************************
For details on data serialization and headstage gateware, have a look at the
:ref:`serialization` page, which describes how coax headstages operate in
general terms. The Neuropixels-1.0f Headstage has the following coaxial link
properties:

.. table::
    :widths: 50 80 50 50 50

    +------------------------+--------------------+----------+----------+----------+
    | Parameter              | Value              | Min      | Max      | Unit     |
    |                        |                    |          |          |          |
    +========================+====================+==========+==========+==========+
    | FPGA                   | Intel 10M08SAM153  |          |          |          |
    +------------------------+--------------------+----------+----------+----------+
    | Serializer             | TI DS90UB933       |          |          |          |
    +------------------------+--------------------+----------+----------+----------+
    | Coax Voltage           | 5.0*               | 4.5*     | 6.5*     | Volts    |
    +------------------------+--------------------+----------+----------+----------+
    | PCLK Frequency         | 42                 |          |          | MHz      |
    +------------------------+--------------------+----------+----------+----------+

.. note:: Have a look at the :ref:`tethers` page for more details on micro-coax
    headstage tethers
