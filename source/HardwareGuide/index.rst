.. |hw_logo| image:: /_static/noun_pcb.svg
  :height: 60

.. _hardware_guide:

|hw_logo| Hardware Guide
==========================================
ONIX consists of several hardware devices:

.. attention:: ONIX hardware version compatibility
    is documented on `this google sheet
    <https://docs.google.com/spreadsheets/d/1LwEOlOkL_HJKeTmNJFVIlItzVeCZDzOt_9Up_rA36Ic/edit?usp=sharing>`_.

.. toctree::
    :maxdepth: 1
    :hidden:

    PCIeHost/index
    BreakoutBoard/index
    Headstages/index
    Miniscopes/index
    Commutators/index
    Lighthouses/index
    Adapters&EIBs/index
    Datasheets/index
    Connections&Cables/index

:ref:`PCIe Host<pcie_host>`
-----------------------------------------
The ONIX PCIe/FMC host device is the heart of ONIX. It provides the interface
between the acquisition computer and any attached headstages, as well as
digital and analog in/outputs. Most acquisition systems communicate via USB,
but this board sits directly in a PCIe slot in the acquisition computer. This
greatly increases the speed of communication between ONIX and the computer,
reducing closed-loop latencies.

The host can also generate a very precise clock that is synchronized to its
hardware.

:ref:`Breakout<breakout>`
-----------------------------------------
The Breakout Board facilitates user access to the functionality of the host
board. On the Breakout Board, the analog channels and digital lines of the host
board are split out into individual connectors. This is where users can, for
instance, connect external devices for acquisition and synchronisation. The
buttons can be user-configured to provide signals to ONIX when pressed.

Headstages can be connected directly to the host, or with an SMA connection
first to the Breakout Board and then to the host. The same can be done to
access the host clock output.

:ref:`Headstages<headstages>` & :ref:`Miniscopes<miniscopes>`
--------------------------------------------------------------------
ONIX headstages communicate with the host board through a coaxial cable, that
can be kept very thin and light. Rather than just pre-amplifying data, ONIX
headstages perform many tasks on the headstage itself. The 64-channel
headstage, for instance, can locally drive an LED or provide current
stimulation, without the need for an external device and an additional fiber or
cable to the animal. UCLA Miniscopes are also directly compatible with ONIX.

:ref:`Commutators<commutators>`
-----------------------------------------
The active commutator is optional, but very useful for experiments with
freely-moving animals. The commutator responds to the orientation sensor in the
headstage or miniscope. When the animal turns, the commutator can actively turn
a rotary joint, precisely counteracting the rotation of the animal and
preventing twisting of the tether.

:ref:`Lighthouses<lighthouses>`
-----------------------------------------
Lighthouses or 'base stations' are positioned above the setup. They emit either
a vertical or horizontal laser plane that sweeps over the setup. Trackable ONIX
headstages contain infrared diodes that detect this light, allowing the spatial
position of the photodiode to be determined.

:ref:`Adapters & EIBs<adapters_eibs>`
-----------------------------------------
Several adapters and EIBs exist to interface between ONIX and
microwire or silicon probes, as well as an adapter for Omnetics-based
EIBs and the Nano-Z.
