.. _onidatasheet_test0:

Test0 Device
###########################################
:Authors: Jonathan P. Newman
:Version: 2
:IO: Frame Source, Register Access
:ONIX ID: 10

Description
*******************************************
The **Test0** device is  used for testing during development.

- Fixed, hardware-defined frame rate
- Fixed, hardware-defined frame size
- Register-defined frame data 

.. _onidatasheet_test0_reg:

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
      - MESSAGE
      - R/W
      - Immediate
      - 42
      - None
      - The first 16-bits of the MESSAGE word appears in the device to host frame

    * - 0x02
      - NUMTESTWORDS
      - R
      - N/A
      - Implementation dependent, see hub documentation
      - None
      - Read-only register indicating number of 16-bit words following MESSAGE
        in each frame

    * - 0x03
      - FRAMERATE
      - R
      - N/A
      - Implementation dependent, see hub documentation
      - None
      - Read-only register indicating the fixed frame rate in Hz. 0 indicates
        that the frame rate is unspecified (variable or upstream controlled).

--

.. _onidatasheet_test0_d2h:

Device To Host Data Frames
******************************************
Each frame transmitted to the host is structured as follows:

.. wavedrom::

    {
        reg: [
          {bits: 64, name: "Acquisition Clock Counter", type: 0},
          {bits: 32, name: "Device Address", type: 0},
          {bits: 32, name: "Data Size", type: 0, attr: 36},

          {bits: 64, name: "Hub Clock Counter", type: 3},

          {bits: 16, name: "MESSAGE", type: 4},

          {bits: 16, name: "0", type: 4},
          {bits: 16, name: "1", type: 4},
          {bits: 16, name: "2", type: 4},
          {bits: 16, name: "...", type: 4},
          {bits: 16, name: "NUMTESTWORDS - 1", type: 4},

        ],
        config: {bits: 288, lanes: 9, vflip: true, hflip: true, fontsize: 11}
    }

Host To Device Data Frames
******************************************
This device does not accept input frames. All write attempts will fail with an
error.
