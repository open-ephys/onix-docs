.. _onidatasheet_fmc_clock_out:

FMC Host Clock Output Device
###########################################
:Authors: Jonathan P. Newman
:IO: Register Access
:ONIX ID: 22
:ONIX Hubs: :ref:`fmc_host_1r3`

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
      - Output enable. Bit 0 = 0 is disabled, Bit 0 = 1 is enabled.

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
Each frame transmitted to the host consists of a single 12-channel round robbin
sample:

.. wavedrom::

    {
        reg: [
          {bits: 64, name: "Acquisition Clock Counter", type: 0},
          {bits: 32, name: "Device Address", type: 0},
          {bits: 32, name: "Data Size", type: 0, attr: 32},

          {bits: 64, name: "Hub Clock Counter", type: 3},

          {bits: 16, name: "Channel 0 Voltage", type: 4, attr: "ADC 0"},
          {bits: 16, name: "Channel 1 Voltage", type: 4, attr: "ADC 0"},
          {bits: 16, name: "Channel 2 Voltage", type: 4, attr: "ADC 0"},
          {bits: 16, name: "Channel 3 Voltage", type: 4, attr: "ADC 0"},
          {bits: 16, name: "Channel 4 Voltage", type: 4, attr: "ADC 0"},
          {bits: 16, name: "Channel 5 Voltage", type: 4, attr: "ADC 0"},

          {bits: 16, name: "Channel 6 Voltage", type: 6, attr: "ADC 1"},
          {bits: 16, name: "Channel 7 Voltage", type: 6, attr: "ADC 1"},
          {bits: 16, name: "Channel 8 Voltage", type: 6, attr: "ADC 1"},
          {bits: 16, name: "Channel 9 Voltage", type: 6, attr: "ADC 1"},
          {bits: 16, name: "Channel 10 Voltage", type: 6, attr: "ADC 1"},
          {bits: 16, name: "Channel 11 Voltage", type: 6, attr: "ADC 1"},

        ],
        config: {bits: 384, lanes: 12, vflip: true, hflip: true, fontsize: 11}
    }

All voltages are signed, twos-complement, 16-bit integers. The two
least-significant bits are always 0 since ADCs are 14-bit.  Under the hood,
there are actually two, simultaneously sampling ADCs each of which produces 6
samples in each data frame (different colors in the diagram). The following
pairs of channels are simultaneously sampled:

- 0 and 6
- 1 and 7
- 2 and 8
- 3 and 9
- 4 and 10
- 5 and 11

Host To Device Data Frames
******************************************
Each frame sent to the device contains 12 16-bit voltages used to update the
DAC:

.. wavedrom::

    {
        reg: [
          {bits: 32, name: "Device Address", type: 0},
          {bits: 32, name: "Data Size", type: 0, attr: 24},

          {bits: 16, name: "Channel 0 Voltage", type: 4},
          {bits: 16, name: "Channel 1 Voltage", type: 4},
          {bits: 16, name: "Channel 2 Voltage", type: 4},
          {bits: 16, name: "Channel 3 Voltage", type: 4},
          {bits: 16, name: "Channel 4 Voltage", type: 4},
          {bits: 16, name: "Channel 5 Voltage", type: 4},
          {bits: 16, name: "Channel 6 Voltage", type: 4},
          {bits: 16, name: "Channel 7 Voltage", type: 4},
          {bits: 16, name: "Channel 8 Voltage", type: 4},
          {bits: 16, name: "Channel 9 Voltage", type: 4},
          {bits: 16, name: "Channel 10 Voltage", type: 4},
          {bits: 16, name: "Channel 11 Voltage", type: 4},

        ],
        config: {bits: 256, lanes: 8, vflip: true, hflip: true, fontsize: 11}
    }

Voltage values are unsigned 16-bit integers. The output voltage transformation
is as follows:

.. math::

    V_{out} = 20 * (Code / (2^{16} - 1)) - 10

Some example codes are:

.. math::

    Code &= 0 \Rightarrow V_{out} = -10V

    Code &= 2^{15} - 1  \Rightarrow V_{out} = -0.000153V

    Code &= 2^{15} \Rightarrow V_{out} = 0.000153V

    Code &= 2^{16} - 1 \Rightarrow V_{out} = 10V

In order for the output voltage to appear at the channel itself, the channel
direction must be set to output (see `Register Programming`_). Outputs are
updated on a ~100 kHz internal clock. All channel voltages are updated
simultaneously.
