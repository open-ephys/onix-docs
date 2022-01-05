.. _system_setup:

System Setup
==========================================

.. contents:: Table of Contents
  :depth: 2
  :local:

.. toctree::
    :maxdepth: 2

Installing and Testing
############################################

1) Install the PCIe board in the PC, along with relevant software, by following the :ref:`pcie_host_setup_windows`.

2) Mount 2 Vive Base Station Lighthouses over the setup (height range)

- Connect one power adaptor to each base station.
- Set one base station to 'A' and one to 'b' using the channel button (see the Vive manual`<https://www.vive.com/eu/support/vive/category_howto/about-the-base-stations.html>`_)
- Connect the basestations to each other, using an audio to audio cable (this is to synchronise them, see `image here <https://www.vive.com/media/filer_public/support_zip_img/eu/www/vive/guid-cba33494-fc82-4b81-84ae-735fcd6a5876-web.png>`_)

3) Mount the active commutator above the setup (you can use the same frame as the base stations).

- Connect the commutator to the computer using a USB to micro-USB cable

.. note::
  Add how to test commutator in Bonsai?

4) Connect the Breakout Board to the Host using the high-speed digital cable

- Test Digital IO
- Test Buttons
- Test Analog IO

5) Connect headstages either directly to host or through the breakout board

The LED on the breakout board (and the PCIe board itself, if visible) should turn purple when the link is made between the headstage and the PCIe host board.
Double-clicking on the OniContext node in Bonsai should now show an additional tab, labelled with the type of headstage. 
