.. _riffa:

riffa
#######################################
`RIFFA <https://github.com/KastnerRG/riffa>`__ is an open-source FPGA core and
kernel driver that abstracts PCIe communication and allows easy integration
into C/C++ programs. We maintain a `fork of the RIFFA driver
<https://github.com/open-ephys/liboni/tree/main/drivers/riffa>`__. RIFFA is
currently the PCIe backend used by ONIX hardware.

.. note:: Currently, only 64-bit architectures are supported by RIFFA.

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

.. note:: The :ref:`downloads` page contains :ref:`pre-compiled versions of RIFFA
    driver <riffa_driver_download>`
