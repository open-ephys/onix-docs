.. _commutators:

Coaxial Commutators
###################################

.. toctree::
    :maxdepth: 1
    :hidden:

    setup

.. image:: ../../_static/images/commutator/commutator_front.jpg
  :width: 80%
  :align: center

ONIX uses an active commutator to prevents tether twisting during freely moving
recordings.  A inertial measurement unit (IMU) on the headstage or miniscope
sends orientation data to the host computer. Because the real-time orientation
of the animal is known, software (e.g. Bonsai) can be used to send commands to
the commutator via its USB interface, and the motor in the commutator willturn
when the animal does. A high-quality radio-frequency rotary joint inside the
commutator maintains electrical connectivity for both power and high-frequency
data signals between the tether leading to the headstage and the coaxial cable
leading to the PCIe host board while turning.
