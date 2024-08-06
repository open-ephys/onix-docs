.. |software_logo| image:: /_static/noun_macbook.svg
  :height: 60

.. _software:

.. toctree::
    :hidden:

    oni-repl/index
    Onix Bonsai Library <onix1>
    Open Ephys GUI/index
    Bonsai.ONIX (DEPRECATED) <Bonsai.ONIX/index>

|software_logo| Software Guide
===================================

Although ONIX is software agnostic, we have focused our development efforts on `Bonsai <https://bonsai-rx.org/>`__ for data acquisition. Bonsai is
very good at dealing with the asynchronous and heterogeneous data that ONIX
hardware produces.

- The :ref:`oni_repl` pages document a low-level C program that
  can be used for debugging and basic streaming IO with ONIX
  hardware.
- The `OpenEphys.Onix1 <https://open-ephys.github.io/onix1-bonsai-docs/index.html>`__ pages detail how to use the ONIX Bonsai library.
- The :ref:`open_ephys_gui` page shows how ephys data can be streamed the Open
  Ephys GUI to take advantage of its excellent visualization capabilities.

Deprecated
-----------

- The :ref:`bonsai_onixref` pages provide detailed information about the deprecated ONIX
  Bonsai library. 


.. tip:: If you want to use ONIX hardware with your acquisition software,
    please :ref:`get in touch <support>`. It's not as hard as you might think
    :).
