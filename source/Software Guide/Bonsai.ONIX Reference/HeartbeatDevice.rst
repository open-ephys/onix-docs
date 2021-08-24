.. _bonsai_heartbeatdev:

HeartbeatDevice
===============================
A `Bonsai source <https://bonsai-rx.org/docs/editor/#toolbox>`__ that wraps a
:ref:`onidatasheet_heartbeat` device.

:Inputs:  None
:Outputs: A single ``HearbeatDataFrame`` that is produced periodically by
          hardware. This type is a wrapper around the :ref:`Device To Host Data
          Frame <onidatasheet_heartbeat_d2h>` specified on the
          :ref:`onidatasheet_heartbeat` device datasheet.

.. raw:: html

    {% with static_path = '../../_static', name = 'Heartbeat' %}
        {% include 'workflow.html' %}
    {% endwith %}

Configuration
--------------------------
Configuration is performed using its property pane which contains the following
options.

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
      - Rate at which beats are produced in Hz.
