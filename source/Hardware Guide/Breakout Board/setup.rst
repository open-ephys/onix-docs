.. _breakout_setup:

Setup
#########################

The Breakout Board must be connected to the PCIe host. Each headstage or other hub requires its own line, and there is a separate Digital & Analog I/O cable:

.. image:: /_static/images/breakout/bb_cables.jpg
    :align: center
    :width: 70%


Digital and Analog I/O
----------------------------
Use the SDR to SDR 26 POS cable to connect the Breakout Board to the PCIe host board.

.. image:: /_static/images/breakout/breakout_IO_cable.jpg
    :width: 50%
    :align: center

Headstage link
----------------------------
.. image:: /_static/images/breakout/MMCX_cable.jpg
    :width: 50%
    :align: center

Use the MMCX to MMCX cable to connect the from PCIe host board to the breakout board. Use one line for each hub/headstage. Make sure that you are using the same port everywhere; i.e. port 'A' on the PCIe host board, the side of the Breakout Board, and the face of the Breakout Board.

The same cable type can be used to connect the clock in/output on the PCIe host board to the clock in/output on the breakout board.

Updating Firmware
-----------------------------
If necessary, the micro-USB port on the Breakout Board can be used to update the firmware on the board.
