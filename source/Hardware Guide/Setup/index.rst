System Setup
==========================================

.. toctree::
    :maxdepth: 1

.. todo:: High level step by step setup and testing process.


1) Hardware list

Minimum:

- An acquisition computer
- PCIe Host
- Headstage or Miniscope

Additional devices:

- Breakout Board
- Commutator
- Lighthouses

2) Connections

Cables & connections:

.. image:: ../../_static/images/connections/connections.png
  :align: center

Commutator
- USB (computer) to micro-USB (commutator) cable, to power the commutator.

Digital and analog I/O:
- `High speed digital cable <https://multimedia.3m.com/mws/media/585365O/3mtm-shrunk-delta-ribbon-sdr-cable-assembly-ts2287.pdf?`_ to connect Host and Breakout Board

Headstages
- MMCX (Host) to MMCX (Breakout Board) - one cable for each headstage or clock in/output.
- SMA (Breakout Board) to SMA (Commutator)
- Tether: SMA (Commutator) to Hirose X.FL-PR-SMT1-2(80) X.FL coaxial socket (Headstage).
:ref: 'Making Coaxial Tethers'

If not using the Breakout Board, you can directly connect a headstage to the Host with a tether and an SMA to MMCX adapter.

Lighthouses
- Audio (Lighthouse A) to Audio (Lighthouse B) - to synchronise lighthouses (only necessary for V1)
- Power cables for lighthouses (x2)

3) Installing and Testing

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
