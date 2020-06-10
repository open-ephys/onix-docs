.. _api_ref:

API Reference
==========================================

.. toctree::
    :hidden:
    :maxdepth: 2

    libonix/index
    cpponix/index
    clronix/index

The ONIX APIs are high-performance software interface for host computer
interaction with ONIX hardware. API implementations are compliant with the
`Open Neuro Interface Specification <https://github.com/open-ephys/ONI>`_.
These APIs are simple and has minimal external dependencies. Therefore, they
are aimed at the creation of higher level language bindings and/or integration
into existing acqusition software.

- :ref:`libonix` is an ANSI-C implementation of the `ONI API Specificaiton
  <https://github.com/jonnew/ONI>`_ It contains functions for configuring
  hardware, streaming data to and from hardware, and controlling hardware
  during operation.
- :ref:`cpponix` are C++14 bindings for :ref:`libonix`.
- :ref:`clronix` are CLR/.NET bindings for :ref:`libonix`.

