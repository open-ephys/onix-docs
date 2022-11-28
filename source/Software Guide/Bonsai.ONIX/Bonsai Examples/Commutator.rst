.. _bonsai_commutator:

Manual Commutator Workflow
===============================
This example workflow shows how manually control :ref:`commutators` by sending
JSON commands in bonsai.

.. raw:: html

    {% with static_path = '../../_static', name = 'CommutatorManual' %}
        {% include 'workflow.html' %}
    {% endwith %}

Usage 
--------------------------
Make sure the port that the commutator is connected to is selected int the
``SerialStringWrite`` node. Press the up and down buttons while the workflow is
running to turn the commutator CW and CCW, respectively.

.. note:: Typically the commutator is used in conjuction with a headstage or
   miniscope to prevent twisting during free moving recordings. Look at
   the :ref:`bonsai_headstage64` for an example.
