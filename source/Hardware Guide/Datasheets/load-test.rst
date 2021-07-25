.. _onidatasheet_load-test:

Load Test Device
###########################################
:Authors: Jonathan P. Newman
:IO: Frame Source, Register Access
:ONIX ID: 27
:ONIX Hubs: This device is used for testing purposes during developments.

Description
*******************************************
The **Load Test** device produces data at user-settable size and rate to stress
test various communication links.

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
      - Heartbeat clock divider ratio. Minimum value is CLK_HZ / 10e6

    * - 0x02
      - CLK_HZ
      - R
      - N/A
      - N/A
      - None
      - The frequency parameter, CLK_HZ, used in the calculation of CLK_DIV.

    * - 0x03
      - FRAME_WORDS
      - R/W
      - On Reset
      - 1
      - None
      - Number of repetitions of 16-bit unsigned integer 42 sent with each
        frame.

.. note::
    The maximum value of ``FRAME_WORDS`` depends of ``CLK_HZ`` and ``CLK_DIV``. There needs
    to be enough clock cycles to satisfy:

    .. math::

        CLK\_HZ / CLK\_DIV >= FRAME\_WORDS + 5

    Exceeding this value will result in *decreased* load bandwidth as samples
    will be skipped.

Device To Host Data Frames
******************************************
With ``FRAME_WORDS`` = 4, each frame transmitted to the host is structured as
follows:

.. wavedrom::

    {
        reg: [
          {bits: 64, name: "Acquisition Clock Counter", type: 0},
          {bits: 32, name: "Device Address", type: 0},
          {bits: 32, name: "Data Size", type: 0, attr: 16},

          {bits: 64, name: "Hub Clock Counter", type: 3},

          {bits: 16, name: "Frame Word 0", type: 6, atter:42},
          {bits: 16, name: "Frame Word 1", type: 6, atter:42},
          {bits: 16, name: "Frame Word 2", type: 6, atter:42},
          {bits: 16, name: "Frame Word 3", type: 6, atter:42}

        ],
        config: {bits: 256, lanes: 8, vflip: true, hflip: true, fontsize: 11}
    }


When ``FRAME_WORDS`` is set to a different value, the Data Size field along with
the number of words at the end of the frame will change.

Host To Device Data Frames
******************************************
This device does not accept input frames. All write attempts will fail with an
error.
