.. _bonsai_onicontext:

ONIContext
===============================
A Bonsai *Source* that manages the acquisition context and allows basic
acquisition parameterization. There must be at least one of these in every
workflow that uses ONIX hardware.

.. raw:: html

    {% with static_path = '../../_static', name = 'ONIContext' %}
        {% include 'workflow.html' %}
    {% endwith %}

Inputs
--------------------------
None

Outputs
--------------------------
A single ``ONIContextTask`` followed by `Never
<http://reactivex.io/documentation/operators/empty-never-throw.html>`__.

Configuration
--------------------------
``ONIContext`` configuration is performed using a GUI provided in the
Bonsai.ONIX.Design library. It can be opened by double clicking on the
``ONIContext`` node if Bonsai.ONIX.Design has been installed.

.. image:: /_static/workflows/ONIContext_configuration.png
   :align: center

This GUI gives access to basic ONI Context configuration such as

- Driver
- Hardware Slot
- Read Block Size
- Write Block Size
- ONIX-specific hub options such as access to raw deserializer data streams:

    .. image:: /_static/workflows/ONIContext_hub-configuration.png
       :align: center

as well as the complete device table. Devices within the table are available
for immediate configuration. Note that changes to device registers using the
``ONIContext`` GUI will not be saved in the workflow file. To save device
register values to file, device configuration must be performed using dedicated
device nodes.
