.. _serialization:

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
flexible. We generally use cables that are 150-300 μm in diameter.

.. note:: Have a look at the :ref:`tethers` page for more detials on mirco-coax
    headstage tethers

ONIX headstages use an FPGA to control peripheral devices and combine their
data streams prior to serialization. For instance, :ref:`headstage_64_1r3` and
:ref:`headstage_neuropix_1r2` use an `Intel MAX10 FPGA
<https://www.intel.com/content/www/us/en/products/programmable/fpga/max-10.html>`_.
The exact FPGA is not important because every ONI-compliant headstage is uses
very similar gateware (FPGA-based firmware) that performs three major functions

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

.. figure:: /_static/images/rf-t.png
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
    compensated for by tuning the host input voltage to account for the drop. ONIX
    host boards have this ability (e.g. see :ref:`fmc_host_1r3`).

DS90UB933/4 Communication Protocols
========================================================
The `DS90UB933 <https://www.ti.com/product/DS90UB933-Q1>`_/`DS90UB934
<https://www.ti.com/product/DS90UB934-Q1>`_ are a coaxial SERDES pair used on
several ONIX headstages and host modules:

- :ref:`headstage_64_1r3` (DS90UB933 Serilizer)
- :ref:`headstage_neuropix_1r2` (DS90UB933 Serilizer)
- :ref:`fmc_host_1r3` (DS90UB934 Deserilizer)

along with the UCLA Miniscope and its derivatives. This section describes how this
SERDES pair is used for control of and communication with headstages.

Data Serialization
--------------------------------------------------------
The `DS90UB933 <https://www.ti.com/product/DS90UB933-Q1>`_ is a 100 MHz
parallel to coaxial serializer that is typically used for streaming camera
data. ONIX headstages use an intermediate FPGA to translate data from any
number of heterogeneous data sources to the serializer input using the
following simple protocol

.. wavedrom::

    {
    signal: [
      {name: 'pclk', wave: 'P.....|.....'},
      {name: 'hsync', wave: '0.10..|.....', },
      {name: 'vsync', wave: '0.....|.10..', data: ['head', 'body', 'tail', 'data']},
      {name: 'data', wave: 'x.35..|.4x..', data: ['ID', 'frame', 'CRC', 'data']},
    ],
    config: { hscale: 1},
    head: {
        text:'DS90UB933 Serialization Protocol',
        tick:0,
    },
    }

|

where the signal lines are defined as follows:

:``plck``: The serializer's pixel clock, repurposed for generic data
           transmission for ONIX headstages.
:``hsync``: The horizontal synchronization signal, re-purposed on ONIX
            headstages to indicate the ``data`` bus contains a device ID on
            ONIX headstages
:``vsync``: The vertical synchronization signal, re-purposed to indicate the
            ``data`` bus a CRC value for the preceeding packet on ONIX
            headstages
:``data``: The 12-bit data bus containing device ID, CRC value, or device data
           depending on the states of ``hsync`` and ``vsync``

The ``ID`` is the device index within the host device table, ``frame`` is a
device's frame data, and ``CRC`` is a `CRC-12
<https://en.wikipedia.org/wiki/Cyclic_redundancy_check>`__ of the ``ID`` and
``frame`` elements.  See the  `ONI Specification
<https://github.com/open-ephys/ONI>`__ for detailed descriptions of these
elements meaning.

These signal lines are present on the FPGA-side of both the serializer and
deserializer, prior to headstage serialization and after host deserialization,
respectively. This means that the serializer link is effectively "invisible"
from the host's perspective, and the headstage can be treated as if it was just
a module on the host itself.

During serialization, data are transmitted over the coaxial cable
using an RF-encoding scheme called `FDP Link III
<https://en.wikipedia.org/wiki/FPD-Link>`_ which embeds the clock in the data
stream and allows for active equalization to compensate for imperfections in
the cable. This link uses and 700 MHz carrier for high speed data and provides
a low speed bidirectional link for sending triggers and configuration to the
headstage.

Register Configuration
--------------------------------------------------------
The `DS90UB933 <https://www.ti.com/product/DS90UB933-Q1>`_/`DS90UB934
<https://www.ti.com/product/DS90UB934-Q1>`_ SERDES pair have a I2C-based
backchannel for bidirectional communication. This channel is used for two
purposes in ONIX hardware.

#. Device configuration via register writing and reading. e.g. setting and
   bandwidth of the filters on the Intan chip.
#. Flashing the headstage FPGA's non-volatile memory with updated firmware.

