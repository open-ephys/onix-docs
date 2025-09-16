.. _onidatasheet_loadtest:

Load Test Device
###########################################
:Authors: Jonathan P. Newman
:Version: 2
:IO: Frame Source, Register Access
:ONIX ID: 27
:ONIX Hubs: This device is used for real-world bandwidth and latency testing.

Description
*******************************************
The **Load Test** device that produces data at user-settable size and rate to
stress test various communication links and test closed-loop response latency.

.. _onidatasheet_loadtest_reg:

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
      - DT0H16_WORDS
      - R/W
      - On Reset
      - 0
      - None
      - The number of incrementing 16-bit integers sent in each read-frame.

        .. note::
            The maximum value of DT0H16_WORDS depends of CLK_HZ and
            CLK_DIV. There needs to be enough clock cycles to satisfy

            .. math::

                DT0H16\_WORDS <= CLK\_HZ / CLK\_DIV - 9

            Setting DTOH16_WORDS above this value will result in a *decreased*
            device to host load as samples will be skipped.

    * - 0x04
      - HTOD32_WORDS
      - R/W
      - On Reset
      - 0
      - None
      - The number of 32-bit dummy words in a write-frame. Write-frames always
        start with a single 64-bit unsigned integer that is subtracted from the
        current acquisition clock counter value when it is received. This value
        is looped back into the device to host data frame for testing loop
        latency. After the 64-bit unsigned integer, write-frames contain
        HTOD32_WORDS 32-bit words which are read and ignored by the device.
        These values can be used to test the impact of various data transmission
        loads on closed-loop performance.

    * - 0x05
      - DTOH_START
      - R/W
      - On Reset
      - 0
      - None
      - The start value of the counter being sent sent with each read-frame.


.. _onidatasheet_loadtest_d2h:

Device To Host Data Frames
******************************************
With DT0H16_WORDS = 4 and DTOH_START= 42, the first frame transmitted to the host
is structured as follows:

.. wavedrom::

    {
        reg: [
          {bits: 64, name: "Acquisition Clock Counter", type: 0},
          {bits: 32, name: "Device Address", type: 0},
          {bits: 32, name: "Data Size", type: 0, attr: 24},

          {bits: 64, name: "Hub Clock Counter", type: 3},

          {bits: 64, name: "Hub Clock Delta", type: 5},

          {bits: 16, name: "Frame Word 0", type: 6, attr:42},
          {bits: 16, name: "Frame Word 1", type: 6, attr:43},
          {bits: 16, name: "Frame Word 2", type: 6, attr:44},
          {bits: 16, name: "Frame Word 3", type: 6, attr:45}

        ],
        config: {bits: 320, lanes: 10, vflip: true, hflip: true, fontsize: 11}
    }

|

Hub Clock Counter Delta
    64-bit unsigned integer that the result of subtracting the Hub Clock
    Counter value from the Hub Clock Counter Loop back value in
    :ref:`onidatasheet_loadtest_h2d`. This provides a real-world, hardware
    timed measurement of closed-loop latency.

Frame Word N
    Ignored data that can be used for host to device load testing.  When
    DT0H16_WORDS is set to a different value, the Data Size field along with
    the number of words at the end of the frame will change.

.. _onidatasheet_loadtest_h2d:

Host To Device Data Frames
******************************************
With HTOD32_WORDS = 2, each frame transmitted to the host is structured as
follows:

.. wavedrom::

    {
        reg: [
          {bits: 32, name: "Device Address", type: 0},
          {bits: 32, name: "Data Size", type: 0, attr: 16},

          {bits: 64, name: "Hub Clock Counter Loopback", type: 3},

          {bits: 32, name: "Frame Word 0", type: 6, atter:42},
          {bits: 32, name: "Frame Word 1", type: 6, atter:43},

        ],
        config: {bits: 192, lanes: 6, vflip: true, hflip: true, fontsize: 11}
    }

|

Hub Clock Counter Loopback
    64-bit unsigned integer that is subtracted from the current Hub Clock
    Counter value to produce the Hub Clock Counter Delta field in
    :ref:`onidatasheet_loadtest_d2h`.

Frame Word N
    Ignored data that can be used for host to device load testing.
