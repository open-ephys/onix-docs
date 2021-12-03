.. _bonsai_miniscopev4bno055dev:

MiniscopeV4BNO055Device
===============================
.. important:: To use Miniscopes with ONIX hardware, you must first use the :ref:`bonsai_onicontext` configuration GUI to set the headstage port to :ref:`Passthrough Mode" <bonsai_onicontext_hubsettings>`

A `Bonsai source <https://bonsai-rx.org/docs/editor/#toolbox>`__  that wraps a
:ref:`onidatasheet_ds90ub9x_raw` device and configures it to allow control over
`UCLA Miniscope V4
<http://miniscope.org/index.php/Overview_of_System_Components>`__'s onboard BNO055 inertial measurement unit.

:Inputs:    None
:Outputs:   A single ``MiniscopeV4BNO055DataFrame`` that is polled by software
            and contains the data-fields of the :ref:`Device To Host Data Frame
            <onidatasheet_bno055_d2h>` specified on the
            :ref:`onidatasheet_bno055` device datasheet, with the exception of
            clock and frame counter information, since data is acquired via
            software polling. 

.. raw:: html

    {% with static_path = '../../_static', name = 'UCLAMiniscopeV4' %}
        {% include 'workflow.html' %}
    {% endwith %}

Configuration
--------------------------
This device has no configuration.
