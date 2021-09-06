.. |api_image| image:: /_static/noun_books.svg
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

The ONIX API, :ref:`liboni`, is a high-performance software interface for
interaction with ONIX, and other ONI-compliant, hardware. The API is compliant
with the `Open Neuro Interface Specification
<https://github.com/open-ephys/ONI>`_. It has minimal external dependencies and
is aimed at the creation of higher level language bindings and/or integration
into existing acquisition software.

- :ref:`liboni` is an ANSI-C implementation of the `ONI API Specificaiton
  <https://github.com/open-ephys/ONI>`_. It contains functions for configuring
  hardware, streaming data to and from hardware, and controlling hardware
  during operation.
- :ref:`cpponi` is C++ bindings for :ref:`liboni`.
- :ref:`clroni` is CLR/.NET bindings for :ref:`liboni`.
- :ref:`drivers` describes device drivers that can be used with ONIX APIs to
  control hardware.

Source Code
---------------------
The API (and bindings) source code is available here:
https://github.com/open-ephys/liboni.
