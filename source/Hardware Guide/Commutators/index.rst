.. _commutators:

Coaxial Commutators
===================================
Active, near-zero torque commutators prevent tether twisting during freely
moving recordings with headstages and/or miniscopes. This page provides a very
brief overview of the commutators; for a more extensive walkthrough, please
follow the `commutator docs
<https://open-ephys.github.io/commutator-docs/index.html>`__.

:Design Repository: https://github.com/open-ephys/commutators
:Compatibility: All coaxial headstags (e.g. :ref:`headstage_64`,
                :ref:`headstage_neuropix2e`, :ref:`miniscopes`)
:Documentation: https://open-ephys.github.io/commutator-docs/index.html

.. _commutators_overview:

Overview
#########################
.. figure:: ../../_static/images/commutator/commutator_front.jpg
  :width: 80%
  :align: center

  ONIX Single Channel Commutator

ONIX uses an active commutator to prevents tether twisting during freely moving
recordings. An inertial measurement unit (IMU) on the headstage or miniscope
sends orientation data to the host computer. Because the real-time orientation
of the animal is known, software can be used to send commands to the commutator
via its USB interface, and the motor in the commutator will turn when the
animal does. A high-quality radio-frequency rotary joint inside the commutator
maintains electrical connectivity for both power and high-frequency data
signals between the tether leading to the headstage and the coaxial cable
leading to the PCIe host board while turning.

In addition to untwisting the tether, the commutator can also play a role in
keeping the tether out of the animal's way and in counterweighing
the headstage. This is done by hooking a thin elastic string to the hook on
the bottom of the commutator gear. For more information on how to do this, visit
the `Tether Management and Headstage Counterweight
<https://open-ephys.github.io/commutator-docs/user-guide/tether-management_counterweight.html>`_
page.

Features
-------------------------
- High bandwidth link up to 18 GHz
- Optical table & 80/20 rail mountable
- Remote control using JSON-encoded commands
- Manual control using capacitive sense buttons
- Indication LED (can be turned off)
- Advanced stepper driver (TMC2130)

  - Voltage-controlled for silent operation
  - Precise motion using step interpolation (256 uSteps/step)

- USB powered and controlled

  - Internal super-capacitor circuitry prevents loading the USB bus during
    motion
