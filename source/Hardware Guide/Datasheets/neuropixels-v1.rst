.. _onidatasheet_neuropixels_v1:

Neuropixels V1
###########################################
:Authors: Jonathan P. Newman
:IO: Frame Source, Register Access
:ONIX ID: 11
:ONIX Hubs: :ref:`headstage_neuropix_1r2`

Description
*******************************************
The **Neuropixels V1 Device** acquires data from `Neuropixels V1 probes
<https://www.neuropixels.org/>`__.

Register Programming
*******************************************

Managed Registers
------------------------------------------
Managed register access is provided at offset 0x10000.

.. list-table:: Managed Registers
    :widths: auto
    :header-rows: 1

    * - Address
      - Name
      - Access
      - Time of Effect
      - POR Value
      - Reset Action
      - Description

    * - 0x10000
      - ENABLE
      - R/W
      - On Reset
      - Implementation dependent, see hub documentation
      - None
      - The LSB is used to enable or disable the device data stream:

          * 0x0: data output disabled
          * 0x1: data output enabled

Unmanaged Registers
------------------------------------------
Direct, unmanaged read and write access is provided to the Neuropixels V1
registers, which are reproduced here for clarity. The time of effect of changes
to these registers are defined by the probe. Complete documentation is
available only through IMEC.

.. list-table:: Unmanaged Registers
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
      - OP_MODE
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Operation mode register.

    * - 0x01
      - REC_MOD
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Recording flags register.

    * - 0x02
      - CAL_MOD
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Calibration flags register.

    * - 0x03
      - TEST_CONFIG1
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Test configuration register 1.


    * - 0x04
      - TEST_CONFIG2
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Test configuration register 2.

    * - 0x05
      - TEST_CONFIG3
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Test configuration register 3.

    * - 0x06
      - TEST_CONFIG4
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Test configuration register 4.

    * - 0x07
      - TEST_CONFIG5
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Test configuration register 5.

    * - 0x08
      - STATUS
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Shift register error status.

    * - 0x09
      - SYNC
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Sync code for delineating data frames.

    * - 0x0a
      - SR_CHAIN5
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Shift register chain 5.

    * - 0x0b
      - SR_CHAIN4
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Shift register chain 4.

    * - 0x0c
      - SR_CHAIN3
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Shift register chain 3.

    * - 0x0d
      - SR_CHAIN2
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Shift register chain 2.

    * - 0x0e
      - SR_CHAIN1
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Shift register chain 1.

    * - 0x0f
      - SR_LENGTH2
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Shift register read length 2. 16-bit integer formed with SR_LENGTH1
        indicates number of bytes to read into shift register.

    * - 0x10
      - SR_LENGTH1
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Shift register read length 1. 16-bit integer formed with SR_LENGTH2
        indicates number of bytes to read into shift register.

    * - 0x11
      - SOFT_RESET
      - R/W
      - See IMEC docs
      - "00000000"
      - None
      - Software issued synchronous reset.


Device To Host Data Frames
******************************************
Each frame transmitted to the host consists of a single "super frame"
containing all 384 AP channels and a single set of 32 LFP channels. Twelve of
these "super frames" are required to construct a single "ultra frame" which
contains 12 samples from each the 384 AP channels and a single sample from each
of the 384 LFP channels.

Each Frame is organized as follows:

.. wavedrom::

    {
        reg: [
          {bits: 64, name: "Acquisition Clock Counter", type: 0},
          {bits: 32, name: "Device Address", type: 0},
          {bits: 32, name: "Data Size", type: 0, attr: 944},

          {bits: 64, name: "Hub Clock Counter", type: 3},

          {bits: 32, name: "LFP Frame N", type: 4},

          {bits: 32, name: "AP Frame 0", type: 6},
          {bits: 32, name: "AP Frame 1", type: 6},
          {bits: 32, name: "AP Frame 2", type: 6},
          {bits: 32, name: "AP Frame 3", type: 6},
          {bits: 32, name: "AP Frame 4", type: 6},
          {bits: 32, name: "AP Frame 5", type: 6},
          {bits: 32, name: "AP Frame 6", type: 6},
          {bits: 32, name: "AP Frame 7", type: 6},
          {bits: 32, name: "AP Frame 8", type: 6},
          {bits: 32, name: "AP Frame 9", type: 6},
          {bits: 32, name: "AP Frame 10", type: 6},
          {bits: 32, name: "AP Frame 11", type: 6}
        ],
        config: {bits: 608, lanes: 19, vflip: true, hflip: true, fontsize: 11}
    }

