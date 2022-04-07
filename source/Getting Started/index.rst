.. |hw_logo| image:: /_static/noun_pcb.svg
  :height: 60

.. _getting_started:

|hw_logo| Getting Started
==========================================

.. toctree::
    :maxdepth: 1
    :hidden:

    whatisonix

Understanding the system
--------------------------------
- Read :ref:`'What is ONIX?' <what_is_onix>` for a high-level introduction to
  this hardware and how it differs from classic neuroscience acquisition
  systems.
- Our :ref:`faq` contains answers to general questions about the system.
- See the :ref:`hardware_guide` for a description of each ONIX hardware component and decide which you will need.

Setting up ONIX
--------------------------------

1. Check that you have all the necessary hardware.

    A full ONIX setup consists of:

    **Devices**

    - PCIe host board
    - Acquisition computer
    - Breakout board
    - ONI-compliant device (such as a headstage or
      Miniscope V4)
    - Active commutator
    - 2 Lighthouse Base Stations

    **Cables**

    :ref:`(All cables are listed here)<connection_overview>`.

    - PCIe host board to Breakout board (headstage link) cable (MMCX to MMCX)
    - PCIe host board to Breakout board (Digital and Analog I/O link) cable (SDR to SDR 26 POS)
    - Headstage Tethers, coaxial, 0.38 mm OD
    - Commutator power & data cable (USB A to Micro B)
    - Breakout board to Commutator cable (headstage link)(SMA to SMA)
    - Lighthouse synchronization cable (3.5 mm Stereo Jack Plug to Plug)

    **A minimal setup will require:**

    - PCIe host board
    - Acquisition computer
    - ONI-compliant device (such as a headstage or Miniscope V4).
    - A coaxial tether (to connect the PCIe host board and headstage)

2. Install the PCIe host board and configure the acquisition computer by following the :ref:`pcie_host_setup_windows`.

3. Connect the remaining hardware using :ref:`system_setup`.

4. Test the installation. 

Using ONIX
--------------------------------

- ONIX uses Bonsai for data acquisition. See the :ref:`bonsai_gettingstarted` page to learn how to install Bonsai and use it to acquire from ONIX.
