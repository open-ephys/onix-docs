.. _serialization:
.. |year| date:: %Y

Data Serialization & Power
###################################
The major advantage of ONI-compliant headstages, compared to others, is that
they contain onboard logic for controlling and streaming from arbitrary
configurations of head-borne devices using a unified, bidirectional data
stream. In this way, data can be sent to host hardware (see :ref:`hosts`) using
modern serializer/deserialzer (SERDES) chips that vastly reduce the amount of
wiring required for communication, or even wirelessly.

Coaxial Serialization
=======================
ONIX headstages use a coaxial serializer for host communication. This chip
provides power and bidirectional data transmission to and from from the
headstage using a single coaxial cable (one signal wire and an outer shield).
The coaxial cable is the only external connection to the headstage. Power (DC),
a control "back-channel" (MHz), and a data "forward-channel" (GHz)
occupy different portions of the RF spectrum and therefore can be resolved as
distinct signal streams. Any high-quality 50-Ohm characteristic impedance cable
with low loss in the GHz frequency range can be used to make this connection
(e.g. SMA cables). However, the connection to the headstage is usually
accomplished using specialized micro-coax cable that is extremely thin and
flexible. We generally use cables that are 0.2-0.38 mm in diameter.

.. note:: Have a look at the :ref:`tethers` page for more detials on mirco-coax
    headstage tethers

ONIX headstages use an FPGA to control peripheral devices
and stitch together their data streams prior to serialization. For instance,
:ref:`headstage_64_1r3` and :ref:`headstage_neuropix_1r2` use an `Intel MAX10
FPGA
<https://www.intel.com/content/www/us/en/products/programmable/fpga/max-10.html>`_.
The exact FPGA is not important because every ONI-compliant headstage is
uses very similar gateware (FPGA-based firmware) that performs three major
functions

1. **Local Hardware Control** Provides hardware controllers (SPI, I2C, etc),
   timing, and control logic for each of the sensors and actuators on the
   headstage

2. **Data Streaming** Provides a standard protocol for arbitrating access of
   each of the device data streams to the serializer.

3. **Register Programming** Provides a standard interface for bi-directional
   configuration and control of the devices on the headstage.

Power
=======================
As mentioned in the previous section, power is DC-coupled into the coaxial link
at the host and recovered at the headstage via a second, inductive DC path.
This "T-network" provides a low impedance path for the DC portion of the signal
(power) and rejects the RF components so that they are preserved for
communication between the SERDES pair.

.. figure:: /asset/image/rf-t.png
    :align: center

    LC-network for combining power and data on the coaxial cable.

Its important to note that this circuit is completely passive. Therefore
whatever voltage is supplied at the host side will end up at the input to the
headstage. Care must be taken to make sure this voltage is appropriate.

.. warning:: Do not exceed the maximaum voltage at the coaxial input to the
    headstage. Make sure you make this measurement at the headstage to account for
    a potential voltage drop in the tether. Exceeding this voltage can permanently
    damage the headstage.

Further, if a long and thin coaxial tether is used, the DC resistivity of the
wire can accumulate, resulting in a significant voltage drop across the cable.

.. note:: Long, thin tethers can have a significant series resistance that
    results in a voltage drop across the length of the tether. This may have to be
    compensated for by tuning the host input voltage to account for the drop. See
    :ref:`fmc_host_1r3` for how.

DS90UB9x3 Communication Protocols
========================================================

Data Serialization 
--------------------------------------------------------
Applicable headstages:

- :ref:`headstage_64_1r3`
- :ref:`headstage_neuropix_1r2`

The `DS90UB933 <https://www.ti.com/product/DS90UB933-Q1>`_ is a 100 MHz
parallel to coaxial serializer that is typically used for streaming camera
data. We have created gateware that adapts this chip to talk to any number of
heterogeneous data sources using the following serialization protocol

.. wavedrom::

    { 
    signal: [
      {name: 'pclk', wave: 'P.....|.....'},
      {name: 'hsync', wave: '0.10..|.....', },
      {name: 'vsync', wave: '0.....|.10..', data: ['head', 'body', 'tail', 'data']},
      {name: 'data', wave: 'x.35..|.4x..', data: ['ID', 'data', 'CRC', 'data']},
    ], 
    config: { hscale: 1},
    head: {
        text:'DS90UB933 Serialization Protocol',
        tick:0,
    },
    }

|

These signals are present on the FPGA-sides of the serializer and deserializer,
prior to headstage serialization and after host deserialization, respectively.

:``plck``: The serializers pixel clock, repurposed for generic data
           transmission for ONIX headstages.
:``hsync``: The horizontal synchronization signal, repurposed on ONIX
            headstages to indicate the ``data`` bus contains a device ID on
            ONIX headstages
:``vsync``: The vertical synchronization signal, repurposed to indicate the
            ``data`` bus a CRC value for the preceeding packet on ONIX
            headstages
:``data``: The 12-bit data bus containing device ID, CRC value, or device data
           depending on the states of ``hsync`` and ``vsync``

Following serialization, these data are transmitted over the coaxial cable
using an RF-encoding scheme called `FDP Link III
<https://en.wikipedia.org/wiki/FPD-Link>`_ which embeds the clock in the data
stream and allows for active equalization to compensate for imperfections in
the cable. This link uses and 700 MHz carrier for high speed data and provides
a low speed bidirectional link for sending triggers and configuration to the
headstage.

Register Configuration 
--------------------------------------------------------
TODO
