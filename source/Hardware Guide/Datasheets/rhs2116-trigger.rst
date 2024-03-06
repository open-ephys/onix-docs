.. _onidatasheet_rhs2116trigger:

RHS2116 Trigger
###########################################
:Authors: Jonathan P. Newman
:Version: 1
:IO: Register Access
:ONIX ID: 32

Description
*******************************************
The **RHS2116 Trigger** device generates triggers and for Intan `RHS2116
bioamplifier and stimulator chip(s)
<https://intantech.com/files/Intan_RHS2116_datasheet.pdf>`__ either from a
remote source via external SYNC pin or locally via GPIO or TRIGGER register.
This device can be used to synchronize stimulus application and recovery across
chips.

.. _onidatasheet_rhs2116trigger_reg:

Register Programming
*******************************************

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Address
      - Name
      - Access
      - Time of Effect
      - POR Value
      - Reset Action
      - Description

    * - 0x00
      - ENABLE
      - R/W
      - N/A
      - N/A
      - N/A
      - ONI required enable register

        * This register has no effect. Writes will be ignored without error.

    * - 0x01
      - TRIGGERSOURCE
      - R/W
      - Immediate
      - 0
      - None
      - The LSB is used to determine the trigger source

        * 0x0: Transmitter. Respect local triggers (e.g. via GPIO or TRIGGER
          register) and broadcast via sync pin. If multiple chips are connected
          to the SYNC pin, then this device becomes a transmitter to trigger
          stimulation sequences other RHS2116 Trigger devices with
          TRIGGERSOURCE = 0x1 (receiver).
        * 0x1: Receiver. Only resepct triggers received from sync pin.

    * - 0x02
      - TRIGGER
      - W
      - Immediate
      - 0
      - 0
      - Writing 0x1 to this register will trigger a stimulation sequence if the
        TRIGGERSOURCE is set to 0x0 (transmitter). Otherwise it will do nothing.
        Regardless, this register is automatically be reset to 0x0 immediately
        after writing to it.

Device To Host Data Frames
******************************************
No frames are transmitted to the host.

Host To Device Data Frames
******************************************
This device does not accept input frames. All write attempts will fail with an
error.

