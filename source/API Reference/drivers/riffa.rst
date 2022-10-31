.. _riffa:

riffa
#######################################
`RIFFA <https://github.com/KastnerRG/riffa>`__ is an open-source FPGA core and
kernel driver that abstracts PCIe communication and allows easy integration
into C/C++ programs. RIFFA is currently the PCIe backend used by ONIX hardware.

.. note:: Currently, we are only supporting 64-bit architectures with a RIFFA
    backend.

Building the library
---------------------------------------

Linux
=======================================

.. code::

    make                # Build without debug symbols
    sudo make install   # Install in /usr/local and run ldconfig to update library cache
    make help           # list all make options


Windows
=======================================
Run the project in Visual Studio. It can be included as a dependency in other
projects.

Obtaining Host Device Driver
---------------------------------------
The RIFFA device driver is available in the `drivers` folder at the top level
of this repo. We have modified this slightly compared to the original driver so
you should use this. You can compile it from source, but we have also included
pre-compiled binaries that can be installed in Windows or Linux. This driver
must be installed before using the RIFFA backend.
