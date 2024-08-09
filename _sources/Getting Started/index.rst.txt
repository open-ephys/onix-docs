.. |hw_logo| image:: /_static/noun_pcb.svg
  :height: 60

.. _getting_started:

.. toctree::
    :maxdepth: 1
    :hidden:

    whatisonix
    warnings

Getting Started
==========================================

Understanding the System
--------------------------------
- Read :ref:`'What is ONIX?' <what_is_onix>` for a high-level introduction to
  this hardware and how it differs from other neuroscience acquisition
  systems.
- Our :ref:`faq` contains answers to general questions about the system.
- See the :ref:`hardware_guide` for a description of each ONIX hardware component and decide which you will need.

.. note::
    To understand the underlying hardware specifications, check out the `ONI Hardware Specification <https://open-ephys.github.io/ONI/hw-spec/index.html>`_.

.. note::
    For developers who want to dig into the API, check out the `ONI API Documentation <https://open-ephys.github.io/ONI/api/index.html>`_.

Usage Warnings
--------------------------------

.. warning::

    Read :ref:`Usage Warnings<warnings>` before starting to work with the system to avoid causing damage to system components.

Setting up your system
--------------------------------

#. Check that you have all the necessary hardware. A full ONIX setup consists of:
    
   **Hardware**
    
   - :ref:`pcie_host`
   - Acquisition computer
   - :ref:`breakout`
   - ONI-compliant device (such as a :ref:`headstage <headstages>` or
     :ref:`miniscopes`)
   - :ref:`commutators`
   - 2x :ref:`lighthouse base stations <lighthouses>`
    

   **Cables** :ref:`(All cables are listed here)<cable_list>`.
   
   - PCIe host board to Breakout board (headstage link) cable (MMCX to MMCX)
   - PCIe host board to Breakout board (Digital and Analog I/O link) cable (SDR to
     SDR 26 POS)
   - Headstage Tethers, coaxial, 0.38 mm OD
   - Commutator power & data cable (USB A to Micro B)
   - Breakout board to Commutator cable (headstage link; SMA to SMA)
   - Lighthouse synchronization cable (3.5 mm Stereo Jack Plug to Plug)

#. Install the PCIe host board and configure the acquisition computer by
   following the :ref:`Setup Guide for Windows<pcie_host_setup_windows>`.
#. :ref:`Mount and connect the 3D-Tracking Lighthouses <lighthouse_setup>`
#. :ref:`Mount and connect the commutator <commutators>`
#. :ref:`Connect the Breakout Board to the PCIe host board <breakout_setup>`.
#. Connect a headstage, Miniscope V4 or other ONI compliant recording device by
   :ref:`following these steps <headstage_setup>`. Be sure to read :ref:`this
   page on the voltage supplied to the headstage <tether_voltage>` to prevent
   damaging your headstage.

Using ONIX
--------------------------------
Have a look at the :ref:`software_guide` page to explore
software options and for intefacing with ONIX hardware.
