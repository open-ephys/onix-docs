.. _bonsai_rhs2116triggerdev:

RHS2116TriggerDevice
===============================
A `Bonsai sink <https://bonsai-rx.org/docs/editor/#toolbox>`__  that wraps a
:ref:`onidatasheet_rhs2116trigger` device.

:Inputs:    boolean

           - True: Trigger the stimulus patterns defined on the
             :ref:`bonsai_rhs2116dev` nodes on the same headstage if
             TriggerSource is set to Local. Otherwise, do nothing.
           - False: Do nothing

.. raw:: html

    {% with static_path = '../../../_static', name = 'RHS2116Trigger' %}
        {% include 'workflow.html' %}
    {% endwith %}

Configuration
--------------------------
Configuration is performed using a combination of the property pane.

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Name
      - Type
      - Description

    * - TriggerSource
      - enum
      - The source of the trigger signal that will be distributed across the
        chips on the headstage 

        * Local: Local trigger source is respected (GPIO input to the headstage
          or writing true into the input of this node). In this case, the
          trigger signal will be sent out on the synchronizaiton cable with
          this device acting as a controller.
        * External: Trigger is provided by the synchronization cable from
          another headstage and this device is a receiver that will distribute the
          externally generated trigger to RHS2116 chips on its headstage.
