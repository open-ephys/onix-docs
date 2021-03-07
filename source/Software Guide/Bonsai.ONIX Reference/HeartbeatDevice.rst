.. _bonsai_heartbeatdev:

HeartbeatDevice
===============================
A Bonsai Source that wraps a :ref:`onidatasheet_heartbeat` device.

.. raw:: html

    {% with static_path = '../../_static', name = 'Heartbeat' %}
        {% include 'workflow.html' %}
    {% endwith %}

Inputs
--------------------------
None

Outputs
--------------------------
A single ``HearbeatFrame`` every time one is produced by hardware. This type is
a direct wrapper around the Device To Host Data Frame specified on the
:ref:`onidatasheet_heartbeat` device datasheet.

Configuration
--------------------------
Configuration of ``Heartbeat`` is performed using its property pane. Parameter
explanations are provided there.