Here, LFP and AP "Frames" are not actually 32-bits words but full, 32-ADC
sample blocks. Each one of these blocks is organized as follows:

.. wavedrom::

    {
        reg: [

          {bits: 16, name: "Sync Type", type: 3, attr: [207, 816]},

          {bits: 16, name: "ADC 00 Voltage", type: 6},
          {bits: 16, name: "ADC 05 Voltage", type: 6},
          {bits: 16, name: "ADC 10 Voltage", type: 6},
          {bits: 16, name: "ADC 15 Voltage", type: 6},
          {bits: 16, name: "ADC 20 Voltage", type: 6},
          {bits: 16, name: "ADC 25 Voltage", type: 6},
          {bits: 16, name: "ADC 30 Voltage", type: 6},

          {bits: 16, name: "ADC 01 Voltage", type: 6},
          {bits: 16, name: "ADC 06 Voltage", type: 6},
          {bits: 16, name: "ADC 11 Voltage", type: 6},
          {bits: 16, name: "ADC 16 Voltage", type: 6},
          {bits: 16, name: "ADC 21 Voltage", type: 6},
          {bits: 16, name: "ADC 26 Voltage", type: 6},
          {bits: 16, name: "ADC 31 Voltage", type: 6},

          {bits: 16, name: "ADC 02 Voltage", type: 6},
          {bits: 16, name: "ADC 07 Voltage", type: 6},
          {bits: 16, name: "ADC 12 Voltage", type: 6},
          {bits: 16, name: "ADC 17 Voltage", type: 6},
          {bits: 16, name: "ADC 22 Voltage", type: 6},
          {bits: 16, name: "ADC 27 Voltage", type: 6},
          {bits: 16, name: "Reserved", type: 0},

          {bits: 16, name: "ADC 03 Voltage", type: 6},
          {bits: 16, name: "ADC 08 Voltage", type: 6},
          {bits: 16, name: "ADC 13 Voltage", type: 6},
          {bits: 16, name: "ADC 18 Voltage", type: 6},
          {bits: 16, name: "ADC 23 Voltage", type: 6},
          {bits: 16, name: "ADC 28 Voltage", type: 6},
          {bits: 8, name: "Reserved", type: 0},
          {bits: 8, name: "Frame Counter MSB", type: 7},

          {bits: 16, name: "ADC 04 Voltage", type: 6},
          {bits: 16, name: "ADC 09 Voltage", type: 6},
          {bits: 16, name: "ADC 14 Voltage", type: 6},
          {bits: 16, name: "ADC 19 Voltage", type: 6},
          {bits: 16, name: "ADC 24 Voltage", type: 6},
          {bits: 16, name: "ADC 29 Voltage", type: 6},
          {bits: 16, name: "Frame Counter LSB", type: 7}

        ],
        config: {bits: 576, lanes: 18, vflip: true, hflip: true, fontsize: 11}
    }

Definitions for each of these fields are as follows:

    Sync Type
      Fixed word indicating the frame type

      -  207: Normal frame. Frame contains AP data.
      -  816: Super frame start. Frame contains LFP data.

    ADC Voltage
      Unsigned integer. Only the 10 LSBs are valid.

    Frame Counter
      A looping 24-bit frame counter produced by the probe to detect dropped
      frames and to ensure proper reset sequence that results in a count of 0
      at the start of transmission.

Host To Device Data Frames
******************************************
This device does not accept input frames. All write attempts will fail with an
error.
