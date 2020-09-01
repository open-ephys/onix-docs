.. _liboni:
.. |year| date:: %Y

liboni
##########################################
C implementation of the `Open Neuro Interface API Specification
<https://github.com/open-ephys/ONI>`_

.. toctree::
    :maxdepth: 1
    :hidden:

    onidefs
    oni
    onidriver
    onix
    build
    liboni-example
    making-drivers

Source Code
********************************************
Source code is available in the `liboni git repository <https://github.com/jonnew/liboni/tree/main/api/liboni>`_.

Scope and External Dependencies
********************************************
``liboni`` is a C library that implements the `ONI API Specification
<https://github.com/open-ephys/ONI>`_. It is written in C to facilitate cross
platform and cross-language use. It is composed of the following files:

#. :ref:`onidefs.h`: common definitions
#. :ref:`oni.h`: core API
#. :ref:`onidriver.h`: device driver translation layer that must be
   implemented for a particular host hardware connection and
   firmware.
#. ``ondriverloader.h``: functions used for dynamically loading the hardware
   driver. This is used internally by the :ref:`oni.h` and can be ignored
   during both software and driver development.
#. :ref:`onix.h`: ONIX-specific, out of ONI API specification
   scope, definitions and functions. Can be ignored for projects that
   do not interact with ONIX hardware.

``liboni`` is a low level library intended for use by high-level language
binding and/or software plugin developers. The only external dependency aside
from the C standard library and dynamic library loading functions is is a
device driver translation layer (:ref:`onidriver.h`, "driver" for short) that
fulfills the requirements of the ONI Host Interconnect Specification. Our API
implementation contains drivers for

#. `RIFFA <https://github.com/KastnerRG/riffa>`_ is a free and open-source,
   FPGA IP core and device driver that allows the ONI communication channels to
   be implemented using the PCIe bus. **Open Ephys hardware uses RIFFA.**
#. `Xillybus <http://xillybus.com/>`_ is a proprietary FPGA IP cores and free
   and open source device drivers to allow the communication channels to be
   implemented using the PCIe bus. The licensing terms for the FPGA core are
   extremely unclear, although "trial" use is allowed. Use at your own risk.
#. FTDI USB3.0: Planned
#. Opal-Kelly USB3.0: Planned

From the API's perspective, hardware communication abstracted to IO system
calls (``open``, ``read``, ``write``, etc.) on file descriptors. File
descriptor semantics and behavior are identical to either normal files
(configuration channel) or named pipes (signal, data input, and data output
channels).  Importantly, the low-level synchronization, resource allocation,
and logic required to use the hardware communication backend is implicit to
``liboni`` API function calls. Orchestration of the communication backend is
not directly managed by the library user.

License
********************************************
`MIT <https://en.wikipedia.org/wiki/MIT_License>`_
