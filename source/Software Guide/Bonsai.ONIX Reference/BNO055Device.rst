.. _bonsai_bno055dev:

BNO055Device
===============================
A Bonsai *Source* that wraps a :ref:`onidatasheet_bno055` device.

.. raw:: html

    {% with static_path = '../../_static', name = 'BNO055' %}
        {% include 'workflow.html' %}
    {% endwith %}

Inputs
--------------------------
None

Outputs
--------------------------
A single ``BNO055DataFrame`` that is produced periodically by hardware. This
type is a wrapper around the *Device To Host Data Frame* specified on the
:ref:`onidatasheet_bno055` device datasheet.

Configuration
--------------------------
This device hard-codes all of the configuration required to operate with the following properties:

- 100 Hz update rate
- Full on-chip sensor fusion ("NDOF" mode)
- Hardcoded axis map (orientation depends on the headstage)

A single data stream enable register is provided.

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Name
      - Type
      - Description

    * - EnableStream
      - boolean
      - Enable the device data stream
