.. _onidatasheet_fmc_digital_io:

FMC Host Digital IO Device
###########################################
:Authors: Jonathan P. Newman, Aarón Cuevas López
:Version: 2
:IO: Frame Source, Frame Sink, Register Access
:ONIX ID: 18
:ONIX Hubs: :ref:`pcie_host`

Description
*******************************************
The **FMC Host Digital IO** device sends and receives digital data to and from
:ref:`breakout` and allows control over its display state. This includes:

- 8x 5-volt tolerate digital inputs sampled at 10 MHz
- 8x digital outputs sampled at 10 MHz
- `HARP bus <https://www.cf-hw.org/harp>`__ controller
- 6x user buttons
- LED brightness and on/off state

Digital communication with the :ref:`breakout` occurs using a simple
serialization protocol.

Breakout to Host Serialization
------------------------------------------
The breakout to host serialization protocol is as follows:

.. wavedrom::

    {
    signal: [
      {name: 'clk',  wave: 'p............'},
      ['Physical Bus',
        {name: 'sclk', wave: '01....0....1.'},
        {name: 'dat0', wave: '6xx3.....6.xx', data:['P10', 'Buttons','P10']},
        {name: 'dat1', wave: '67.......6.7.', data:['P32', 'Digital In','P32']},
      ],
    ],
    config: { hscale: 1},
    head: {
        text:'Breakout to Host Serialization Protocol',
        tick:0,
    },
    }

|

Buttons
    Buttons press state. Each bit represents the press state of a single
    button in the 6-buttons bank.

    -  0: Up
    -  1: Down

Digital In
    Digital input port. Each bit represents state of a signal line in the
    8-bit port.

    - 0: Low
    - 1: High

Pnn
    Headstage port power state. Each bit represents the power state of one of
    the four headstage ports.

    - 0: Power off
    - 1: Power on

A clock recovery circuit is required at the receiver to generate ``clk`` from
``sclk`` in order to sample the ``dat`` lines.

Host to Breakout Serialization
------------------------------------------
The host to breakout serialization protocol is as follows:

.. wavedrom::

    {
    signal: [
      {name: 'clk',  wave: 'p..............'},
      ['Physical Bus',
        {name: 'sclk', wave: '01.....0.....1.'},
        {name: 'dat0', wave: '73.6.7.......3.', data:['', 'CMD','SW','Digital Out']},
      ],
    ],
    config: { hscale: 1},
    head: {
        text:'Host to Breakout Serialization Protocol',
        tick:0,
    },
    }

|

CMD
    Two bit command word that determines what to do with SW.

    - 0b00: Shift slow bits into slow shift register
    - 0b01: Validate and move slow shift register to outputs and set initial
      state to [0, ..., 0, slow1, slow0]. slow1 should be the desired MSB at
      next command.
    - 0b10: Reserved, same as 0b00 currently. Don't use.
    - 0b11: Reset

SW
    Two-bit "slow-word" part. These bits are accumulated over time in order
    to control the display state and non-timing critical apsects of the
    breakout board. For instance, LED colors and brightness, headstage lock
    state, etc. As of this writing, for :ref:`breakout`, a complete
    slow-word is as follows.

    .. wavedrom::

        {
            reg: [
              {bits: 1, name: "Acq. Running" },
              {bits: 1, name: "Acq. Reset Done" },
              {bits: 2, name: "Reserved" },
              {bits: 4, name: "LED Level" },
              {bits: 2, name: "LED Mode" },
              {bits: 2, name: "Port A Status" },
              {bits: 2, name: "Port B Status" },
              {bits: 2, name: "Port C Status" },
              {bits: 2, name: "Port D Status" },
              {bits: 12, name: "Analog IO Dir." },
              {bits: 2, name: "HARP Conf." },
              {bits: 16, name: "GPIO Dir." }
            ],
            config: {bits: 48, lanes: 8, vflip: true, hflip: true, fontsize: 11}
        }

    which are defined as follows:

    - Acq. Running: Host hardware run state. 0 = not running, 1 = running
    - Acq. Reset Done: Host reset state. 0 = reset not complete, 1 = reset
      complete
    - Reserved: NA
    - LED Level: 4 bit register for general LED brighness. 0 = dimmest, 16 =
      brightest
    - LED Mode: 2 bit register for LED mode. 0 = all off, 1 = only
      power/running, 2 = power/running, pll, harp, 3 = all on
    - Port X Status: 2 bit register describing the headstage port state. 00:
      power off, 01: power on, 10: locked, 11: device map good.
    - Analog IO Dir.: 12 bit register describing the direcitonality of each
      of the analog inputs. 0 = input, 1 = output.
    - HARP Config.: 2 bit register for possible future harp configuration.
    - GPIO Dir.: 16 bit register for possible future digital io
      directionality configuration.

