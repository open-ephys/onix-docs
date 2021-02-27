.. _onidatasheet_fmc_analog_io:

FMC Host Analog IO Device
###########################################
:Authors: Jonathan P. Newman
:IO: Frame Source, Frame Sink, Register Access
:ONIX ID: 22
:ONIX Hubs: :ref:`fmc_host_1r3`

Description
*******************************************
The **FMC Host Analog IO** device sends and receives data to/from 12 analog
IOs. It is based on three chips:

- `AD7617 <https://www.analog.com/en/products/ad7617.html>`__ 14-bit ADC/DAS
- `AD7617 <https://www.analog.com/en/products/ad5766.html>`__ 16-bit DAC
- `DG1412E <https://www.vishay.com/docs/75104/dg1411e.pdf>`__ Precision analaog switch

The direction of each of channel is selectable during acquisition via
configuration registers. Analog inputs are always active regardless of the
directionality, such that a copy of output signals is visible on the input
channels. The input range of each analog input can be independently adjusted
prior to acquisition between three ranges: ±2.5V, ±5V, or ±10V. Analog inputs
are sampled at 100 kHz per channel with simultaneous sampling between groups of
two channels. Analog inputs have a ~33 kHz cutoff first-order anti-aliasing
filter prior to the ADC. The DAC output range is ±10V. All DAC outputs are
updated synchronously whenever new data is provided. Regardless of the selected
analog input range, DAC outputs will not damage the ADC.

.. warning::

    The maximal usable range of the analog inputs is ±10V. Inputs exceeding
    ±20V may cause perminent damage.

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
      - DIR
      - R/W
      - Immediate
      - 0x0000
      - None
      - The twelve LSBs (0b000000000000) are a bitfield indicating
        directionality of each channel. Bit 0 corresponds to channel 0 and bit
        11 corresponds to channel 11. For each bit:

            * 0b0: Output
            * 0b1: Input

    * - 0x02
      - INRANGE00
      - R/W
      - On Reset
      - 0x0000
      - None
      - The two LSBs indicate the channel 0 ADC input voltage range:

            * 0xXXX0: ±10V
            * 0xXXX1: ±2.5V
            * 0xXXX2: ±5V
            * 0xXXX3: ±10V


    * - 0x03
      - INRANGE01
      - R/W
      - On Reset
      - 0x0000
      - None
      - The two LSBs indicate the channel 1 ADC input voltage range:

            * 0xXXX0: ±10V
            * 0xXXX1: ±2.5V
            * 0xXXX2: ±5V
            * 0xXXX3: ±10V

    * - 0x04
      - INRANGE02
      - R/W
      - On Reset
      - 0x0000
      - None
      - The two LSBs indicate the channel 2 ADC input voltage range:

            * 0xXXX0: ±10V
            * 0xXXX1: ±2.5V
            * 0xXXX2: ±5V
            * 0xXXX3: ±10V

    * - 0x05
      - INRANGE03
      - R/W
      - On Reset
      - 0x0000
      - None
      - The two LSBs indicate the channel 3 ADC input voltage range:

            * 0xXXX0: ±10V
            * 0xXXX1: ±2.5V
            * 0xXXX2: ±5V
            * 0xXXX3: ±10V

    * - 0x06
      - INRANGE04
      - R/W
      - On Reset
      - 0x0000
      - None
      - The two LSBs indicate the channel 4 ADC input voltage range:

            * 0xXXX0: ±10V
            * 0xXXX1: ±2.5V
            * 0xXXX2: ±5V
            * 0xXXX3: ±10V

    * - 0x07
      - INRANGE05
      - R/W
      - On Reset
      - 0x0000
      - None
      - The two LSBs indicate the channel 5 ADC input voltage range:

            * 0xXXX0: ±10V
            * 0xXXX1: ±2.5V
            * 0xXXX2: ±5V
            * 0xXXX3: ±10V

    * - 0x08
      - INRANGE06
      - R/W
      - On Reset
      - 0x0000
      - None
      - The two LSBs indicate the channel 6 ADC input voltage range:

            * 0xXXX0: ±10V
            * 0xXXX1: ±2.5V
            * 0xXXX2: ±5V
            * 0xXXX3: ±10V

    * - 0x09
      - INRANGE07
      - R/W
      - On Reset
      - 0x0000
      - None
      - The two LSBs indicate the channel 7 ADC input voltage range:

            * 0xXXX0: ±10V
            * 0xXXX1: ±2.5V
            * 0xXXX2: ±5V
            * 0xXXX3: ±10V

    * - 0x0a
      - INRANGE08
      - R/W
      - On Reset
      - 0x0000
      - None
      - The two LSBs indicate the channel 8 ADC input voltage range:

            * 0xXXX0: ±10V
            * 0xXXX1: ±2.5V
            * 0xXXX2: ±5V
            * 0xXXX3: ±10V

    * - 0x0b
      - INRANGE09
      - R/W
      - On Reset
      - 0x0000
      - None
      - The two LSBs indicate the channel 9 ADC input voltage range:

            * 0xXXX0: ±10V
            * 0xXXX1: ±2.5V
            * 0xXXX2: ±5V
            * 0xXXX3: ±10V

    * - 0x0c
      - INRANGE10
      - R/W
      - On Reset
      - 0x0000
      - None
      - The two LSBs indicate the channel 10 ADC input voltage range:

            * 0xXXX0: ±10V
            * 0xXXX1: ±2.5V
            * 0xXXX2: ±5V
            * 0xXXX3: ±10V

    * - 0x0d
      - INRANGE11
      - R/W
      - On Reset
      - 0x0000
      - None
      - The two LSBs indicate the channel 11 ADC input voltage range:

            * 0xXXX0: ±10V
            * 0xXXX1: ±2.5V
            * 0xXXX2: ±5V
            * 0xXXX3: ±10V

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
          {bits: 16, name: "Channel 11 Voltage", type: 6, attr: "ADC 1"}
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
          {bits: 16, name: "Channel 11 Voltage", type: 4}
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
