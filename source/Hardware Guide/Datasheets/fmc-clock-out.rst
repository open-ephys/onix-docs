.. _onidatasheet_fmc_clock_out:

FMC Host Clock Output Device
###########################################
:Authors: Jonathan P. Newman
:Version: 1
:IO: Register Access
:ONIX ID: 20
:ONIX Hubs: :ref:`pcie_host`

Description
*******************************************
The **FMC Host Clock Output** device generates a clock output that is
synchronized to a local hardware clock. It has very fast rising edges and a
high-current output that can drive 50 ohm coaxial cable.

The output of this clock can optionally be gated by the ONI-specified `RUNNING`
gate to link the clock to the start of data acquisition within a given
Acquisition Context.

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
      - NULLPARM
      - R
      - Immediate
      - 0
      - None
      - No command

    * - 0x01
      - EN
      - R/W
      - Immediate
      - 0
      - None
      - Output enable. Bit 0 = 0 is disabled (output driven low), Bit 0 = 1 is enabled.

    * - 0x02
      - H
      - R/W
      - Immediate
      - 1
      - None
      - Number of input clock cycles output clock should be high. Valid values
        are 1 or greater.

    * - 0x03
      - L
      - R/W
      - Immediate
      - 1
      - None
      - Number of input clock cycles output clock should be low. Valid values
        are 1 or greater.

    * - 0x04
      - DELAY
      - R/W
      - On Reset
      - 0
      - None
      - Delay, in input clock cycles, following reset before clock becomes
        active.

    * - 0x05
      - GATEWRUN
      - R/W
      - Immediate
      - 1
      - None
      - LSB sets the gate using run status

        * 0b0: Clock runs whenever FMCCLKOUT_EN(0) is 1.
        * 0b1: Clock runs only when acquisition is in RUNNING state.

    * - 0x06
      - BASEFREQ
      - R
      - N/A
      - CLK_RATE_HZ
      - Default
      - Frequency of the input clock

Device To Host Data Frames
******************************************
No frames are transmitted to the host.

Host To Device Data Frames
******************************************
This device does not accept input frames. All write attempts will fail with an
error.
