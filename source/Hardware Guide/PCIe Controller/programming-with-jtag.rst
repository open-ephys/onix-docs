:orphan:

.. _pcie_controller_program_over_jtag:

.. toctree::
    :hidden:
    
Programming a Blank PCIe Controller (Windows)
##############################################

#. If you have not done so already, follow the steps on the :ref:`Setup Guide for Windows <pcie_controller_setup_windows>` page.

#. Download and install Vivado Lab Edition here: https://www.xilinx.com/support/download.html.

#. Download **PCIe Controller Bootloader**.

#. Download the most recent :ref:`pcie_controller_image_download` that is compatible with your hardware

#. Open Vivado and click open Hardware manager on splash screen

#. Clock on "Tools" and select "Generate Memory Configuration File..."

   .. figure:: /_static/images/pcie-controller/vivado-generate-mem-config.PNG
        :align: center
        :width: 50%

#. Enter the following values into the form and click OK. This will generate an
   .mcs file that can be flashed onto your PCIe Controller.

   - Format: MCS
   - Memory part: mt25ql128-spi-x1_x2_x4
   - Interface: SPIx4
   - Load bitstream files: enabled
   - Select the two bitfiles ("\*.bit"). Bootloader at address 0x0000000,
     normal image at address 0x0800000. Both with direction "up".
   - Every other option disabled

   .. figure:: /_static/images/pcie-controller/mcs-configuration.PNG
        :align: center

   .. note:: To add the second, bit file, click the "plus" icon on the first
      row in the table under Load Bitstream files (red in image).

#. After generating the mcs file, plug in a `Xilinx Platform Cable
   II <https://www.xilinx.com/products/boards-and-kits/hw-usb-ii-g.html>`__ to a
   USB port on your computer. Then plug the other end into the JTAG connector
   (red box in figure) on the PCIe Controller.

   .. figure:: /_static/images/pcie-controller/nereid-jtag-programming.png
        :align: center

   .. note:: If the Controller is not already plugged into a PCIe slot, do so
      now and be sure to also be sure to plug in an ATX power connection (green
      box in figure).

#. In the Hardware Manager, click Open Target and select "Auto Connect" to find
   the programmer and scan for the FPGA on the JTAG chain.

   .. figure:: /_static/images/pcie-controller/auto-connect.PNG
        :align: center
        :width: 70%

#. Once the FPGA is enumerated in the hardware manager, right click it and
   select "Add Configuration Memory Device..."

   .. figure:: /_static/images/pcie-controller/add-config-memory-device.PNG
        :align: center
        :width: 60%

#. Search for "mt25ql128-spi-x1_x2_x4" in the "Memory Device" field and add it.
   Add the path to the .mcs file generated previously in the "Configuration
   file" field. Click OK to flash the PCIe Controller.

   .. figure:: /_static/images/pcie-controller/program-with-mcs.PNG
        :align: center
        :width: 50%

#. Power off the computer and then restart.

#. Open the Device Manager from the Windows Search Bar and you
   should see a RIFFA in there.

#. After this, you will be able to quickly upgrade your PCIe Controller over PCIe by
   following the steps on the **pcie_controller_gateware_drivers** page.
