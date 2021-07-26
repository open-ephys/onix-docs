.. _breakout_overview:

Overview
#########################
The **ONIX Breakout Board** allows bench access to the IO provided by the
:ref:`pcie_host`.

.. figure:: /_static/images/breakout/breakout_1r5_callouts.jpg
    :align: center

    ONIX Breakout Board revision 1.5.

Features
-------------------------
The Breakout Board provides access to the following IO:

- 4x headstage port feed-throughs, each with a power switch
- 3x, passive, high-speed clock feed-throughs
- 12x passive, ESD-protected, analog feed-throughs.
- BNC, ribbon, or direct wire access to 12 analog inputs or outputs
- Ribbon cable or direct, wire-access to 8 digital outputs and 8 digital
  inputs. These are 5V compliant.
- `HARP bus <https://www.cf-hw.org/harp>`__ controller

Additionally, it has the following features:

- Lots of indication LEDs
- 6 buttons for marking experimental events for communication and programming.
- Rugged M6 and 1/4-20 mounting holes for both metric and imperial optical
  tables
- 19" rack compatibility
- Fully open-source gateware and made using an open-source FPGA toolchain
  (`yosys <http://www.clifford.at/yosys/>`__ & `nextpnr
  <https://github.com/YosysHQ/nextpnr>`__)

This board is behaves as if it was passive. It works in coordination with a
host board which determines its detailed functionality via its connectivity
with the breakout board along with the firmware running on the host. For every
host, all IO is carried through the following connections:

.. todo:: Image of right-angle cabling pinout

Refer to the host documentation for a detailed description of how each of these
signal lines are acquired.

.. note:: There may be more IO present on the breakout board than is available
    on a particular host board. For instance, :ref:`pcie_host` has two coaxial
    links, but the breakout board provides four. This is is by design. The breakout
    is compatible with all host configurations.

Gateware
-------------------------
The breakout board contains a `TinyFPGA BX
<https://tinyfpga.com/bx/guide.html>`__ (Lattice ICE40 breakout board) for
digital input serialization, digital output deserialization, interpreting user
input, and driving indication LEDs. The gateware can be found `here
<https://github.com/open-ephys/onix-breakout/tree/main/gateware>`__ and is
impelemented using an open-source toolchain (`Yosys
<http://www.clifford.at/yosys/>`__ and `NextPnR
<https://github.com/YosysHQ/nextpnr>`__).
