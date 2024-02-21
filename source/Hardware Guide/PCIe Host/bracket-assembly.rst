.. _pcie_host_bracket_assembly:

:orphan:

.. toctree::
    :hidden:
    
PCIe Bracket Assembly
########################################

The :ref:`pcie_host` host has a 3D printed front panel/bracket. This exposes
the PCIe Host IO and allows the device to be mounted in a standard PCIe slot.

Materials
-----------------------------------------
.. list-table:: Bill of materials
    :widths: 30 10 20 40
    :header-rows: 1

    * - Part
      - Qty
      - Part No.
      - Notes
    * - 3D printed bracket
      - 1
      - `STL file <https://github.com/open-ephys/onix-fmc-host/blob/main/mechanical/pcie-bracket-3dprint/stl/pcie-bracket-1p27mm.STL>`__
      - Sintered Nylon. Glass-bead reinforced is even better
    * - 3mm light pipe
      - 2
      - PLPC3-125
      -
    * - 5mm RGB LED
      - 2
      - HV-5RGB60
      -
    * - Ribbon cable
      - 0.5
      - A08SUR08SUR32W203A
      - Cut into two 8mm long pieces
    * - Heat shrink
      -
      -
      - 8 segments, ~1.5mm ID before shrinking

Tools and consumables
   - 5-minute epoxy
   - Soldering iron
   - Heat gun

Insert the PCIe Host Module
---------------------------------------
#. Get the required parts.

   .. image:: /_static/images/pcie-bracket/pcie-bracket_parts.jpg
        :alt: Bracket parts
        :align: center
        :width: 70%

#. Coat the inside of the light-pipe holes and LED sockets with a very small
   amount of 5 minute epoxy. Insert the light pipes from the front until flush
   with the face of the bracket. Insert the LEDs from the back (the holes are
   keyed).

   .. image:: /_static/images/pcie-bracket/pcie-bracket_light-pipes.jpg
        :alt: Bracket with light-pipes and LEDs inserted.
        :align: center
        :width: 70%

#. Cut the LED leads to about 4 mm in length

   .. image:: /_static/images/pcie-bracket/pcie-bracket_cut-leads.jpg
        :alt: Cutting the leads of LEDs
        :align: center
        :width: 70%

#. Cut the ribbon cable in to two 8 cm segments. Strip the wires on one of
   them. Slip heat shrink segments over each of the 8 wires.

   .. image:: /_static/images/pcie-bracket/pcie-bracket_cut-ribbon.jpg
        :alt: 8 cm ribbon cable
        :align: center
        :width: 70%


#. Solder the wires to the LED leads in the orientation shown below. Note the
   plug orientation. Slip the tube segments over the solder joint and shrink
   with heat gun.

   .. image:: /_static/images/pcie-bracket/pcie-bracket_finished.jpg
        :alt: 8 cm ribbon cable
        :align: center
        :width: 70%
