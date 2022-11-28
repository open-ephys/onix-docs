.. _pcie_host_firmware_update:

Updating Firmware in Windows
########################################

#. If you have not done so already, follow the steps on the :ref:`pcie_host_setup_windows` page.

#. Download the latest :ref:`oni_repl_download` and unzip it. Navigate to this
   location using a console (e.g. PowerShell).

#. Verify your PCIe Host Hardware version by running `oni-repl` and typing `H`
   into the command prompt. This will print a list of all hubs in the current
   ONI context, one of which will be the PCIe Host.

   .. code-block:: console

        $ oni-repl.exe riffa 0

   .. figure:: /_static/images/pcie-host/oni-repl-host-hardware-version.png
        :align: center

#. Download the latest :ref:`pcie_host_image_download` hardware version and unzip.

   .. warning::
        Make sure that the host firware matches the hardware version from the
        last step or the update will not work properly.

#. Download the :ref:`pcie_host_updater_download` utilities package and unzip
   it. Navigate to this folder using a console.

#. Run `onix-pcie-host-change-mode` to put the PCIe host into bootloader mode.

   .. code-block:: console

        $ onix-pcie-host-change-mode.exe
   
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
        If the devie has a smale yellow triangle icon next to it, you will need
        to reboot your computer to finish the process.

#. Return to the console and run the `onix-pcie-host-update` program using the
   **.bin** file downloaded in step 4 and the index of the PCIe host device
   you want to update.

   .. code-block:: console

        $ onix-pcie-host-update.exe <path to image.bin> [index]

   .. figure:: /_static/images/pcie-host/oni-pcie-flash-image.png
        :align: center

#. When the program completes, `onix-pcie-host-change-mode` to put the PCIe
   host into normal mode.

   .. code-block:: console

        $ onix-pcie-host-change-mode.exe
   
   .. figure:: /_static/images/pcie-host/oni-pcie-change-mode-to-normal.png
        :align: center

#. Repeat steps 7 and 8 to reactivate the PCIe Host with the updated
   firmware.  
