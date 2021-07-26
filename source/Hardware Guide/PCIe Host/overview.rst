.. _pcie_host_overview:

Overview
#########################
The **ONIX PCIe Host** combines the `ONIX FMC Host
Module
<https://github.com/open-ephys/onix-fmc-host>`__
with the PCIe-connectivity and bulk-FPGA power
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

- Two deserailizers for any multifunction headstage conforming to the ONIX
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
with the ONIX FMC Host Board. It has a Kintex-7 FPGA, PCIe (Gen3 4x) bus, and 4
GB of RAM for PC-independent data buffering.

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
