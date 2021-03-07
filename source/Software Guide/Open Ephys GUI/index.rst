.. _open_ephys_gui:

Open Ephys GUI
===================

Where is the ONIX Plugin?
---------------------------------------------
There is currently no dedicated ONIX plugin available for the `Open Ephys GUI
<https://open-ephys.github.io/gui-docs/index.html>`__. There is a simple but
compelling reason for this: the Open Ephys GUI is built on top of an audio
processing library that has trouble dealing with asynchronous data streams.

.. note:: Have a look at the `Open Ephys GUI documentation
    <https://open-ephys.github.io/gui-docs/User-Manual/Before-you-begin.html>`_
    for some history on the GUI's design.

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
There are currently some areas where the Bonsai Editor **doesn't shine**. One
of the most glaring is its primitive ephys visualization capabilities. Bonsai
provides advanced access to GPU visualization capabilities, but this has to be
manually configured and can be a hurdle for those that just want to see if they
have their probe in the right spot. In the future, we aim to change this
situation, and eventually provide first-class native ephys visualization
capabilities right in the Bonsai Editor.

.. note:: If you want to help improve Bonsai's Ephys visualization capabilites,
    :ref:`get in touch <support>`.

In the meantime, for the practicing electrophysiologist, the Open Ephys GUI
provides superior plug-and-play ephys visualization and audio streaming
capabilities than Bonsai. We can take advantage of these capabilities by using
the Open Ephys GUI's `Ephys Socket Plugin
<https://open-ephys.github.io/gui-docs/User-Manual/Plugins/Ephys-Socket.html>`__
to receive data from Bonsai
