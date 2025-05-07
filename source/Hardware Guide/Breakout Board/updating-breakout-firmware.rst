.. _breakout_firmware_update:

.. toctree::
    :hidden:
    
Updating Breakout Board Firmware in Windows
###############################################

.. warning::
     Connecting or disconnecting the breakout board while the PC is on causes damage to the FMChost.
   
#. Power off the PC to which the breakout board is connected.

#. Disconnect the breakout board from the PC by disconnecting the digital and analog I/O grey SDR cable.

#. Connect a USB-microUSB from the PC you will use to perform the firmware update to the Config port on the side of the breakout board.

#. Verify the Breakout Board version by looking at the specifications on the product.

   .. figure:: /_static/images/breakout/breakout_1r5_fw.png
        :align: center
        :width: 60%

        Breakout Board version 1.5 has four headstage ports (only two are enabled).

   .. figure:: /_static/images/breakout/breakout_1r6_fw.png
        :align: center
        :width: 60%

        Breakout Board version 1.6 has two headstage ports.

#. Download the latest :ref:`firmware image <breakout_image_download>` for your hardware version. 

   .. warning::
         Make sure that the host firmware image you download matches the Breakout Board hardware version
         you verified in the previous step. An incorrect firmware version will not report any error while updating but will cause failures during operation.

#. Download the :ref:`breakout_updater_download` utilities package and unzip
   it. Navigate to this folder using a console. Place the firmware image you downloaded in the previous step in the same folder.

#. Press the onboard FPGA reset button (using a thin tool that fits the reset hole) to put the device into bootloader mode. The onboard FPGA status LED will breathe to indicate it is ready to be programmed.

   .. figure:: /_static/images/breakout/tinyfpga_breathing.gif
        :align: center
        :width: 40%

#. From the console, use the following command with the correct name of the firmware image you downloaded to program the device: 

   .. code-block:: console

        $ tinyprog.exe -p breakout_firmware_image_filename.bit

#. Check that the breakout board firmware was programmed successfully

   .. figure:: /_static/images/breakout/tinyprog_success.jpg
        :align: center
        :width: 80%

#. Disconnect the USB-microUSB cable from the breakout board

#. Power off the PC to which the breakout board will be connected.

#. Connect the breakout board to the PC using the digital and analog I/O grey SDR cable, and any necessary headstage links as per the :ref:`setup guide <breakout_setup>`.

.. #. Test the breakout board works by using the DigitalIO node to test communication from the board by using the buttons and the AnalogIO to test communication to the board by toggling the configuration between input and output.