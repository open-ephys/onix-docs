.. _breakout_setup:

Setup
#########################

.. image:: /_static/images/breakout/bb_cables.jpg
    :align: center
    :width: 60%

|
1. Connect the Breakout Board Digital and Analog I/O to the PCIe host board.

    Use the SDR to SDR 26 POS cable to connect the Breakout Board to the PCIe host board. Though one end of this cable is marked with 'camera', the cable is symmetrical for our purposes, so it can be connected in either direction.

    .. image:: /_static/images/connections/breakout_IO_cable.jpg
      :width: 50%
      :align: center

2. For each headstage or other measurement device, form a headstage line between the Breakout Board and the PCIe host board.

    Use the MMCX to MMCX cable to connect the from PCIe host board to the breakout board. Use one line for each hub/headstage. Make sure that you are using the same port everywhere; i.e. port 'A' on the PCIe host board, the side of the Breakout Board, and the face of the Breakout Board.

    The same cable type can be used to connect the clock in/output on the PCIe host board to the clock in/output on the breakout board.

    .. image:: /_static/images/connections/MMCX_cable.jpg
        :width: 50%
        :align: center

    .. warning::
      See :ref:`here <mmcx_cable>` how to connect and remove MMCX cables without damaging the connector.

3. Reset the board

    If the lights on the Breakout Board turn off unexpectedly, you can reset the Breakout Board by inserting a thin wire into the small hole just below the 'Digital Out' marking.

4. Update Firmware

    If the Open Ephys team have provided you with an updated firmware file for the Breakout Board, the micro-USB port on the Breakout Board (labelled 'config') can be used to update the firmware on the board.
