.. _warnings:

Usage Warnings
==========================================
.. warning::  Improper setup and usage can cause damage to system components.

- Read the following warnings before starting to work with your system. These are crucial aspects to consider during setup and usage that are included in the documentation but are listed here for your convenience.
- Read the complete documentation carefully to understand how the system works and refer back to these warnings before using it. 

Hardware
--------------------------------
- Connecting or disconnecting the breakout board while the PC is on causes damage to the FMChost. More: :ref:`breakout_setup`.
   
   - **Power off the PC before connecting/disconnecting the breakout board.**

- Headstage voltage must be configured correctly for operation. The voltage that works for one headstage can damage another, and depends on your hardware configuration such as tether length. More: :ref:`tether_voltage`.

   - **Ensure each headstage is configured with the correct voltage according to its specification before connecting and switching on the headstage port switch.** 


Software
--------------------------------
*For the current Bonsai.ONIX library which is being revised to improve usability*

- Headstage port voltage configuration is managed via the :ref:`bonsai_onicontext` node or the :ref:`bonsai_headstageportcontroldev` node. The changes you make using these nodes apply immediately and persist in hardware even if the Bonsai workflow is not running. Headstage port voltage is reset to the default 4.9V only on a power cycle (power off and on — not reboot).
   
   - **Keep the headstage port switches off until you have configured each port correctly.**
   
   - **Remember to set the headstage voltage to the desired value after a power cycle.**
 
- The :ref:`bonsai_onicontext` provides a dynamic window to read and write to hardware, but parameters such as device voltage are not saved in the node when the workflow is saved. The :ref:`bonsai_headstageportcontroldev` node also reads and writes to hardware, but parameters are saved with the workflow. On loading a workflow, Bonsai writes the parameter values set when the workflow was last saved.

   - When you configure the voltage, the :ref:`bonsai_onicontext` node shows that value and when you save the workflow this value is not saved. Therefore, that value will not be set to hardware when you load the workflow again. On loading the workflow, the :ref:`bonsai_onicontext` node will be reading the voltage that is already set on the hardware and showing this  in the ``LinkVoltage`` field.

   - When you configure the voltage, the :ref:`bonsai_headstageportcontroldev` node shows that value and when you save the workflow this value is saved. Therefore, that value will be set to hardware when you load the workflow again. If you make changes to the voltage value (with any node) and save the workflow, they will be saved in the ``LinkVoltage`` property of the :ref:`bonsai_headstageportcontroldev` node.
 
- Any workflows containing the :ref:`bonsai_NeuropixelsV1edev` node require the :ref:`headstage_neuropix1e` to be connected before the workflows can be opened or loaded into Bonsai.
   
   - Check that the voltage set to the headstage port is correct for the :ref:`headstage_neuropix1e` by using a workflow of a single :ref:`bonsai_onicontext` node to configure it before connecting the headstage in order to open a workflow that contains the :ref:`bonsai_NeuropixelsV1edev` node.

- An :ref:`bonsai_onicontext` node or any device node in a workflow can override device settings in another workflow if device addresses are not distinct, because these nodes read/write directly to hardware.

   - Only have one workflow open at a time.
