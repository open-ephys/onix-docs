#################
RHS2116 Headstage
#################

.. image:: /_static/images/rhs2116/rhs2116.webp
    :align: center
    :height: 300px
    :alt: ONIX rhs2116

|

The RHS2116 Headstage is a serialized headstage for small animals with 32
bi-direcional channels which each can be used to deliver electrical stimuli.
The RHS2116 Headstage can be used with passive probes (e.g. silicon arrays, EEG/ECOG
arrays, etc) using a 36-Channel Omnetics EIB. 

********
Features
********

* Two RHS2116 ICs for a combined 32 bi-directional ephys channels
* ~1 millisecond active stimuls artifact recovery
* Max stimulator current: 2.55mA @ +/-7V compliance. 
* Sample rate: 30193.2367 Hz 
* Stimulus active and stimulus trigger pins
* On-board Lattice Crosslink™ FPGA for real-time data arbitration

..  _rhs2116_data_link_serialization:

***********************
Data Link Serialization
***********************

For details on data serialization and headstage gateware, have a look at the
:ref:`serialization` page, which describes how coax headstages operate in
general terms. The RHS2116 headstage has the following coaxial link properties:

.. table::
    :widths: 50 80 50 50 50

    +------------------------+--------------------+----------+----------+----------+
    | Parameter              | Value              | Min      | Max      | Unit/    |
    |                        |                    |          |          | Type     |
    +========================+====================+==========+==========+==========+
    | FPGA                   | LIF-MD6000-6UMG64I |          |          |          |
    +------------------------+--------------------+----------+----------+----------+
    | Serializer             | TI DS90UB933       |          |          | Coaxial  |
    +------------------------+--------------------+----------+----------+----------+
    | Supply Voltage         | 4.0                | 3.4      | 5.0*     | Volts    |
    +------------------------+--------------------+----------+----------+----------+
    | Hub Clock Frequency    | 50                 |          |          | MHz      |
    +------------------------+--------------------+----------+----------+----------+

.. warning:: \*Do not exceed 5.0 VDC at the coaxial input to the headstage.
   Make sure you make this measurement at the headstage (see
   :ref:`measure_voltage`) to account for a potential voltage drop in the
   tether. 

.. note:: Have a look at the :ref:`tethers` page for more details on micro-coax
   headstage tethers

*****************
Electrophysiology
*****************

RHS2116 headstage uses two 16-channel `Intan RHS2116
<https://intantech.com/>`__ bioamplifier chip. The chip is operated at a fixed
sampling rate of ~30 kHz/channel. These 32 ephys channels are exposed via a 36
pin `Omnetics connector
<https://www.omnetics.com/wp-content/uploads/2022/01/A79025-001.pdf>`__ at the
edge of the headstage and can record from most passive probes (e.g. tetrodes,
silicon probe arrays, tungsten microwires, steel EEG wires, etc.) as well as
stimulate.

.. 
    RHS2116 Pinout
    ==============

    ..  image:: /_static/images/rhs2116/rhs2116-omnetics-pinout.webp
        :align: center
        :height: 300px
        :alt: ONIX rhs2116 omnetics

    |

    ..  image:: /_static/images/rhs2116/rhs2116-bottom-pinout.webp
        :align: center
        :height: 300px
        :alt: ONIX rhs2116 bottom pinout

*****************
Bill of Materials
*****************

- `Interactive BoM <../../_static/boms/headstage-rhs2116_bom.html>`__ (a csv BoM can be downloaded from this page)

.. note:: Have a look at the :ref:`tether_voltage` page for more details on probing and verifying headstage power voltages 
