.. _hardware_repo_info:

Hardware Repository Information
##################################
ONIX hardware design repositories follow some conventions that are described
below.

PCB Design Files
****************************
`Autodesk EAGLE <https://www.autodesk.com/products/eagle/overview>`__ PCB Design
files are located at the top directory of each hardware project:

- \*.sch = schematic
- \*.brd = board layout

.. note:: `KiCad <https://kicad-pcb.org/>`_ now includes native EAGLE to KiCad conversion
    if you wish to use that instead of EAGLE.

A PDF version of the schematic is also located at the top level of the top
directory:

- \*_schematic.pdf = board layout

PCB Fabrication Files
****************************
PCB `gerber files <https://en.wikipedia.org/wiki/Gerber_format>`__ are defined
as follows:

- \*.GKO = board outline
- \*.GTS = top solder mask
- \*.GBS = bottom solder mask
- \*.GTO = top silk screen
- \*.GBO = bottom silk screen
- \*.GTL = top copper
- \*.GnL = inner layer n copper
- \*.GBL = bottom copper
- \*.XLN[.xxyy] = drill hits and sizes. Files specifying blind or buried also
  specify start (xx) and end (yy) layers as additional extension.
- \*.gvp = `gerbv <http://gerbv.geda-project.org/>`__ project file.

Gerber files for a board will be located in the ``gerber`` folder next to the
board design.

If available, solder stencil gerber files are located in the ``sencil``
folder. Files within this folder are defined as follows:

- \*.CST = top-side stencil
- \*.SST = bottom-side stencil

For example, `here <https://github.com/jonnew/ONIX/tree/main/eib-64/revisions/rev-1.2/gerber>`_ 
are the gerber files needed to create :ref:`eib_64_1r2`. In some cases, panelized versions of
the PCB will be available in the ``gerber-panel`` and ``stencil-panel`` folders.

Bills of Materials
****************************
Each peice of hardware will have a bill of materials available on a google
sheet, which includes schematic-linked designators, quantities, manufacturer
part numbers, vendor part numbers. For instance, here is the `BOM for
headstage-64 v1.3 <https://docs.google.com/spreadsheets/d/1F-KWcdvH_63iXjZf0cgCfDiFX6XXW3qw6rlR8DZrFpQ/edit#gid=138167638>`__

Aside from a spreadsheet of electronic components, some boards may include the
following other materials information

- An interactive electronics BOM (e.g. like `this one
  <../_static/boms/headstage-64_1r3_bom.html>`__ for :ref:`headstage_64_1r3`)
- Lists of mechanical components that need to be machined, 3D-printed, and/or
  assembled (e.g. for breakout boards)

.. note:: Common parts (e.g. standard surface mount resistors and capacitors)
    may lack manufacturer and vendor part numbers. This is because the distribution
    turnover of these kinds of parts is so high that maintaining part numbers is a
    fools errand.

PCB Assembly Files
****************************
.. todo:: Document
