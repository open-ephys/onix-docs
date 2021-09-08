.. _onidatasheet_ts4231_v1_array:

TS4231 Array for V1 Base Stations
###########################################
:Authors: Jonathan P. Newman
:IO: Frame Source, Register Access
:ONIX ID: 25
:ONIX Hubs: :ref:`headstage_64`, :ref:`headstage_neuropix1`

Description
*******************************************
The **TS4231 Array for V1 Base Stations**  ONIX device is a localization unit
that provides 3D position information. At is core, this device comprises an
array of optical to digital converters that work with both V1 and V2 ("Index")
and Steam/HTC base stations:

- `TS4231 <https://triadsemi.com/product/ts4231/>`__ Optical to digital converter

This device transmits data every time one of the sensors in the array receives
and optical signal. The host computer must perform the mathematics in order to
calculate positional information using these data.

.. _onidatasheet_ts4231_v1_array_reg:

Register Programming
*******************************************

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Address
      - Name
      - Access
      - Time of Effect
      - POR Value
      - Reset Action
      - Description

    * - 0x00
      - ENABLE
      - R/W
      - On Reset
      - Implementation dependent, see hub documentation
      - None
      - The LSB is used to enable or disable the device data stream:

            * 0x0: data output disabled
            * 0x1: data output enabled

.. _onidatasheet_ts4231_v1_array_d2h:

Device To Host Data Frames
******************************************
Each frame transmitted to the host is structured as follows:

.. wavedrom::

    {
        reg: [
          {bits: 64, name: "Acquisition Clock Counter", type: 0},
          {bits: 32, name: "Device Address", type: 0},
          {bits: 32, name: "Data Size", type: 0, attr: 16},

          {bits: 64, name: "Hub Clock Counter at Envelope Start", type: 3},

          {bits: 16, name: "Sensor Index", type: 4},

          {bits: 32, name: "Envelope Width (Hub Clock Cycles)", type: 5},

          {bits: 16, name: "Envelope Code", type: 6}

        ],
        config: {bits: 256, lanes: 8, vflip: true, hflip: true, fontsize: 11}
    }

Each frame encodes a single optical detection from a single TS4231 and
photodiode

.. figure:: /_static/images/device_ts4231-v1-array/ts4231-v1-waveforms.png
    :align: center

    Optical waveforms detected by the photodiode and the envelope output used
    for sweep classification.

Envelope codes are defined based on their width as follows:

:Sweep: Width <= 50.0 μS
:J0:    Width <= 62.5 μS
:K0:    Width <= 72.9 μS
:J1:    Width <= 83.3 μS
:K1:    Width <= 93.8 μS
:J2:    Width <= 104.0 μS
:K2:    Width <= 115.0 μS

Where Sweep is a light-sheet pass and Jx/Kx are synchronization flashes. See
the `Lighthouse Redox Project
<https://github.com/nairol/LighthouseRedox/blob/master/docs/Light%20Emissions.md>`__
for more information.

Host To Device Data Frames
******************************************
This device does not accept input frames. All write attempts will fail with an
error.
