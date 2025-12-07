.. _breakout_setup:

Breakout Board Guide
#########################

.. warning:: Always make sure the PC is powered off **before** connecting or disconnecting the Breakout Board. Neglecting to do this will damage the PCIe Host.

Setup
-------------------------
The Breakout Board provides access to signals to and from the PCIe host. Each
PCIe host is connected to a breakout board using the following connections:

#. Digital and analog I/O (Required for breakout board operation): A single
   shrunk delta ribbon (SDR) cable is used for all auxiliary IO and provide
   power to the Breakout Board.
#. Headstage links (Required for headstages): A single MMCX coaxial cable is
   used for each headstage port.
#. High speed clocks (Optional): A single MMCX caoxial cable is used for each
   clock signal
#. HARP (Optional): A 3.5mm audio jack
#. Configuration (Optional): Micro USB used to update the breakout gateware.

.. image:: /_static/images/breakout/breakout_host_connections_callouts.png
    :align: center
    :width: 60%

.. image:: /_static/images/breakout/bb_cables.jpg
    :align: center
    :width: 60%

Refer to the :ref:`pcie_host` documentation for a detailed description of how
each of these signal lines are acquired.

.. note:: There may be more IO present on the breakout board than is available
    on a particular host board. For instance, :ref:`pcie_host` has two coaxial
    links, but the breakout board provides four. This is is by design. The breakout
    is designed to be compatible with future host hardware.

Reset Button
________________________

There are two holes on the breakout board that allow access to the onboard FPGA reset button and status LED.
The reset hole is located just below the 'Digital Out' marking, and can be used to access the reset button on the onboard FPGA by inserting a thin wire or pin.
The onboard FPGA status can be inspected by looking into the status LED hole.

.. image:: /_static/images/breakout/breakout_reset.png
    :width: 50%
    :align: center


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
     reset the Breakout Board by pressing the onboard FPGA reset button (see above).

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
- If you are feeding the clock inputs/outputs from the controller through 
  the breakout board, make sure that the port number (0, 1, 2) on the breakout
  board matches the port number on the PCIe host. Older 3D printed versions of 
  the PCIe bracket label the clock ports as I\ :sub:`0`\, I\ :sub:`1`\, and O - 
  these should connect to the breakout in the following respective order: 0, 1, 2.
- Additional MMCX cables can be used to connect the optional clock IO ports
  on the PCIe host board to the clock ports on the breakout board. These
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
Buttons can be used to log various experimental events and turn on and off the
indication LEDs. The button state is sent with digital data to the PCIe Host.
Pressing a button sends a single event per change in button state. Holding a
button will not result in repeat presses as a keyboard would. Each button sets
one bit in a 6-bit word. For exampled

:000001:    Button 0 pressed (integer value 1)
:100001:    Button 0 and button 5 pressed (integer value 33)
:111111:    All buttons pressed (integer value 63)

Additional, pressing button 0  will toggle indication LED power. This allows
all LEDs to be completely turned off for light-sensitive experiments.

.. figure:: /_static/images/breakout/buttons_labelled.png
    :width: 60%
    :align: center


    Numbers show integer value transmitted to host from pressing each. The
    first button also controls the illumination state of the indication LEDs on
    the breakout board.

Gateware
-------------------------
The breakout board contains a `TinyFPGA BX <https://github.com/tinyfpga/TinyFPGA-BX>`__ (Lattice ICE40 breakout board) for
digital input serialization, digital output deserialization, interpreting user
input, and driving indication LEDs. The `breakout board gateware
<https://github.com/open-ephys/onix-breakout/tree/main/gateware>`__ is
implemented using an open-source toolchain (`Yosys
<https://yosyshq.net/yosys/>`__ and `NextPnR
<https://github.com/YosysHQ/nextpnr>`__).

Follow the instructions in :ref:`Updating Breakout Board Firmware <breakout_firmware_update>` to update the breakout board firmware to the latest version.