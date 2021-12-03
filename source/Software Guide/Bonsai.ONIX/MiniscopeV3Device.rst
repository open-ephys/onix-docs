.. _bonsai_miniscopev3dev:

MiniscopeV3Device
===============================
.. important:: To use Miniscopes with ONIX hardware, you must first use the :ref:`bonsai_onicontext` configuration GUI to set the headstage port to :ref:`Passthrough Mode" <bonsai_onicontext_hubsettings>`

A `Bonsai source <https://bonsai-rx.org/docs/editor/#toolbox>`__  that wraps a
:ref:`onidatasheet_ds90ub9x_raw` device and configures it to allow control over
`UCLA Miniscope V3
<http://miniscope.org/index.php/Overview_of_System_Components>`__.

:Inputs:    None
:Outputs:   A single ``MiniscopeV3DataFrame`` that is produced periodically
            by the scope and contains an image and corresponding sample and
            frame counters.

.. raw:: html

    {% with static_path = '../../_static', name = 'UCLAMiniscopeV3' %}
        {% include 'workflow.html' %}
    {% endwith %}

Configuration
--------------------------
Configuration is performed using the property pane which contains the following
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

    * - LEDBrightness
      - double
      - Excitation LED brightness (0-100%).

    * - Gain
      - double
      - Camera sensor analog gain (0-100%).

    * - FrameRate
      - FPS (enum)
      - Camera images acquired per second.
