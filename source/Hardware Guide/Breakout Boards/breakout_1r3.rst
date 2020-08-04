.. _breakout_1r3:
.. |year| date:: %Y

breakout v1.3
#########################
**breakout v1.3** allows bench access to the IO provided by the
following host boards

- :ref:`fmc_host_1r3`
.. - :ref:`fmc_host_1r4`

.. todo:: Image of breakout v1.3 with callouts

.. note:: There may be more IO present on the breakout board than is available
    on a particular host board. For instance, :ref:`fmc_host_1r3` has two coaxial
    links, but the breakout board provides four. This is is by design. The breakout
    is compatible with all host configurations.

Features
****************
breakout v1.3 provides access to the following IO:

- 4x headstage port feed-throughs, each with a power switch
- 3x, passive, high-speed clock feed-throughs
- 12x passive, ESD-protected, analog feed-throughs.
- BNC, ribbon, or direct wire access to 12 analog inputs or outputs
- Ribbon cable or direct, wire-access to 8 digital outputs and 8 digital
  inputs. These are 5V compliant.
- `HARP bus <https://www.cf-hw.org/harp>`__ controller

Additionally, breakout v1.3 has the following features:

- Lots of indication LEDs
- 6 buttons for marking experimental events for communication and programming.
- Rugged M6 and 1/4-20 mounting holes for both metric and imperial optical
  tables
- 19" rack compatibility

This board is essentially passive. It works in coordination with a host board
which determines its detailed functionality via its connectivity with the
breakout board along with the firmware running on the host. For every host, all
IO is carried through the following connections:

.. todo:: Image of right-angle cabling pinout

Refer to the host documentation for a detailed description of how each of these
signal lines are acquired.

Bill of Materials
****************************
- The interactive BOM is `here <../../_static/breakout-1r3_bom.html>`_
- The complete BOM (including vendor part numbers) is located on `this google
  sheet
  <https://docs.google.com/spreadsheets/d/18WfmbLGt8bGUUdksKp6AKA_wMX2SJ3Tndin-nnEgUCs/edit?usp=sharing>`_

License
****************************
Copyright Jonathan P. Newman |year|

This documentation describes Open Hardware and is licensed under the
CERN OHL v.1.2.

You may redistribute and modify this documentation under the terms of the CERN
OHL v.1.2. (http://ohwr.org/cernohl). This documentation is distributed WITHOUT
ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING OF MERCHANTABILITY, SATISFACTORY
QUALITY AND FITNESS FOR A PARTICULAR PURPOSE. Please see the CERN OHL v.1.2 for
applicable conditions
