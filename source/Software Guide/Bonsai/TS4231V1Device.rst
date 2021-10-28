.. _bonsai_ts4231v1dev:

TS4231V1Device
===============================
A `Bonsai source <https://bonsai-rx.org/docs/editor/#toolbox>`__  that wraps a
:ref:`onidatasheet_ts4231_v1_array`. Typically, this node is followed by
at least one **TS4231V1FrameToPosition** transform node, which converts the raw
output from a single photodiode in the sensor array to a 3D position.

:Inputs:    None
:Outputs:   A single ``TS4231V1DataFrame`` that is produced
            periodically by hardware. This type is a wrapper around
            the :ref:`Device To Host Data Frame
            <onidatasheet_ts4231_v1_array_d2h>` specified on the
            :ref:`onidatasheet_ts4231_v1_array` device datasheet.

.. raw:: html

    {% with static_path = '../../_static', name = 'TS4231' %}
        {% include 'workflow.html' %}
    {% endwith %}

Configuration
--------------------------
Configuration is performed using the property pane which contains the following
configuration options:

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Name
      - Type
      - Description

    * - EnableStream
      - boolean
      - Enable the device data stream
