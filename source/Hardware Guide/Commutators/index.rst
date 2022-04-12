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

The active commutator prevents twisting of the tether leading to the animal, by rotating whenever the animal turns.
A BNO on the headstage sends orientation data to the PCIe host board. By streaming this data to Bonsai and sending it to the commutator via USB, the motor in the commutator can turn when the animal does. A rotary joint inside the commutator maintains electrical contact between the tether leading to the headstage and the SMA cable leading to the PCIe host board while turning.
