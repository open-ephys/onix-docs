.. _drivers:

Hardware Translation Layers
#######################################
There are a many existing `device drivers
<https://en.wikipedia.org/wiki/Device_driver>`_ that are designed to support
hardware for data acquisition. Some of these are appropriate to be used as a
hardware backend for ONI-compliant APIs. Specifically, this is true if they
provide some means to support the required hardware communication channels:

- High-speed data in
- High-speed data out
- Low speed signal In
- Register Programming

Have a look at the `ONI Spec <https://github.com/open-ephys/ONI>`_ for more
exact specifications of these communication channels.  

An ONI translation layers implement `onidriver.h
<https://github.com/jonnew/liboni/blob/main/api/liboni/onidriver.h>`_ to
convert routines in existing, potentially proprietary, device drivers (and
corresponding hardware) into a user space library that can be consumed by
ONI-compliant APIs. These are loaded by the API dynamically at runtime and
therefore are separate form the API both in terms of development and licensing
requirements. The APIs agnosticism to hardware its most powerful features
because it means it can be use for third party hardware without reinventing the
wheel.

ONIX hardware translation layer implementations are documented here. Have a
look at the following links for more information on each. :ref:`Get in touch
<support>` if you want to write a driver to give your hardware automatic access
to our API and software.

.. toctree::
    :maxdepth: 1

    test
    riffa
    xillybus
