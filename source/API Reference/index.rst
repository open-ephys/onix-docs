.. |api_image| image:: ../_static/noun_books.svg
  :height: 60

.. _api_ref:

|api_image| API Reference
==========================================

.. toctree::
    :hidden:
    :maxdepth: 2

    liboni/index
    cpponi/index
    clroni/index
    drivers/index

ONIX APIs are high-performance software interfaces for host computer
interaction with ONIX hardware. ONIX API implementations are compliant with the
`Open Neuro Interface Specification <https://github.com/open-ephys/ONI>`_.
These APIs are simple and have minimal external dependencies. Therefore, they
are aimed at the creation of higher level language bindings and/or integration
into existing acqusition software.

- :ref:`liboni` is an ANSI-C implementation of the `ONI API Specificaiton
  <https://github.com/jonnew/ONI>`_ It contains functions for configuring
  hardware, streaming data to and from hardware, and controlling hardware
  during operation.
- :ref:`cpponi` are C++14 bindings for :ref:`liboni`.
- :ref:`clroni` are CLR/.NET bindings for :ref:`liboni`.
- :ref:`drivers` are ONIX device driver implementations
