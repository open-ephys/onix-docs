.. _pcie_host_setup_windows:

Setup Guide for Windows
########################################

Insert the PCIe Host Module
---------------------------------------
#. Power off the computer.

#. Plug the PCIe host board into an available PCIe slot

   .. note:: You do not need to plug the ATX power supply into connector on
        the board (although doing so won't hurt). The PCIe slot itself provides
        adequate power to operate the host board.

#. Boot the computer.

#. The RGB LED in the center of the module should be blue.

   .. note:: The RGB LED has three color states.

        - Blue: Ready to go.
        - Yellow: Acquisition stopped.
        - Pink: Acquisition running.

Put Windows In Testing Mode
---------------------------------------

.. note:: As of this writing, the ONIX driver is not digitally signed by
    Microsoft, but in a developer testing phase. Following the conclusion of the
    beta-test period, we will complete this process and the following steps
    will not be required.

#. Download the :download:`OpenEphysTestDriver.cer
   <../../_static/downloads/OpenEphysTestDriver.cer>` testing certificate and double
   click it.
#. On the dialog, select **Install Certificate**.

   .. figure:: /_static/pcie-host-windows/install-certificate.png
        :align: left

#. It is recommended to select **Current User** certificate storage option.

   .. figure:: /_static/pcie-host-windows/certificate-import-current-user.png
        :align: left

#. For ease of management, it is recommended to manually select a certificate
   storage and chose **Personal**.

   .. figure:: /_static/pcie-host-windows/certificate-import-personal-storage.png
        :align: left

#. Open the Windows Start Menu and type **cmd** to find the command prompt
   application. Right click it and chose **Run as Administrator**.

   .. figure:: /_static/pcie-host-windows/cmd-run-as-admin.png
        :align: left

#. Execute the following command: ``bcdedit /set testsigning on``

   .. figure:: /_static/pcie-host-windows/windows-test-mode-command.png
        :align: left

#. Restart the computer.

   .. note:: A regular reboot ('restart') is required. A complete power cycle (turning the PC off completely) may not set
        the option.

#. You should see now some text at the bottom right of the Desktop indicating
   that Windows is operating in testing mode:

   .. figure:: /_static/pcie-host-windows/windows-test-mode-text.png
        :align: left

   .. note:: The computer will keep the test state until you run ``bcdedit /set
        testsigning off`` in an administrator command prompt again and reboot the
        computer

Install C++ Runtime
---------------------------------------
Windows does not ship with a C++ runtime. Before using ONIX on windows, you
will need to install `Microsoft Visual C++ Redistributable for Visual Studio
2015, 2017 and 2019 <https://aka.ms/vs/16/release/vc_redist.x64.exe>`__.

Install Device Driver
---------------------------------------

.. warning:: Pre-built drivers target 64-bit Windows 10. Other targets will
    need to be compiled from source.

#. Download :download:`riffa driver
   <../../_static/downloads/riffa-driver.zip>` and unzip the archive.
#. Open the folder and right right click the **riffa.inf** file.
   Select **install** from the context menu.
#. Open the start menu and type **device manager** and click to open. You shoul
   see **RIFFA** in the device tree.

   .. figure:: /_static/pcie-host-windows/package-manager-riffa.png
       :align: left

Install ONIX Bonsai Library
---------------------------------------
#. If you don't have Bonsai on your computer, visit https://bonsai-rx.org/ and
   install the latest release.
#. Open Bonsai. At the start menu, select **Manage Packages**.

   .. figure:: /_static/pcie-host-windows/bonsai-start-menu.png
       :align: left

#. Select **Community Packages** as the package source.
#. Search for **Bonsai.ONIX**.
#. Install **Bonsai.ONIX.Design**. This packages will install both the core
   library and visualization tools.
#. Have a look at the :ref:`bonsai_onixref` for usage instructions
   and example scripts.
