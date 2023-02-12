.. _breakout_setup:

Breakout Board Guide
#########################

Setup
-------------------------
The Breakout Board provides easy access to signals to and from the PCIe host.
Each PCIe host can be connected to its own breakout board through  the
following connections:

#. Digital and Analog I/O: A single shrunk delta ribbon (SDR) cable is used for
   all auxliary IO and providew power to the Breakout Board.
#. Headstage links: A single MMCX coaxial cable is used for each headstage port.
#. High speed Clock A single MMCX caoxial cable is used for each clock signal.

.. image:: /_static/images/breakout/bb_cables.jpg
    :align: center
    :width: 60%

Refer to the :ref:`pcie_host` documentation for a detailed description of how
each of these signal lines are acquired.

.. note:: There may be more IO present on the breakout board than is available
    on a particular host board. For instance, :ref:`pcie_host` has two coaxial
    links, but the breakout board provides four. This is is by design. The breakout
    is designed to be compatible with future host hardware.

SDR Cable
________________________
Plug in the SDR cable for analog and digital I/O.

.. image:: /_static/images/connections/breakout_IO_cable.jpg
    :width: 50%
    :align: center

- Use the SDR to SDR 26 POS cable to connect the Breakout Board to the PCIe
  host board.
- Though one end of this cable is marked with 'camera', the cable is
  symmetrical for our purposes, so it can be connected in either direction.
- The Breakout Board will power on soon after the SDR cable connected to an
  active host

  .. attention:: Some boards have a bug in the power on sequence that means a
     reset is required before the board will work. This has been fixed in later
     revisions. If the RGB LEDs remain off after plugging in the SDR cable,
     reset the Breakout Board by inserting a thin wire or screw driver into the
     small hole just below the 'Digital Out' marking to reset the onboard FPGA.

     .. image:: /_static/images/breakout/reset_button.png
        :width: 50%
        :align: center

MMCX Cables
________________________
Plug in MMCX coaxial connections for headstage ports and clock signals.

.. image:: /_static/images/connections/MMCX_cable.jpg
   :width: 50%
   :align: center

- Use the MMCX to MMCX cable to connect a headstage port on the
  :ref:`pcie_host` to the breakout board. A single cable is required for
  each headstage port.
- Make sure that port letter (A, B, C, D) on the breakout matches the port
  letter on the PCIe host.
- Additional MMCX cables can be used to connect the optional clock IO ports
  on the PCIe host board to the clock ports on the breakout board.  These
  are passive, 50-ohm transmission lines so the order does not matter.

.. warning:: The MMCX connectors can be damaged if they are removed
  improperly. See :ref:`this link <mmcx_cable>` for information on how to
  connect and remove MMCX cables without damaging the connector.

LEDs
_________________________
RGB LEDs indicate various port states, signal directions, digital signals, and
acquisition states, etc. The following diagrams provide definitions for each
LED color on the breakout board.

.. figure:: /_static/images/breakout/rgb-leds_callouts.png
    :width: 100%
    :align: center

    Indication LED legend. Half-filled circles indicate a flashing LED. An
    error status on a headstage port indicates a loss of lock during
    acquisition. The headstage connection must be re-established and
    acquisition restarted.

Buttons
_________________________

.. todo:: Document

Gateware
-------------------------
The breakout board contains a `TinyFPGA BX
<https://tinyfpga.com/bx/guide.html>`__ (Lattice ICE40 breakout board) for
digital input serialization, digital output deserialization, interpreting user
input, and driving indication LEDs. The `breakout board gateware
<https://github.com/open-ephys/onix-breakout/tree/main/gateware>`__ is
impelemented using an open-source toolchain (`Yosys
<http://www.clifford.at/yosys/>`__ and `NextPnR
<https://github.com/YosysHQ/nextpnr>`__).


Updating the Gateware
_________________________
If Open Ephys team have provided you with an updated firmware file for the
Breakout Board, the micro-USB port on the Breakout Board (labelled 'config')
can be used to update the firmware on the board.

.. todo:: Link and instructions
