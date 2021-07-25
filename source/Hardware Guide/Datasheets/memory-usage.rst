.. _onidatasheet_memory-usage:

Memory Usage Monitor
###########################################
:Authors: Aarón Cuevas López
:IO: Frame Source, Register Access
:ONIX ID: 28
:ONIX Hubs: :ref:`pcie_host`

Description
*******************************************
The **Memory Usage Monitor** produces periodic samples that contain information
about data buffer memory status. This device is useful for monitoring
if frames are being cleared fast enough by the host PC to prevent real-time
delays or overflows. Ideally, buffering should never be used and the memory
usage should remain at 0.

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
      - CLK_DIV
      - R/W
      - On Reset
      - CLK_HZ / HB_HZ where HB_HZ is a implementation dependent default rate
      - None
      - Read frequency clock divider ratio. Minimum value is CLK_HZ / 10e6

    * - 0x02
      - CLK_HZ
      - R
      - N/A
      - N/A
      - None
      - The frequency parameter, CLK_HZ, used in the calculation of CLK_DIV.

    * - 0x03
      - MEM_WORDS
      - R
      - N/A
      - N/A
      - None
      - The total number of 32-bit words in memory.

Device To Host Data Frames
******************************************
Each frame transmitted to the host is structured as follows:

.. wavedrom::

    {
        reg: [
          {bits: 64, name: "Acquisition Clock Counter", type: 0},
          {bits: 32, name: "Device Address", type: 0},
          {bits: 32, name: "Data Size", type: 0, attr: 12},

          {bits: 64, name: "Hub Clock Counter", type: 3},

          {bits: 32, name: "Number of 32-bit Memory Words Used", type: 4}

        ],
        config: {bits: 224, lanes: 7, vflip: true, hflip: true, fontsize: 11}
    }

Host To Device Data Frames
******************************************
This device does not accept input frames. All write attempts will fail with an
error.
