.. _headstage_64_1r3:
.. |year| date:: %Y

headstage-64 v1.3
##############################
**headstage-64 v1.3** is an ONI-compatible, serialized, multifunction headstage for
small animals. This headstage is designed to function with :ref:`eib_64_1r3` for
`tetrode microdrives <https://open-ephys.org/shuttledrive>`_. Alternatively it can be used with other passive
probes (e.g. silicon arrays, flexible eeg arrays, etc) using
:ref:`omnetics_adapter_64_1r0` or similar.

.. todo:: This is a picture of revision 1.1!

.. image:: /asset/image/headstage-64.png
   :align: center

.. note:: Make sure to double check your headstage revision by looking at the
    silkscreen on the bottom of the headstage. You should see ``Rev1.3``. If not,
    refer the appropriate revision's documentation.

headstage-64 v1.3 is compatible with the following ONIX hardware

#. :ref:`eib_64_1r2`
#. :ref:`eib_64_large_1r0`
#. :ref:`omnetics_adapter_64_1r0`
#. :ref:`test_board_64_1r2`
#. :ref:`breakout_1r4`
#. :ref:`fmc_host_1r3`

Coaxial Link
***********************************
For details on ONI-compiant data serialiation and headstage gateware, have a
look at the :ref:`serialization` page, which describes how ONI-compliant
headstages operatate in general terms. Within this context, headstage-64 v1.3 has
the following coaxial link properties:

.. table::
    :widths: 50 80 50 50

    +------------------------+--------------------+----------+----------+
    | Parameter              | Value              | Max      | Unit     |
    |                        |                    |          |          |
    +========================+====================+==========+==========+
    | FPGA                   | Intel 10M08DFV81   |          |          |
    +------------------------+--------------------+----------+----------+
    | Serializer             | TI DS90UB933       |          |          |
    +------------------------+--------------------+----------+----------+
    | Coax Voltage           | 5.0                | 6.0*     | Volts    |
    +------------------------+--------------------+----------+----------+
    | PCLK Frequency         | 42                 |          | MHz      |
    +------------------------+--------------------+----------+----------+

.. warning:: \*Do not exceed 6VDC at the coaxial input to the headstage. Make
    sure you make this measurement at the headstage to account for a potential
    voltage drop in the tether. Exceeding this voltage can permanently damage the
    headstage.

.. note:: Have a look at the :ref:`tethers` page for more detials on mirco-coax
    headstage tethers

The following devices are accessible over the coaxial link:

#. 64 ephys channels and 3 auxiliary channels sampled at 30 kHz per channel
#. Real-time, mm-precision 3D-position tracking using Steam VR basestations (60
   Hz)
#. 9DOF absolute head orientation tracking (100 Hz)
#. An electrical stimulator (current controlled, +/-15V, electrode discharge)
#. 2x optical stimulators (800 mA per channel)

Electrophysiology
*******************
headstage-64 v1.3 uses a 64-channel, BGA-packaged `Intan RHD2164
<http://intantech.com/>`_ bioamplifier chip. This chip provides:

- 64 high-bandwidth electrode channels which are exposed via a mezzanine connector on the
  bottom of the headstage and can be used to record from most types of passive
  probes (e.g. tetrodes, silicon probe arrays, tungsten microwires, steel EEG
  wires, etc)
- 3 auxiliary channels

  - AUX 1 and 2 are pinned out on the bottom of the headstage to an unpopulated
    mezzanine connector and solder-able test points
  - Channel 3 is tied to the electrical stimulator's current measurement
    circuit via a selectable solder jumper on the bottom of the board. This
    jumper can be desoldered and instead a series resistor added to allow
    low-frequency LFP recordings as per pg. 26 of the RHD2000 datasheet.

Each of these channels is sampled at 30 kHz.

3D Position Tracking
**********************
.. warning:: TODO: Move this into its own page

headstage-64 v1.3 has four `SteamVR <https://store.steampowered.com/steamvr>`_
receivers for 3D position tracking.

.. warning:: These receivers are compatible with both V1 and V2 ("index" branded)
    basestations. Although the firmware we supply for the headstage can be used
    to obtain 3D position from kinds of basestation, we consider V1
    basestations deprecated and cannot guarantee future functionality.

Assuming you are using `V2
basestations <https://store.steampowered.com/app/1059570/Valve_Index_Base_Station/>`_,
to set up tracking,

#. Mount each of the basestations so that they have a clear line of sight to as
   much of the behavioral space as possible. For a relatively flat arena, the
   simplest configuration is to mount two basestations directly above the
   behavioral space inline and separated by 0.5 to 1 meters. For more complex
   environments more than 2 basestations are required to get full coverage, any
   configuration is possible so long 2 basestations have a line of site to the
   headstage and are no more than 4 meters away. For this, there are lots of
   options for ready-made, adjustable basestation mounts availble on Amazon and
   elsewhere.
