.. _onidatasheet_ds90ub9x_raw:

DS90UB9X Raw Device
###########################################
:Authors: Aarón Cuevas López
:IO: Frame Source, Register Access
:ONIX ID: 24
:ONIX Hubs: :ref:`pcie_host`

Description
*******************************************
The **DS90UB9X Raw Device** can be used to receive raw data from and control
`DS90UB9x <https://www.ti.com/product/DS90UB934-Q1>`__ SERDES pairs. This
device is useful for acquiring data from instruments that use `DS90UB9x3
<https://www.ti.com/product/DS90UB933-Q1>`__ serializers, which are physically
compatible with ONIX host hardware, but do not implement :ref:`ONIX Serization
protocol <serialization>`. For example, third party devices such as `UCLA
Miniscope <http://miniscope.org/index.php/Main_Page>`__ and its derivatives.

Register Programming
*******************************************

Managed Registers
------------------------------------------
Managed register access is provided at offset 0x8000.

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

    * - 0x8000
      - ENABLE
      - R/W
      - On Reset
      - Implementation dependent, see hub documentation
      - None
      - The LSB is used to enable or disable the device data stream:

          * 0x0: data output disabled
          * 0x1: data output enabled

    * - 0x8001
      - READSZ
      - R/W
      - On Reset
      - 1280
      - None
      - Frame data size in samples

    * - 0x8002
      - TRIGGER
      - R/W
      - On Reset
      - 0
      - None
      - The LSBs determines the data capture start tigger

          * Bit 0: Trigger mode. '0' = Continuous, '1' = Use trigger
          * Bit 1: Trigger bit. '0' = HSYNC, '1' = VSYNC.  
          * Bit 2: Mode. '0' = Edge, '1' = Level (High or Low)
          * Bit 3: Polarity. '0' = Non-inverted (Rising/High), '1' = Inverted (Falling/Low).

    * - 0x8003
      - TRIGGEROFF
      - R/W
      - On Reset
      - 0
      - None
      - Offset, in samples, that are skipped following trigger.

    * - 0x8004
      - DATAGATE
      - R/W
      - On Reset
      - 0
      - None
      - The LSBs are used to determine how data is gated

          * Bit 0: Gate mode. '0' = disabled, '1' = enabled. 
          * Bit 1: Gate bit. '0' = HSYNC gate, '1' = VSYNC gate. 
          * Bit 2: Polarity. '0' = Non-inverted (high), '1' = Inverted (low).

    * - 0x8005
      - SYNCBITS
      - R/W
      - On Reset
      - 0
      - None
      - The LSB determines if HSYNC and VSYNC bits are included in the data
        word along with parallel port state. If included, bit 13 is HSYNC and
        bit 14 is VSYNC.

          * 0x0: not included
          * 0x1: included

    * - 0x8006
      - SYNCBITS
      - R/W
      - On Reset
      - 0
      - None
      - If enabled, mark bit 15 of all data words in a frame after a choosen
        sync edge. Note that words in a frame still respect TRIGGER and GATE
        properties. Therefore this property provides a means to mark the first
        frame in a multi-frame sample (e.g. the first row in a camera image).

          * Bit 0: not included
          * Bit 1: '0' = HSYNC, '1' = VSYNC
          * Bit 2: '0' = Rising edge, '1' = Falling edge


    * - 0x8007
      - GPIO_DIR
      - R/W
      - On Reset
      - 0 
      - None
      - Bits 0-3 determine the direction of GPIO 0-3. For each bit:

          * 0b0: Output
          * 0b1: Input

    * - 0x8008
      - GPIO_VAL
      - R/W
      - On Reset
      - 0
      - None
      - Bits 0-3 determine the value of GPIO 0-3. For each bit:

          * 0b0: Low
          * 0b1: High

    * - 0x8009
      - GPIO_VAL
      - R
      - On DS90UBX LOCK or PASS pin state change
      - N/A
      - None
      - Access the DS90UBX LOCK and PASS pin state to determine if the SERDES
        is operating normally.

          * Bit 0: DS90UBX LOCK pin state
          * Bit 1: DS90UBX PASS pin state


Unmanaged Registers
------------------------------------------
Unmanaged read and write access is provided to the SERDES I2C bus when using
register addresses less than 0x8000.

Device To Host Data Frames
******************************************
Each frame transmitted to the host consists of a READSZ-sample frame.

.. wavedrom::

    {
        reg: [
          {bits: 64, name: "Acquisition Clock Counter", type: 0},
          {bits: 32, name: "Device Address", type: 0},
          {bits: 32, name: "Data Size", type: 0, attr: 32},

          {bits: 64, name: "Hub Clock Counter", type: 3},

          {bits: 16, name: "Sample 0", type: 4},
          {bits: 16, name: "Sample 1", type: 4},
          {bits: 16, name: "Sample ...", type: 4},
          {bits: 16, name: "Sample READSZ - 1", type: 4},
        ],
        config: {bits: 256, lanes: 8, vflip: true, hflip: true, fontsize: 11}
    }


Host To Device Data Frames
******************************************
This device does not accept input frames. All write attempts will fail with an
error.
