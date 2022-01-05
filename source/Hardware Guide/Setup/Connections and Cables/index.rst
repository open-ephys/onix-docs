.. _connection_overview:

Cables and Connections
############################################

This page is meant to help you understand the various connectors and data links in the ONIX hardware.

.. image:: ../../_static/images/connections/connections.svg
  :align: center

(not shown: USB cable connecting computer to commutator)

Commutator link
************************

* Computer (USB) to commutator (micro-USB) cable, to power the commutator & provide it with 3D tracking data.

Digital and Analog I/O
************************

* :ref:`High speed digital cable <https://multimedia.3m.com/mws/media/585365O/3mtm-shrunk-delta-ribbon-sdr-cable-assembly-ts2287.pdf>`_ to connect Host and Breakout Board.

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

* Audio (Lighthouse A) to Audio (Lighthouse B) - to synchronise lighthouses (only necessary for V1 Basestations)
* Power cables for lighthouses (x2, provided with lighthouses)
