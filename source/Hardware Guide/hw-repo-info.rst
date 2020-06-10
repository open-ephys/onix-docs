.. _hardware_repo_info:
.. |year| date:: %Y

Repository Information
##################################
ONIX hardware designs follow some convetions, which are described below.

PCB Design Files
****************************
`Autodesk EAGLE <https://www.autodesk.com/products/eagle/overview>`_ PCB Design
files are located at the top directory of each hardware project:

- \*.sch = schematic
- \*.brd = board layout

.. note:: `KiCad <https://kicad-pcb.org/>`_ now includes native EAGLE to KiCad conversion
    if you wish to use that instead of EAGLE.

A PDF version of the schematic is also located at the top level of the top directory.

- \*_schematic.pdf = board layout

PCB Fabrication Files
****************************
PCB `gerber files <https://en.wikipedia.org/wiki/Gerber_format>`_ are defined as follows:

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
- \*.gvp = `gerbv <http://gerbv.geda-project.org/>`_ project file.

Gerber files for a board will be located in the ``gerber`` folder next to the board design.

If available, solder stencil gerber files are located in the ``sencil``
folder. Files within this folder are defined as follows:

- \*.CST = top-side stencil
- \*.SST = bottom-side stencil

For example, `here <https://github.com/jonnew/open-ephys-pcie/tree/master/eib-64/revisions/rev-1.2/gerber>`_ 
are the gerber files needed to create :ref:`eib_64_1r2`. In some cases, panelized versions of
the PCB will be avaiable in the ``gerber-panel`` and ``stencil-panel`` folders.

Bills of Materials
****************************
TODO

PCB Assembly Files
****************************
TODO
