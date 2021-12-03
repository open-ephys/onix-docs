.. _bonsai_clockoutputdev:

ClockOutputDevice
===============================
A `Bonsai sink <https://bonsai-rx.org/docs/editor/#toolbox>`__ that wraps a
:ref:`onidatasheet_fmc_clock_out` device.

:Inputs:    A ``boolean`` that is connected to the ``Enable`` setting and can be
            use to gate the clock output, but is not required.

:Outputs:   None

.. raw:: html

    {% with static_path = '../../_static', name = 'ClockOutput' %}
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

    * - ClockEnabled
      - boolean
      - If true the clock output is enable and disabled if false. This can be
        controlled from within the workflow using the boolean input. 

    * - Frequency
      - double
      - Output clock frequency in Hz 

    * - DutyCycle
      - double
      - Output clock duty cycle (percent) 

    * - Delay
      - double
      - If SyncToRun is true, this determins the delay from the start of the
        hardware running state to the start of the clock output in seconds. 

    * - SyncToRun
      - bool
      - If true, then the clock output will remain low until hardware
        aquisition starts. Otherwise it will free run independent of acqusition
        state. 
