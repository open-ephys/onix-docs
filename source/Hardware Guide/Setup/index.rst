.. _system_setup:

Hardware System Setup
==========================================

.. toctree::
    :maxdepth: 2

    Connections and Cables 


PCIe and computer
--------------------------------

* Install the PCIe board in the PC, along with relevant software, by following the :ref:`pcie_host_setup_windows`.


Lighthouse Base Stations
--------------------------------

* Mount 2 Vive Base Station Lighthouses over the setup.
   - Connect one power adaptor to each base station.
   - Set one base station to 'A' and one to 'b' using the channel button (see the `Vive manual <https://www.vive.com/eu/support/vive/category_howto/about-the-base-stations.html>`_)
   - Connect the basestations to each other, using an audio to audio cable (this is to synchronise them, see `image here <https://www.vive.com/media/filer_public/support_zip_img/eu/www/vive/guid-cba33494-fc82-4b81-84ae-735fcd6a5876-web.png>`_)

Commutator
--------------------------------

Mount the active commutator above the setup (you can use the same frame as the base stations).

- Connect the commutator to the computer using a USB to micro-USB cable

.. note::
  Add how to test commutator in Bonsai?

Breakout Board
--------------------------------

The breakout board can be mounted on a rack.

Connect the breakout board to the PCIe host board using the high-speed digital cable.

.. note::
  - Test Digital IO
  - Test Buttons
  -  Test Analog IO

Headstages/other devices
--------------------------------

* Connect the headstages either directly to host or through the breakout board (see headstage link).
   - The LED on the breakout board (and the PCIe board itself, if visible) should turn purple when the link is made between the headstage and the PCIe host board.
   - Double-clicking on the OniContext node in Bonsai should now show an additional tab, labelled with the type of headstage.
