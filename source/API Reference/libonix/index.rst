.. _libonix:
.. |year| date:: %Y

``libonix``
##########################################
ANSI C implementation of the `Open Neuro Interface API Specification
<https://github.com/open-ephys/ONI>`_

.. toctree::
    :maxdepth: 1

    libonix-ref
    libonix-example

Scope and External Dependencies
********************************************
``libonix`` is a C library that implements the `ONI API Specification
<https://github.com/open-ephys/ONI>`_. It is written in C to facilitate cross
platform and cross-language use.It is composed of the following files:

#. ``oni.h`` and ``oni.c``: core API implementation
#. ``onidevice.h`` and ``onidevices.c``: Open Ephys supported device and
   register definitions. This file can be ignored for projects that do not wish
   to conform to the official device specification. the core API implementation
   is not dependent on it.
#. ``ondriverloader.h`` and ``onidriverloader.c``: functions for dynamically
   loading hardware translation driver.
#. ``onidriver.h``: hardware translation driver header that must be implemented
   for a particular host hardware connection and firmware.

``libonix`` is a low level library intended for use by high-level language
binding and/or software plugin developers. It is not meant to be used by
neuroscientists directly. The only external dependency aside from the C
standard library and dynamic library loading functions is is a hardware
translation driver ("driver") that fulfills the requirements of the ONI Host
Interconnect Specification.  This implementation contains drivers for

#. `RIFFA <https://github.com/KastnerRG/riffa>`_ is a free and open-source,
   FPGA IP core and device driver that allows the ONI communication channels to
   be implemented using the PCIe bus. **Open Ephys hardware uses RIFFA.**
#. `Xillybus <http://xillybus.com/>`_ is a proprietary FPGA IP cores and free
   and open source device drivers to allow the communication channels to be
   implemented using the PCIe bus. The licensing terms for the FPGA core are
   extremely unclear, although "trial" use is allowed. Use at your own risk.
#. FTDI USB3.0: TODO
#. Opal-Kelly USB3.0: TODO

From the API's perspective, hardware communication abstracted to IO system
calls (``open``, ``read``, ``write``, etc.) on file descriptors. File descriptor
semantics and behavior are identical to either normal files (configuration
channel) or named pipes (signal, data input, and data output channels).
Importantly, the low-level synchronization, resource allocation, and logic
required to use the hardware communication backend is implicit to ``libonix`` API
function calls. Orchestration of the communication backend is not directly
managed by the library user.

License
********************************************
`MIT <https://en.wikipedia.org/wiki/MIT_License>`_

Build in Linux
********************************************

For build options, look at the top level ``Makefile``. To build and install:

.. code-block:: console

    $ make <options>
    $ make install PREFIX=/path/to/install

to place headers in whatever path is specified by ``PREFIX``. ``PREFIX`` defaults to
``/usr/lib/include``. You can uninstall (delete headers and libraries) via

.. code-block:: console

    $ make uninstall PREFIX=/path/to/uninstall

To make a particular driver, navigate to its location within the ``drivers``
subdirectory and:

.. code-block:: console

    $ make <options>
    $ make install PREFIX=/path/to/install

Then update dynamic library cache via:

.. code-block:: console

    $ ldconfig

Performance Testing
--------------------------------------------

Install google perftools:

.. code-block:: console

    $ sudo apt-get install google-perftools

Check what library is installed:

.. code-block:: console

    $ ldconfig -p | grep profiler

If ``libprofiler.so`` is not there, but ``libprofiler.so.x`` exists, create a softlink:

.. code-block:: console

    $ sudo ln -rs /path/to/libprofiler.so.x /path/to/libprofiler.so

Link test programs against the CPU profiler:

.. code-block:: console

    $ cd libonix-test
    $ make profile

Run the `firmware` program to serve fake data. Provide a numerical argument
specifying the number of fake frames to produce. It will tell you how long it
takes `host` to sink all these frames. This is host processing time + UNIX pipe
read/write.

.. code-block:: console

    $ cd bin
    $ ./firmware 10e6


Run the `host` program while dumping profile info:

.. code-block:: console

    $ env CPUPROFILE=/tmp/host.prof ./host

Examine output

.. code-block:: console

    $ pprof ./host /tmp/host.prof

Memory Testing
--------------------------------------------

Run the `host` program with valgrind using full leak check

.. code-block:: console

    $ valgrind --leak-check=full ./host

Build in Windows
********************************************
Open the included `Visual Studio
Coummunity <https://visualstudio.microsoft.com/vs/community/>`_ solution and
press play. For whatever reason, it seems that the startup project is not
consistently saved with the solution.  So make sure that is set to
``libonix-test`` in the solution properties.
