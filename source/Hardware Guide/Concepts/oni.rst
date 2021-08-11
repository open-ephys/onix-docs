.. _oni_guide:

ONI vs. ONIX 
==========================================
`Open Neuro Interface <https://github.com/open-ephys/ONI>`__ is a hardware and
API specification designed to meet the needs of experimental neuroscientists.
ONIX hardware and `liboni <https://github.com/open-ephys/liboni>`__ are
implementations of the ONI specification. Some ONI concepts are useful for
understanding how to effectively use the ONIX system, so they are presented
here in a simplified form.

.. todo:: Finish documenting.

.. code::

    Host Computer
    |...||
    |   || Host Interconnect 0 
    |   ||
    |   |+-- Host 0 [Governed by a Context & generates a Host Device Table]
    |   |    |
    |   |    +-- Hub 0 [Generates a Hub Device Table]
    |   |    |   |
    |   |    |   | Port 0
    |   |    |   |
    |   |    |   +-- Device 0.0.0 (Host.Hub.Device)
    |   |    |   +-- Device 0.0.1
    |   |    |   +-- ..
    |   |    |   +-- Device 0.0.N
    |   |    |
    |   |    +-- Hub 1 [Governed by a Hub Device Table]
    |   |    ·
    |   |    ·
    |   |    +-- Hub M [Governed by a Hub Device Table]
    |   |
    |   | Host Interconnect 1
    |   |
    |   + Host 1 [Governed by a Context & Host Device Table]
    ·
    ·
    |
    | Host Interconnect P 
    |
    +--- Host P [Governed by a Context & Host Table]

