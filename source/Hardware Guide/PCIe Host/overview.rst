.. _pcie_host_overview:

Overview
#########################
The **ONIX PCIe Host** combines the `ONIX FMC Host Module
<https://github.com/open-ephys/onix-fmc-host>`__ and the PCIe-connectivity
provided by the `Numato Nereid
<https://numato.com/product/nereid-kintex-7-pci-express-fpga-development-board/>`__
carrier board.

.. figure:: /_static/images/pcie-host/host-board_edited_callouts.jpg   
    :align: center
    :width: 500px

- Acquire from two headstages (or miniscopes)
- Breakout board connectivity

  - 8x digital inputs
  - 8x digital outputs
  - 12x analog outputs or inputs (±10V)

- Multi-board synchronization and triggering to increase number of headstages
  and IO
- Low-latency closed-loop capabilities (headstage dependent;
  typically < 100 µs)

Host Module
-------------------------
The `ONIX FMC Host <https://github.com/open-ephys/onix-fmc-host>`__ module
provides a host interface for serialized headstages and miniscopes, as well as
general purpose analog and digital IO. It is a VITA-57.1 compliant mezzanine
board that uses high pin-count FMC connector. In combination with a base FPGA
board , it provides host PC communication.

.. figure:: /_static/images/todo.jpg
    :align: center

    The ONIX FMC Host module.

- Two deserializers for any multifunction headstage conforming to the ONIX
  serialization protocol
- 12x ±10V analog outputs or inputs. Direction selected via analog switch
  controllable over the FMC connector. 
- Analog output are always looped back using the analog inputs.
- 3x high speed LVDS input pairs
- 2x high speed LVDS outputs pairs
- 2x high speed, arbitrary logic-level, singled-ended Hi-Z or 50-ohm clock inputs
- 1x high speed single ended, 50-ohm clock output
- 4x MLVDS input or output trigger lines

Numato Nereid
-------------------------
The `Numato Nereid
<https://numato.com/product/nereid-kintex-7-pci-express-fpga-development-board/>`__
is a VITA-57 compliant high-density FMC carrier module, which is compatible
with the ONIX FMC Host Board. It has a Kintex-7 FPGA, PCIe bus (Gen2 4x), and 4
GB of RAM for PC-independent data buffering. Our gateware bypasses this RAM
when its not needed for maximum close-loop performance.

.. figure:: /_static/images/pcie-host/nereid-callouts.png
    :align: center

    The Numato Nereid Kintex-7 PCIe/FMC carrier module (`image source
    <https://numato.com/product/nereid-kintex-7-pci-express-fpga-development-board/>`__).

PCIe Stack
-------------------------
We are using a slightly modified `version
<https://github.com/aacuevas/riffa>`__ of the excellent, open-source `RIFFA
<https://github.com/KastnerRG/riffa>`__ project to orchestrate data
transmission over the PCIe bus. The PCIe protocol implementation and physical
interface is provided by a `hard block
<https://www.xilinx.com/products/intellectual-property/7_series_pci_express_block.html>`_
in the Kintex-7 FPGA.

.. centered:: Riffa License

::

  Copyright (c) 2016, The Regents of the University of California All
  rights reserved.

  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions are
  met:

      * Redistributions of source code must retain the above copyright
        notice, this list of conditions and the following disclaimer.

      * Redistributions in binary form must reproduce the above
        copyright notice, this list of conditions and the following
        disclaimer in the documentation and/or other materials provided
        with the distribution.

      * Neither the name of The Regents of the University of California
        nor the names of its contributors may be used to endorse or
        promote products derived from this software without specific
        prior written permission.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL REGENTS OF THE
  UNIVERSITY OF CALIFORNIA BE LIABLE FOR ANY DIRECT, INDIRECT,
  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
  OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
  TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
  USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
  DAMAGE.