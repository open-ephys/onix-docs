.. _what_is_onix:

What is ONIX?
==========================================

ONIX is an acquisition system for neuroscience, composed of various pieces of
hardware that are ONI-compliant, i.e. they follow the Open Neuro Interface
Specification for communication.

ONIX differs from classic acquisition systems in three major points:

1. Standards
--------------------------------
All acquisition systems follow specific sets of rules that outline how data is
structured and communicated between parts of the system. For instance, Intan
headstages and the classic Open Ephys Board use the Serial Peripheral Interface
(SPI) for communication. Many different and non-interchangeable interfaces and
protocols are in use, which is why each type of probe or camera usually comes
with its own specific acquisition board.

ONI is an open standard that was designed as a unified protocol to communicate
with a wide variety of instruments. By specifying how data should be organised
but remaining agnostic to the type of data, this one interface can be used to
acquire from, for instance, extracellular probes, cameras, and tracking
systems.

This means that the same acquisition software and hardware can now be used for
a wide range of different devices, so that labs do not have to spend time and
money acquiring separate acquisition systems for each extra tool they wish to
add to their experiment. For those who want to develop new devices for
neuroscience, using this standard means that rather than spending their time
trying to get different interfaces to communicate with each other, they can
focus on the specifics of the device they wish to build.

2. Tethers
--------------------------------
There is a growing appreciation of experiments that examine the natural
behaviours of animals. This often means using larger and more intricate
(perhaps 3D) experimental setups. It also means that the animal should be
impaired as little as possible by the recording setup. To achieve this it is of
course important to reducing the weight of the headstage, but the weight of the
tether that connects the headstage to the acquisition system is often
overlooked. As the animal explores the arena, the centre of mass of the tether
is rarely directly above the animal. Instead, it is off to one side,
introducing a rotational force on the animal. The animal must compensate for
this torque in order to keep its head up straight.  Because the ONI
specification allows communication over a single wire, ONIX uses a single
coaxial cable, making ONIX tethers lighter and thinner compared to classic
acquisition systems. ONIX tethers are 0.1 to 0.4 mm in diameter and are
extremely flexible.

The tether must also be able to rotate as the animal does to prevent it from
becoming twisted. Commutators are hardware devices that allow the tether to
rotate while maintaining an electrical connection to the rest of the path to
the acquisition system. As the animal moves through the arena, the ONIX
commutator receives 3D tracking information from the headstage and drives  a
motor to actively rotate the tether, preventing twisting.

3) Latencies
--------------------------------
In closed-loop experiments, data is not only acquired, but also processed and
acted upon. For instance, one can provide optogenetic stimulation to a brain
area every time a certain type of event is detected by an extracellular probe.
The closed-loop latency of the acquisition system describes how much time
passes between the initial event and the response of the system. In classic
acquisition systems, this time is primarily spent on transmitting and
processing acquired data, which becomes more and more challenging as the number
of channels on a probe increases. A short latency allows the user to respond on
the timescale of the biological event; for instance, within the integration
window of a neuron.

Many classic acquisition systems rely on a USB connection between the
acquisition board and PC. The slower transfer characteristics of USB means that
a typical closed-loop latency would be in the range of several to tens of
milliseconds. This is a considerable duration for the brain, as it is notably
longer than the average action potential duration of around 1 ms. ONIX has much
shorter latencies, of around 150 microseconds, because the host board of ONIX
is directly connected to the acquisition PC, in a PCIe slot. This means that
the system can respond quickly to detected events. It also means that time is
freed up for this detection itself; by reducing the overhead time, more complex
analysis can be run to extract the phenomenon you are interested in.
