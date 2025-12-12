.. _pcie_host:

PCIe Host
=========================================
This device provides `PCIe
<https://en.wikipedia.org/wiki/PCI_Express>`__-based communication
with a single `ONIX FMC Host Module
<https://github.com/open-ephys/onix-fmc-host>`__ and allows
sub-millisecond closed-loop IO with the brain and auxiliary lab
equipment.

.. toctree::
    :maxdepth: 1
    :hidden:

    overview
    setup-windows
    updating-firmware
    multi-board-sync

:Design Repository: https://github.com/open-ephys/onix-fmc-host
:Compatibility: :ref:`headstage_64`,
                :ref:`headstage_neuropix1`, :ref:`miniscopes`
                :doc:`../Headstages/headstage-neuropix-1e`, 
                :doc:`../Headstages/headstage-neuropix-2e`,
                :doc:`../Headstages/headstage-rhs2116`
                
.. figure:: /_static/images/pcie-host/pcie-host_nereid_fmc-host-1r4.jpg
    :align: center
