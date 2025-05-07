.. _pcie_host_firmware_update:

.. toctree::
    :hidden:
    
Updating Firmware in Windows
########################################

#. If you have not done so already, follow the steps on the
   :ref:`Setup Guide for Windows <pcie_host_setup_windows>` page.

#. Download the latest :ref:`oni_repl_download` and unzip it. Navigate to this
   location using a console (e.g. PowerShell).

   .. note:: For a complete description of this program, have a look at its
        :ref:`usage guide <oni_repl>`

#. Verify your PCIe Host Hardware version by running ``oni-repl`` and typing "H"
   into the command prompt. This will print a list of all hubs in the current
   ONI context, one of which will be the PCIe Host.

   .. code-block:: console

        $ oni-repl.exe riffa 0
        ...
        ...
        ...
        >>> H

   .. figure:: /_static/images/pcie-host/oni-repl-host-hardware-version.png
        :align: center

#. Download the latest :ref:`pcie_host_image_download` for your hardware
   version. 

   .. warning::
         Make sure that the host firmware image you download matches the PCIe Host Hardware version
         you verified in the previous step. An incorrect firmware version will not report any error while updating but will cause failures during operation.

#. Download the :ref:`pcie_host_updater_download` utilities package and unzip
   it. Navigate to this folder using a console.

#. Run the ``oni_pcie_mode_change`` command to put the PCIe host into bootloader
   mode.

   .. code-block:: console

        $ oni_pcie_mode_change.exe
   
   .. figure:: /_static/images/pcie-host/oni-pcie-change-mode-to-bl.png
        :align: center

#. Open the Windows Device Manager by typing "device manager" into the windows
   search bar.Find the RIFFA device you are going to update in the device tree.
   Right click on the RIFFA device and select inactivate.

   .. figure:: /_static/images/pcie-host/device-manager-disable-riffa.png
        :align: center
        :width: 80%

#. Right click again and click activate

   .. figure:: /_static/images/pcie-host/device-manager-enable-riffa.png
        :align: center
        :width: 80%

   .. note::
        If prompted to do so, or if the device has a small yellow triangle icon
        next to it, you will need to reboot your computer to finish the
        process.

#. Return to the console and run the ``oni_pcie_flash_image`` command using the
   **.bin** file downloaded in step 4 and the index of the PCIe host device you
   want to update. If you only have a single PCIe Host board, index can be
   specified as 0 or omitted.

   .. code-block:: console

        $ oni_pcie_flash_image.exe <path to image.bin> [index]

   .. figure:: /_static/images/pcie-host/oni-pcie-flash-image.png
        :align: center

#. When the program completes, run ``oni_pcie_mode_change`` to put the PCIe
   host into normal mode.

   .. code-block:: console

        $ oni_pcie_mode_change.exe
   
   .. figure:: /_static/images/pcie-host/oni-pcie-change-mode-to-normal.png
        :align: center

#. Repeat steps 7 and 8 to reactivate the PCIe Host with the updated
   firmware.  

#. To verify the firmware update, repeat step 3. The firmware version of the
   PCIe Host should now match the one downloaded in step 4.
