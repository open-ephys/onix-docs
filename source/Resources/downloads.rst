.. _downloads:

Downloads
=============================================

.. _oni_repl_download:

`oni-repl` Console Application
----------------------------------------------

.. note:: Please see the :ref:`oni-repl guide <oni_repl>` for instructions on
    how to use this software. When using mac or linux, you will need to compile
    from source. See compilation instructions in the `Makefile
    <https://github.com/open-ephys/liboni/blob/main/api/liboni/oni-repl/Makefile>`__.

.. list-table::
   :widths: 15 25 60
   :header-rows: 1

   * - Version
     - Release Date
     - Release Notes
   * - :download:`1.1.0 <../_static/downloads/onix-software-releases/oni-repl-x64_v1.1.0.zip>`
     - 2025.06.25
     - Fixes to hardware reset behavior. Addition of several command line
       switches and options in the REPL.

.. _riffa_driver_download:

RIFFA PCIe Driver
----------------------------------------------

.. note:: Please see :ref:`Install RIFFA PCIe Driver <install_riffa>` 
    for instructions on how to use this file. When
    using mac or linux, you will need to compile from `source
    <https://github.com/open-ephys/liboni>`__.

.. list-table::
   :widths: 15 25 60
   :header-rows: 1

   * - Version
     - Release Date
     - Release Notes
   * - :download:`6.1.0.2 <../_static/downloads/onix-driver-releases/riffa/riffa-x64_v6.1.0.2.zip>`
     - 2024.03.14
     - Fix race condition in the RIFFA kernel driver for windows.


PCIe Host Gateware
----------------------------------------------

.. note:: Please see :ref:`Updating PCIe Host Gateware
   <pcie_host_gateware_update>` for instructions on how to use these files.
   When using mac or linux, you will need to compile the Updater software from
   `source <https://github.com/open-ephys/onix-gateware-field-updaters>`__.

.. _pcie_host_updater_download:

PCIe Host Upload Tool
______________________________________________
Software for uploading PCIe Host gateware to PCIe Host hardware.

.. list-table::
   :widths: 15 25 60
   :header-rows: 1

   * - Version
     - Release Date
     - Release Notes
   * - :download:`1.0.0 <../_static/downloads/onix-software-releases/onix-pcie-host-flash-tools-x64_v1.0.0.zip>`
     - 2022.11.27
     - Initial release.

.. _pcie_host_image_download:

PCIe Host Gateware Images
______________________________________________

.. warning::
   Make sure that the host gateware image you download matches the PCIe Host
   Hardware version you have as shown in the table below. An incorrect gateware
   version will not report any error while updating but will cause failures
   during operation.

.. table::
    :widths: 30 70

    +-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
    | | PCIe Host Hardware version                                      | | Latest PCIe Host                                                                                             |
    | | per :ref:`oni-repl <controller_version_difference>`             | | gateware version                                                                                             |
    +===================================================================+================================================================================================================+
    | Hardware Revision 1.4                                             | Deprecated. Please :ref:`get in touch <support>` so we can assist you.                                         |
    +-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
    | Hardware Revision 1.5                                             | | :download:`Gateware version 2.0D <../_static/downloads/onix-gateware-images/onix-host-v2.0-update-revD.bin>` |
    |                                                                   | | Requires OpenEphys.Onix1 v0.6+ or Open Ephys GUI v1.0+                                                       |
    +-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
    | Hardware Revision 1.6                                             | | :download:`Gateware version 2.0F <../_static/downloads/onix-gateware-images/onix-host-v2.0-update-revF.bin>` |
    |                                                                   | | Requires OpenEphys.Onix1 v0.6+ or Open Ephys GUI v1.0+                                                       |
    +-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+


.. .. list-table::
..    :widths: 15 25 60
..    :header-rows: 1
..
..    * - Version
..      - Release Date
..      - Release Notes
..    * - :download:`0.6 <./_static/downloads/onix-gateware-images/pcie-host-1r4/onix-pcie-host-1r4_v0.6.bin>`
..      - 2022.11.27
..      - Remove unnecessary breakout board PLL reset during context initialization which could cause LEDs to turn off.


Breakout Board Gateware
----------------------------------------------

.. note:: Please see :ref:`Updating Breakout Board Gateware <breakout_gateware_update>`
    for instructions on how to use these files. When
    using mac or linux, you will need to compile from `source
    <https://github.com/open-ephys/onix-gateware-field-updaters>`__.

.. _breakout_updater_download:

Breakout Board Upload Tool
______________________________________________
Software for uploading Breakout Board gateware to Breakout Board hardware.

.. list-table::
   :widths: 15 25 60
   :header-rows: 1

   * - Version
     - Release Date
     - Release Notes
   * - :download:`1.0.0 <../_static/downloads/onix-software-releases/tinyprog.zip>`
     - 2024.07.05
     - Initial release.

.. _breakout_image_download:

Breakout Board Gateware Images
______________________________________________

.. warning::
   Make sure that the breakout board gateware image you download matches the
   breakout board hardware version you have as shown in the table below. An
   incorrect gateware version will not report any error while updating but will
   cause failures during operation.

.. table::
    :widths: 40 60

    +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
    | | Breakout Board Hardware version                            | | Latest Breakout Board                                                                                     |
    | | per :ref:`visual inspection <breakout_version_difference>` | | gateware version                                                                                          |
    +==============================================================+=============================================================================================================+
    | Hardware Revision 1.5  (four headstage ports)                | :download:`Gateware version 1.3 <../_static/downloads/onix-gateware-images/breakout-rev1.5-gw1.3.bin>`      |
    +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
    | Hardware Revision 1.6  (two headstage ports)                 | :download:`Gateware version 1.3 <../_static/downloads/onix-gateware-images/breakout-rev1.6-gw1.3.bin>`      |
    +--------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+

