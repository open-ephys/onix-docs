.. _bonsai_heartbeatdev:

HeartbeatDevice
===============================
A Bonsai *Source* that wraps a :ref:`onidatasheet_heartbeat` device.

.. raw:: html

    {% with static_path = '../../_static', name = 'Heartbeat' %}
        {% include 'workflow.html' %}
    {% endwith %}

Inputs
--------------------------
None

Outputs
--------------------------
A single ``HearbeatDataFrame`` that is produced periodically by hardware. This
type is a wrapper around the *Device To Host Data Frame* specified on the
:ref:`onidatasheet_heartbeat` device datasheet.

Configuration
--------------------------
Configuration of ``HeartbeatDevice`` is performed using its property pane which
contains the followin options.

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Name
      - Type
      - Description

    * - EnableStream
      - boolean
      - Enable the device data stream

    * - BeatHz
      - uint
      - Rate at which beats are produced
