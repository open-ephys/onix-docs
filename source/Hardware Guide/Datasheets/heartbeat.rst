.. _onidatasheet_heartbeat:

Heartbeat
###########################################
:Authors: Jonathan P. Newman
:Version: 1
:IO: Frame Source, Register Access
:ONIX ID: 12
:ONIX Hubs: :ref:`pcie_host`

Description
*******************************************
The **Heartbeat** device produces periodic samples containing the hub clock
count. It is useful for generating keep-alive signal for various communication
channels.

.. _onidatasheet_heartbeat_reg:

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
      - Immediate
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

.. _onidatasheet_heartbeat_d2h:

Device To Host Data Frames
******************************************
Each frame transmitted to the host is structured as follows:

.. wavedrom::

    {
        reg: [
          {bits: 64, name: "Acquisition Clock Counter", type: 0},
          {bits: 32, name: "Device Address", type: 0},
          {bits: 32, name: "Data Size", type: 0, attr: 36},

          {bits: 64, name: "Hub Clock Counter", type: 3}
        ],
        config: {bits: 192, lanes: 6, vflip: true, hflip: true, fontsize: 11}
    }

.. _onidatasheet_heartbeat_h2d:

Host To Device Data Frames
******************************************
This device does not accept input frames. All write attempts will fail with an
error.