The `ONI Specification <https://github.com/open-ephys/ONI>`__ describes a
register programming protocol that is very similar to a simple wishbone bus.
This bus needs to be transmitted over the DS90UB933/4 I2C backchannel to be used
to configure headstage devices. We have developed a simple Wishbone over I2C
module to accomplish this .

..
    A bitfield?
    ------------------------------
    Status

    .. wavedrom::

            {
            reg: [
                {                       "bits": 1 },
                { "name": "WBUSY",      "bits": 1 },
                { "name": "WCOMPLETE",  "bits": 1 },
                { "name": "WERROR",     "bits": 1 },
                { "name": "RBUSY",      "bits": 1 },
                { "name": "RCOMPLETE",  "bits": 1 },
                { "name": "RERROR",     "bits": 1 },
                { "name": "SEQERROR",   "bits": 1 }
            ],
            config: {bits: 8, vflip: true, hflip: false},
            }


    A state machine?
    --------------------------------
    .. graphviz::

       digraph {

          "IDLE" -> "WRITE ENABLE";
          "IDLE" -> "READ REQUEST";

          "WRITE ENABLE" -> "WRITE ADDR";

          "READ REQUEST" -> "WRITE ADDR";
       }

    "WRITE ADDR " -> "WRITE VAL0";
    "IDLE" -> "WRITE VAL1";
    "IDLE" -> "STATUS START";
    "IDLE" -> "STATUS REPORT";

    Protocol Transactions Definitions:
    --------------------------------------

     - [ : I2C start
     - ] : I2C stop
     - W : child device address + I2C write bit
     - R : child device address + I2C read bit

     - Status_result:
        - [X, w_busy, w_complete, w_error, r_busy, r_complete, r_error, seq_error]
        - seq_error always reset after successful "atomic" sequence

     - Command words:

        #. 0x00 WRITE_ENABLE
        #. 0x01 READ_REQUEST
        #. 0x02 READ_ENABLE_0
        #. 0x03 READ_ENABLE_1
        #. 0x04 READ_ENABLE_2
        #. 0x05 READ_ENABLE_3
        #. 0x06 READ_ENABLE_4
        #. 0x07 STATUS_0
        #. 0x08 STATUS_1
        #. 0xFF INVALID

    Course-grained States Machine
    -----------------------------

        IDLE:

            - if reg_tx.cyc = '1' and reg_tx.we = '1' then
                goto WRITE_REGISTER
              else if reg_tx.cyc = '1' and reg_tx.we = '0' then
                goto READ_REGISTER

        WRITE_REGISTER:

            1. [W, WRITE_ENABLE, dev_idx]
            2. [W, reg_tx.addr(15:8), reg_tx.addr(7:0)]
            3. [W, reg_tx.val(31:24), reg_tx.val(23:16)]
            4. [W, reg_tx.val(15:08), reg_tx.val(07:00)]

            5. [W, STATUS_0, reg_tx.idx]
            6. [W, STATUS_1, [R, status_result]

            - Repeat 5 & 6 repeat until status_result(5) = 1
            - reg_rx.err <= status_result(4) or status_result(0)
            - reg_rx.ack <= '1'
            - goto CYC_WAIT

        READ_REGISTER:

            1. [W, READ_REQUEST, reg_tx.idx]
            2. [W, reg_tx.addr(15:8), reg_tx.addr(7:0)]

            3. [W, STATUS_0, reg_tx.idx]
            4. [W, STATUS_1, [R, status_result]

            - Repeat 3 & 4 until status_result(5) = 1
            - if status_result(0) or status_result(4)
                reg_rx.ack <= '1'
                reg_rx.err <= '1'
                goto CYC_WAIT
              else
                continue

            5. [W, READ_ENABLE_0, reg_tx.idx]
            6. [W, READ_ENABLE_1, [R, reg_rx.val(31:24)]
            7. [W, READ_ENABLE_2, [R, reg_rx.val(23:16)]
            8. [W, READ_ENABLE_3, [R, reg_rx.val(15:08)]
            9. [W, READ_ENABLE_4, [R, reg_rx.val(07:00)]

           10. [W, STATUS_0, reg_tx.idx]
           11. [W, STATUS_1, [R, status_result]

            -  reg_rx.err <= status_result(0) or status_result(1)
            -  reg_rx.ack <= '1'
            -  goto CYC_WAIT

         CYC_WAIT:

            - reg_rx_o.ack <= '0';
            - reg_rx_o.err <= '0';
            - if reg_tx.cyc = 0
                goto IDLE
