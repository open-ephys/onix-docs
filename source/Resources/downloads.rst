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

.. list-table:: oni-repl Windows downloads
   :widths: 15 25 60
   :header-rows: 1

   * - Version
     - Release Date
     - Release Notes
   * - :download:`1.0.0 <../_static/downloads/onix-software-releases/oni-repl-x64_v1.0.0.zip>`
     - 2022.11.27
     - Initial release.

.. _pcie_host_updater_download:

PCIe Host Updater
----------------------------------------------

.. note:: Please see :ref:`Updating PCIe Host Firmware
    <pcie_host_firmware_update>` for instructions on how to use these files. When
    using mac or linux, you will need to compile from `source
    <https://github.com/open-ephys/onix-gateware-field-updaters>`__.

.. list-table:: PCIe Host update tools
   :widths: 15 25 60
   :header-rows: 1

   * - Version
     - Release Date
     - Release Notes
   * - :download:`1.0.0 <../_static/downloads/onix-software-releases/onix-pcie-host-flash-tools-x64_v1.0.0.zip>`
     - 2022.11.27
     - Initial release.

-----------------

.. _breakout_updater_download:

Breakout Board Updater
----------------------------------------------

.. note:: Please see :ref:`Updating Breakout Board Firmware
    <breakout_firmware_update>` for instructions on how to use these files.

.. list-table:: Breakout Board update tools
   :widths: 15 25 60
   :header-rows: 1

   * - Version
     - Release Date
     - Release Notes
   * - :download:`1.0.0 <../_static/downloads/onix-software-releases/tinyprog.zip>`
     - 2024.07.05
     - Initial release.

-----------------

.. _riffa_driver_download:

RIFFA Device Driver
----------------------------------------------

.. note:: Please see :ref:`Updating PCIe Host Firmware
    <pcie_host_firmware_update>` for instructions on how to use these files. When
    using mac or linux, you will need to compile from `source
    <https://github.com/open-ephys/liboni>`__.

.. list-table:: RIFFA PCIe driver
   :widths: 15 25 60
   :header-rows: 1

   * - Version
     - Release Date
     - Release Notes
   * - :download:`6.1.0.2 <../_static/downloads/onix-driver-releases/riffa/riffa-x64_v6.1.0.2.zip>`
     - 2024.03.14
     - Fix race condition in the RIFFA kernel driver for windows.

-----------------

.. _pcie_host_image_download:

PCIe Host Firmware
----------------------------------------------
.. note:: Please see :ref:`Updating PCIe Host Firmware
    <pcie_host_firmware_update>` for instructions on how to use these files.

.. warning::
      Make sure that the host firmware image you download matches the PCIe Host Hardware version you have
      as shown in the table below. An incorrect firmware version will not report any error while updating but will cause failures during operation.

.. table::
    :widths: 50 50

    +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
    |            PCIe Host Hardware version                 |                            PCIe Host Firmware latest version                                                |
    |               as reported by `oni-repl`               |                                   to download and update                                                    |
    +=======================================================+=============================================================================================================+
    | Hardware Revision 1.4                                 | Deprecated. Please :ref:`get in touch <support>` so we can assist you.                                      |
    +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
    | Hardware Revision 1.5                                 | :download:`Firmware version 1.1D <../_static/downloads/onix-gateware-images/onix-host-v1.1-update-revD.bin>`|
    +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
    | Hardware Revision 1.6                                 | :download:`Firmware version 1.1F <../_static/downloads/onix-gateware-images/onix-host-v1.1-update-revF.bin>`|
    +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+


.. .. list-table:: PCIe Host Revision 1.4 firmware images
..    :widths: 15 25 60
..    :header-rows: 1
.. 
..    * - Version
..      - Release Date
..      - Release Notes
..    * - :download:`0.6 <./_static/downloads/onix-gateware-images/pcie-host-1r4/onix-pcie-host-1r4_v0.6.bin>`
..      - 2022.11.27
..      - Remove unnecessary breakout board PLL reset during context initialization which could cause LEDs to turn off.
 

.. _breakout_image_download:

Breakout Board Firmware
----------------------------------------------
.. note:: Please see :ref:`Updating Breakout Board Firmware
    <breakout_firmware_update>` for instructions on how to use these files.

.. warning::
      Make sure that the breakout board firmware image you download matches the breakout board hardware version you have
      as shown in the table below. An incorrect firmware version will not report any error while updating but will cause failures during operation.

.. table::
    :widths: 50 50

    +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
    |            Breakout Board Hardware version            |                             Breakout Board Firmware latest version                                          |
    |                 as per product specs                  |                                   to download and update                                                    |
    +=======================================================+=============================================================================================================+
    | Hardware Revision 1.5  (four headstage ports)         | :download:`Firmware version 1.3 <../_static/downloads/onix-gateware-images/breakout-rev1.5-fw1.3.bin>`      |
    +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
    | Hardware Revision 1.6  (two headstage ports)          | :download:`Firmware version 1.3 <../_static/downloads/onix-gateware-images/breakout-rev1.6-fw1.3.bin>`      |
    +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+