Digital Out
    Digital output port state. Each bit represents state of an output signal
    line in the 8-bit port.

    - 0: Low
    - 1: High

A clock recovery circuit is required at the receiver to generate ``clk`` from
``sclk`` in order to sample the ``dat`` line.

.. _onidatasheet_fmc_digital_io_reg:

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
      - LEDMODE
      - R/W
      - Immediate
      - 0x0003
      - None
      - The two LSBs determine the breakout board's LED display mode:

        * 0b00: All off
        * 0b01: Power/running only
        * 0b10: Power, running, HARP, and Lock
        * 0b11: Normal

    * - 0x02
      - LEDLVL
      - R/W
      - On Reset
      - 0x0003
      - None
      - The four LSBs determine the overall LED brightness. Brightness
        increases linearly with this register's 0-15 value.

    * - 0x03
      - HARPCONF
      - R/W
      - On Reset
      - 0x0000
      - None
      - `HARP Bus <https://www.cf-hw.org/harp>`__ configuration. Reserved for future use.

    * - 0x04
      - GPIODIR
      - R/W
      - On Reset
      - 0x0000
      - None
      - GPIO configuration. Reserved for future use.

    * - 0x05
      - CLKHZ
      - R
      - N/A
      - N/A
      - None
      - The system clock frequency in Hz

    * - 0x06
      - SPACING
      - R/W
      - On Reset
      - 0x0000
      - None
      - Minimum CLK_HZ cycles between samples. Can be used to debounce inputs.
        Ignored if SAMPLING > 0.

    * - 0x07
      - SAMPLING
      - R/W
      - On Reset
      - 0x0000
      - None
      - If > 0, produce one sample with each SAMPLING value of the CLK_HZ clock.
        regardless of if there are changes in digital input state or not.

.. _onidatasheet_fmc_digital_io_d2h:

Device To Host Data Frames
******************************************
Each frame transmitted to the host consists of a single data specifying the
current digital input and user input state.

.. note::
   Input frames are only transmitted if there is a change in digital input or
   user input state.

.. wavedrom::

    {
        reg: [
          {bits: 64, name: "Acquisition Clock Counter", type: 0},
          {bits: 32, name: "Device Address", type: 0},
          {bits: 32, name: "Data Size", type: 0, attr: 12},

          {bits: 64, name: "Hub Clock Counter", type: 3},

          {bits: 8},
          {bits: 8, name: "Input Port State", type: 4},
          {bits: 6},
          {bits: 4, name: "Link State", type: 6},
          {bits: 6, name: "Button State", type: 5},
        ],
        config: {bits: 224, lanes: 7, vflip: true, hflip: true, fontsize: 11}
    }

.. wavedrom::

    {
        reg: [
          {bits: 64, name: "Acquisition Clock Counter", type: 0},
          {bits: 32, name: "Device Address", type: 0},
          {bits: 32, name: "Data Size", type: 0, attr: 10},

          {bits: 64, name: "Hub Clock Counter", type: 3},

          {bits: 8, name: "Status Codeword", type: 4},

          {bits: 5, name: "Reserved"},

          {bits: 1, name: "CV", type: 2},
          {bits: 1, name: "PP", type: 2},
          {bits: 1, name: "SL", type: 2},

          {bits: 16}

        ],
        config: {bits: 224, lanes: 7, vflip: true, hflip: true, fontsize: 11}
    }

|

Input Port State
    8-bit input port state

Link State
    On/off state of each headstage link.

Button State
    Press state of each button.

.. _onidatasheet_fmc_digital_io_h2d:

Host To Device Data Frames
******************************************
Each frame sent to the device contains an 8-bit word specifying the digital
output port state:

.. wavedrom::

    {
        reg: [
          {bits: 32, name: "Device Address", type: 0},
          {bits: 32, name: "Data Size", type: 0, attr: 4},

          {bits: 24},
          {bits: 8, name: "Output Port State", type: 4},
        ],
        config: {bits: 96, lanes: 3, vflip: true, hflip: true, fontsize: 11}
    }

|

Output Port State
    8-bit output port state
