.. _what_is_onix:

.. toctree::
    :hidden:

What is ONIX?
==========================================
ONIX is a data acquisition system for neuroscience, composed of various pieces
of hardware. ONIX differs from other acquisition systems in three ways:

1. Standards & Interoperability
--------------------------------
All acquisition systems follow specific sets of rules that outline how data is
structured and transmitted between parts of the system. For instance, Intan
headstages and the `classic Open Ephys Board
<https://open-ephys.org/acq-board>`__ use a `Serial Peripheral Interface (SPI)
for communication
<https://en.wikipedia.org/wiki/Serial_Peripheral_Interface>`__. Many different
and non-interchangeable interfaces and protocols are in use, which is why each
type of probe or camera usually comes with its own specific acquisition board.

The `Open Neuro Interface (ONI) <https://open-ephys.github.io/ONI>`__ is an
open standard that was designed as a unified protocol to communicate with a
wide variety of instruments. By specifying how data should be organised but
remaining agnostic to the type of data, a single acquisition system can be used
to acquire from, for instance, extracellular probes, cameras, and tracking
systems.

This means that the same software and hardware can now be used for a wide range
of different recording instruments, so that labs do not have to spend time and
money purchasing separate acquisition systems for each extra tool they wish to
add to their experiment. Additionally, for those who want to develop new tools
to study the brain, ONIX provides a powerful hardware backend and software
infrastructure that can be reused to control almost any type of recoding
instrument.

2. Thin Tethers & Zero Torque Commutation
-------------------------------------------
There is a growing appreciation of experiments that examine the natural
behaviours of animals. This often means using larger and more intricate
(perhaps 3D) experimental setups. It also means that the animal should be
impaired as little as possible by the recording setup. To achieve this it is of
course important to reducing the weight of the headstage, but the weight of the
tether that connects the headstage to the acquisition system is often
overlooked. As the animal explores the arena, the center of mass of the tether
is rarely directly above the animal. Instead, it is off to one side,
introducing a rotational force (torque) on the animal. The animal must
compensate for this torque in order to keep its head up straight.  Because the
ONI specification allows communication over a single wire, ONIX uses a single
coaxial cable, making ONIX tethers lighter and thinner compared to classic
acquisition systems. ONIX tethers are 0.1 to 0.4 mm in diameter and are
extremely flexible.

The tether must also be able to rotate as the animal does to prevent it from
becoming twisted. Commutators are hardware devices that allow the tether to
rotate while maintaining an electrical connection to the rest of the path to
the acquisition system. As the animal moves through the arena, the ONIX
commutator receives 3D tracking information from the headstage and drives  a
motor to actively rotate the tether, preventing twisting. Importantly, this
process is driven by real-time measurement of headstage rotation, *not by
torque transmitted by the tether*. This allows nearly zero-torque commutation
and the use of tethers that are so thin, they would not not function in systems
that require torque measurements to drive active commutation.

3. Low Latencies
--------------------------------
In closed-loop experiments, data is not only acquired, but also processed and
acted upon. For instance, one can provide optogenetic stimulation to a brain
area every time a certain type of event is detected by an extracellular probe.
The closed-loop latency of the acquisition system describes how much time
passes between the physical event and the response of the real-time system. A
short latency allows the user to respond on the timescale of the biological
event; for instance, within the integration window of a neuron.

Many acquisition systems rely on a USB connection between the acquisition board
and PC. Or, they rely on closed-source 3rd-party drivers and APIs that are not
optimized for low response latencies. The slower transfer characteristics of
USB means that a typical closed-loop latency is in the range of several
to tens of milliseconds. This is a considerable duration for the brain, as it
is notably longer than the average action potential duration of around 1 ms. On
average, ONIX provides much shorter latencies, of around 150 microseconds, because:

- ONIX is transfers data to the host computer without the CPU via DMA over PCIe.
- ONIX uses a custom device driver optimized for low latency.
- The ONI API allows explicit control over a single parameter to governs the
  trade off between data latency and overall bandwidth.

This permits the user to optimize their system's response time for a given
experiment.  In all, this means that the system can respond quickly to detected
events. It also means that time is freed up for this detection itself; by
reducing the overhead time, more complex analysis can be run to extract the
phenomenon you are interested in.
