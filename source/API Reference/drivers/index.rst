.. _drivers:

Driver Translators
#######################################
There are a many existing `device drivers
<https://en.wikipedia.org/wiki/Device_driver>`_ that support hardware for data
acquisition. Some of these drivers can be used as a backend for ONI-compliant
APIs if they provide some means to support the required ONI communication
channels. Have a look at the `ONI Spec <https://github.com/open-ephys/ONI>`_
for specifications of these channels.

An ONI hardware driver translator implements `onidriver.h
<https://github.com/open-ephys/liboni/blob/main/api/liboni/onidriver.h>`_ to
convert, potentially proprietary, device drivers (and corresponding hardware)
into a user space library that can be consumed by ONI-compliant APIs. These are
loaded by the API at runtime and therefore are separate from the API both in
terms of development and licensing requirements.

ONIX driver translator implementations are documented here. Have a
look at the following links for more information on each. :ref:`Get in touch
<support>` if you want to write a driver translator to give your hardware
automatic access to our API and software.

.. toctree::
    :maxdepth: 1

    test
    riffa
    ft600
    xillybus
