.. |software_logo| image:: /_static/noun_macbook.svg
  :height: 60

.. _software:

|software_logo| Software Guide
===================================

.. toctree::
    :hidden:

    Bonsai.ONIX/index
    Bonsai Examples/index

ONIX uses `Bonsai <https://bonsai-rx.org/>`__ for data acquisition. Bonsai is
very good at dealing with the asynchronous and heterogeneous data that ONIX
hardware produces.

    - The :ref:`bonsai_onixref` pages provide detailed information about the
      ONIX Bonsai library. 
    - The :ref:`bonsai_onixexamples` pages provide example Bonsai.ONIX
      workflows 

.. tip:: If you want to use ONIX hardware with your acquisition software,
    please :ref:`get in touch <support>`. It's not as hard as you might think
    :).

.. _open_ephys_gui:

Where is the Open Ephys GUI Plugin?
---------------------------------------------
There is currently no dedicated ONIX plugin available for the `Open Ephys GUI
<https://open-ephys.github.io/gui-docs/index.html>`__.  The Open Ephys GUI is
built on top of an audio processing library that has trouble dealing with
asynchronous data streams.

.. note:: Have a look at the `Open Ephys GUI documentation
    <https://open-ephys.github.io/gui-docs/User-Manual/Before-you-begin.html>`_
    for information on the GUI's design.

This is fine when the data being processed is synchronized ephys and auxiliary
data. However, by design, ONIX hardware makes no such guarantees about the
nature of the data it produces. On the contrary, an
:ref:`oni_h_acquisition_context` manages a table of devices that are
potentially all asynchronous from one another. Even though each sample from
these devices is individually time-stamped in hardware, there is no guarantee
of when they will arrive or in what order. This necessitates the use of
event-driven acquisition software that only propagates data when its received,
and this is where `Bonsai <https://bonsai-rx.org/>`__ really shines. For this
reason, we have dedicated the majority of our development effort toward the
:ref:`Bonsai.ONIX <bonsai_onixref>` library.

Using the Open Ephys GUI for ONIX Data Visualization
--------------------------------------------------------------
Bonsai provides advanced access to GPU visualization capabilities, but has to
be manually programmed to generate high performance real-time plotting. Thiscan
be a hurdle for those that just want to see if they have their probe in the
right spot. In the future, we aim to change this situation, and eventually
provide first-class native ephys visualization capabilities in the Bonsai
Editor.

.. note:: If you want to help improve Bonsai's Ephys visualization capabilites,
    :ref:`get in touch <support>`.

In the meantime we can take advantage of the Ephys GUI's visualization and
audio streaming by the `Ephys Socket Plugin
<https://open-ephys.github.io/gui-docs/User-Manual/Plugins/Ephys-Socket.html>`__
to receive data from Bonsai.
