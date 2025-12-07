.. _breakout:

Breakout Board
==========================================
This device provides user-facing access for headstage, miniscope, and auxiliary
data IO.

.. toctree::
    :maxdepth: 1
    :hidden:

    setup
    updating-breakout-firmware

:Design Repository: https://github.com/open-ephys/onix-breakout
:Compatibility: :ref:`pcie_host`, :ref:`headstage_64`,
                :ref:`headstage_neuropix1`, :ref:`miniscopes`,
                :doc:`../Headstages/headstage-neuropix-1e`, 
                :doc:`../Headstages/headstage-neuropix-2e`,
                :doc:`../Headstages/headstage-rhs2116`


.. _breakout_overview:

Overview
#########################
The **ONIX Breakout Board** allows bench access to the IO provided by the
:ref:`pcie_host`.

.. figure:: /_static/images/breakout/breakout_edited_callouts.png
    :align: center

    ONIX Breakout Board v1.5.

Features
-------------------------
The Breakout Board provides access to the following IO:

- 2x headstage port feed-throughs, each with a power switch.
- 3x, passive, high-speed clock feed-throughs. 
- 12x passive, ESD-protected, analog feed-throughs.
- BNC, ribbon, or direct wire access to 12 analog inputs or outputs.
- Ribbon cable or direct, wire-access to 8 digital outputs and 8 digital
  inputs. These are 5V compliant.
- `HARP bus <https://www.cf-hw.org/harp>`__ controller

Additionally, it has the following features:

- Lots of indication LEDs.
- 6 buttons for marking experimental events for or triggering software actions.
- Rugged M6 and 1/4-20 mounting holes for both metric and imperial optical
  tables.
- 19" rack compatibility.
- Fully open-source gateware and made using an open-source FPGA toolchain
  (`yosys <https://yosyshq.net/yosys/>`__ & `nextpnr
  <https://github.com/YosysHQ/nextpnr>`__).
