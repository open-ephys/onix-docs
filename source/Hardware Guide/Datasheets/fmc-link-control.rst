.. _onidatasheet_fmc_link_control:

FMC Link Controller
###########################################
:Authors: Jonathan P. Newman
:IO: Frame Source, Register Access
:ONIX ID: 23
:ONIX Hubs: :ref:`fmc_host_1r3`

Description
*******************************************
The **FMC Host Link Controller** is used to control and monitor DS90UB9x-based
serialized connections to hubs connected to a host such as headstages and
miniscopes. It can control power provided to those hubs and receives RF lock,
CRC error, and other information.

.. note::

    Typical inplementaitons will default link voltages to 0. Often the link
    will need to be manually activated via the appropriate registers in order
    for a headstage to be used.

.. warning::

    The maximum DC voltage that can be produced by this device far exceeds the
    absolute maximum ratings for most headstages. Although they typically will
    have some form input overvoltage protection, the user should be careful to
    keep the voltage within a functional range.

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
      - On Reset
      - Implementation dependent, see hub documentation
      - None
      - The LSB is used to enable or disable the device data stream:

            * 0x0: data output disabled
            * 0x1: data output enabled

    * - 0x01
      - GPOSTATE
      - R/W
      - Immediate
      - 0
      - 0
      - GPO output state (bits 31 downto 3: ignore. bits 2 downto 0: '1' = high, '0' = low)

    * - 0x02
      - DESPWR
      - R/W
      - Immediate
      - 0
      - None
      - Set link deserializer PDB state, 0 = deserializer power off else on.  Does not affect port voltage!

    * - 0x03
      - PORTVOLTAGE
      - R/W
      - Immediate
      - EEPROM*
      - None
      - 10 * link voltage. Valid values:

            * 000         :  Turn off
            * 001         :  3.3 volts (min)
            * ...         :  3.3 volts (min)
            * 032         :  3.3 volts (min)
            * 033         :  3.3 volts (min)
            * 034         :  3.4 volts
            * 035         :  3.5 volts
            * ...         :  ...
            * 108         : 10.8 volts
            * 109         : 10.9 volts
            * 110         : 11.0 volts (max)
            * 111         : 11.0 volts (max)
            * ...         : 11.0 volts (max)

    * - 0x04
      - SAVEVOLTAGE
      - W
      - Immediate
      - EEPROM*
      - None
      - Save link voltage to non-volatile EEPROM if greater than 0. This
        voltage will be applied after POR.

Device To Host Data Frames
******************************************
Each frame transmitted to the host is structured as follows:

.. wavedrom::

    {
        reg: [
          {bits: 64, name: "Acquisition Clock Counter", type: 0},
          {bits: 32, name: "Device Address", type: 0},
          {bits: 32, name: "Data Size", type: 0, attr: 10},

          {bits: 64, name: "Hub Clock Counter", type: 3},

          {bits: 8, name: "Status Codeword", type: 4},

          {bits: 5, name: "Reserved"},

          {bits: 1, name: "CV", type: 2},
          {bits: 1, name: "PP", type: 2},
          {bits: 1, name: "SL", type: 2},

          {bits: 16}

        ],
        config: {bits: 224, lanes: 7, vflip: true, hflip: true, fontsize: 11}
    }

This device produces frames when triggered by the **CV**, **PP**, or **SL**
bits. These are defined as follows:

    CV
      Codeword valid. Indicates that the Status Codeword field has valid data.
      A frame is produced when this bit goes high. The codeword meaning is
      hub-dependent. See hub documentation for definitions.

    PP
      Parity Check Pass. This bit reflects the state of the PASS pin on the
      DS90UB9x4 deserializer.

        - 0b0: One or more errors were detected in the received payload.
        - 0b1: Error free transmission in forward channel operation.

      A frame is produced whenever this bit changes state.

    SL
      SERDES Lock. This bit reflects the state of the LOCK pin on the DS90UB9x4
      deserializer, which monitors the lock status of FPD-Link III channel.

        - 0b0: PLL is unlocked link is down.
        - 0b1: PLL is locked, link is active.

      A frame is produced whenever this bit changes state.

Host To Device Data Frames
******************************************
This device does not accept input frames. All write attempts will fail with an
error.
