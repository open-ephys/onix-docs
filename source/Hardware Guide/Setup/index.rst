.. _system_setup:

System Setup
==========================================

.. toctree::
    :maxdepth: 2


Hardware list
############################################

Minimum:

- Acquisition computer
- PCIe Host
- ONI-compliant device (e.g. Headstage/ Miniscope V4)

Additional devices:

- Breakout Board
- Commutator
- Lighthouses
- Adapters and EIBs

Cables and Connections
############################################

.. image:: ../../_static/images/connections/connections.png
  :align: center

Commutator link
************************

* Computer (USB) to commutator (micro-USB) cable, to power the commutator & provide it with 3D tracking data.

Digital and Analog I/O
************************

* :ref:`High speed digital cable <https://multimedia.3m.com/mws/media/585365O/3mtm-shrunk-delta-ribbon-sdr-cable-assembly-ts2287.pdf`_ to connect Host and Breakout Board.

Headstage Link
************************
The headstage link can be formed directly with the host PCIe board, or via a commutator and/or breakout board.

Connectors used for headstage link:

* 64-channel headstage, npix headstage and miniscope: Hirose X.FL-PR-SMT1-2(80) X.FL coaxial socket connector.
* PCIe host board: MMCX connectors
* Breakout board: MMCX connectors (to link to PCIe host) & SMA connectors (to link to commutator or headstage).
* Commutator: SMA connectors to link to both breakout board and headstage.

Example configurations and required cables:

- Directly from headstage (*Hirose X.FL-PR-SMT1-2(80) X.FL coaxial socket*) to PCIe host board (*MMCX*), using a coaxial tether (:ref:'Making Coaxial Tethers') and an SMA to MMCX adapter.

- From headstage (*Hirose X.FL-PR-SMT1-2(80) X.FL coaxial socket*) to breakout board (*SMA*), then from breakout board (*MMCX*) to PCIe host board (*MMCX*).

- From headstage (*Hirose X.FL-PR-SMT1-2(80) X.FL coaxial socket*) to commutator (*SMA*), from commutator (*SMA*) to breakout board (*SMA*), then from breakout board (*MMCX*) to PCIe host board (*MMCX*).

- From headstage (*Hirose X.FL-PR-SMT1-2(80) X.FL coaxial socket*) to commutator (*SMA*), from commutator (*SMA*) to PCIe host board (*MMCX*).

- Tether: SMA (Commutator) to Hirose X.FL-PR-SMT1-2(80) X.FL coaxial socket (Headstage). :ref: 'Making Coaxial Tethers'

Lighthouses
************************

- Audio (Lighthouse A) to Audio (Lighthouse B) - to synchronise lighthouses (only necessary for V1 Basestations)
- Power cables for lighthouses (x2, provided with lighthouses)

Installing and Testing
############################################

- Install the PCIe board in the PC (ref to guide here)
- Mount 2 Base Station Lighthouses over the setup (height range)
-- Connect their power cables
-- Set one to A and one to B
-- Connect them using an audio to audio cable to synchronise them.
- Mount the active commutator above the setup
-- Power it from the computer using a USB to micro-USB cable
-- Test in Bonsai?
- Connect the Breakout Board to the Host using the high-speed digital cable
-- Test Digital IO
-- Test Buttons
-- Test Analog IO
- Connect headstages either directly to host or through Breakout Board
-- Check link
-- Testing/ checking depending on device