#. Serial into each of the basestations using the USB connection on the back
   and set up a terminal connection using ``screen /dev/ttyACM0 115200`` or
   similar
#. Once connected you can hit Tab to see commands
#. Set the mode of of each base staiton to a different value using
   ``mode n`` where ``n`` is the desired mode (1-16). The only requirement is
   that each basestation have a unique mode.

.. note:: If a basestation loses power, it will reset to mode 1. Its best to
    just leave the basestations plugged in and untouched to minimize the need to
    for re-calibration and mode programming

#. TODO: obtain the position and orientation of each basestations

3D Orientation Tracking
*************************
headstage-64 v1.3 has a `BNO055
<https://www.bosch-sensortec.com/products/smart-sensors/bno055.html>`_ 9-axis
inertial measurement unit that provides the absolute orientation of the
headstage. This device produces orientation (and other) measurements are 100
Hz.

Neural Stimulation
****************************
headstage-64 v1.3 provides onboard electrical and optical stimulation. Stimulus
trains can be parameterized in a similar way to the master-8 or pulse pal.
Electrical and optical stimulus trains cannot be delivered simultaneously.
If there is a conflict, electrical stimuluation will take priority and optical
stimulus triggers will be ignored.

To achieve the shortest latency, electrical and optical stimulation can be triggered
using the GPIO1 serializer output. Because both stimulators share this trigger line,
it is important to only enable one of the devices (using its ENABLE register) prior
to toggling this pin.

Optical Stimulation
~~~~~~~~~~~~~~~~~~~~
Optical stimulation is provided by a dual-channel, high-current LED driver.
This driver can be used for LEDs or laser diodes. It provides 800-mA per
channel.

    :Q: Can I parallel the Cathode connections to increase max current?

    :A: Yes. The maximum peak current in 1.6 Amps. However, if you deliver this current for a significant amount of time, the headstage will shutdown due to an over-temperture condition. The optical stimulator is only appropriate for low duty-cycle pulse type stimulation.

Electical Stimulation
~~~~~~~~~~~~~~~~~~~~~~
The electrical stimulation cicuit is an improved Howland current pump followed by
an precision current measurement circuit. The current pump is supplied by +/-15V
rails and can supply up to +/- 2.5 mA. The output current is defined as:

.. code-block:: none

    ISTIM = (VDAC  - 2.5)/1000.
    e.g.
    VDAC = 2.5   -> ISTIM = 0
    VDAC = 5.0   -> ISTIM = 2.5 mA
    VDAC = 0.0   -> ISTIM = -2.5mA

.. code-block:: none

    Imeas = 400 * ISTIM + 1.25V
    e.g.
    ISTIM = 0      -> IMEAS = 1.25V
    ISTIM = 2.5mA  -> IMEAS = 2.25V
    ISTIM = -2.5mA -> IMEAS = 0.25V

Schematic
****************************
.. image:: /asset/image/headstage-64_schematic.png
   :align: center

Gerber Files
****************************
.. image:: /asset/image/headstage-64_gerbers.png
    :class: img-fluid

Bill of Materials
****************************

- The interactive BOM is `here <../../_static/headstage-64_1r3_bom.html>`__
- The complete BOM (including vendor part numbers) is located on `this google
  sheet
  <https://docs.google.com/spreadsheets/d/1F-KWcdvH_63iXjZf0cgCfDiFX6XXW3qw6rlR8DZrFpQ/edit#gid=138167638>`__


FPGA & Bottom Connector Pinouts
************************************

- The FPGA pinout is located on `this Google
  sheet <https://docs.google.com/spreadsheets/d/1oJoQ89dJNL9LIiTrRnwJ_9KGiLzJ53Tju5Lfchuvsb0/edit#gid=2100166621>`__

- The headstage connector pinout (ADC input mapping, stimulation connections,
  etc) is located on `this Google sheet <https://docs.google.com/spreadsheets/d/11wRDYOqHN5lPb03yUdfXfK0zvaDYsVetplaNK-R90Gg/edit#gid=663991061>`__

License
****************************
Copyright Jonathan P. Newman, Jakob Voigts |year|

This documentation describes Open Hardware and is licensed under the
CERN OHL v.1.2.

You may redistribute and modify this documentation under the terms of the CERN
OHL v.1.2. (http://ohwr.org/cernohl). This documentation is distributed WITHOUT
ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING OF MERCHANTABILITY, SATISFACTORY
QUALITY AND FITNESS FOR A PARTICULAR PURPOSE. Please see the CERN OHL v.1.2 for
applicable conditions
