.. _warnings:

.. toctree::
    :hidden:

Usage Warnings
==========================================

.. warning::  Improper setup and usage can cause damage to system components.

    - Read the following warnings before starting to work with your system. These
      are crucial aspects to consider during setup and usage that are included in
      the documentation but are listed here for your convenience.
    - Read the complete documentation carefully to understand how the system works
      and refer back to these warnings before using it.

Breakout Board
--------------------------------

.. warning:: Connecting or disconnecting the :ref:`breakout` while the PC is on
    can damage to the :ref:`pcie_host`. For more details, see
    :ref:`breakout_setup`. **Power off the PC before connecting/disconnecting the
    breakout board.**

Headstage Voltages
--------------------------------

.. warning::
   **Ensure each headstage is configured with the correct voltage.** Although
   headstages are quite tolerate of over-voltage and under-voltage conditions,
   they are only guaranteed to function within a specified range.  When using
   long and/or thin tethers, the voltage drop across the cable can become
   significant. For more details, see :ref:`tether_voltage`.


