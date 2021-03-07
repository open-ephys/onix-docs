.. |download_image| image:: /_static/download.svg
  :height: 18
.. |copy_image| image:: /_static/copy.svg
  :height: 18

.. _bonsai_onixref:

Bonsai.ONIX Reference
===================================
.. toctree::
    :maxdepth: 2
    :hidden:
    
    ONIContext
    HeartbeatDevice
..     FMCAnalogDevice
..     FMCDigitalDevice
..     FMCClockOutput
..     FMCClockInput
..     Neuropixels1R0
..     RHD2162
..     BNO055
..     LightHouseV2Array
..     OptoStimulator
..     ElectricalStimulator
..     MiniscopeV3

``Bonsai.ONIX`` is a `Bonsai <https://bonsai-rx.org/>`__ library for ONIX
hardware. This library contains `Bonsai Operators
<https://bonsai-rx.org/docs/operators/>`__ for acquiring and sending data to
ONIX hardware. An additional library, ``Bonsai.ONIX.Design``, contains GUI
elements for the core library. Although it is possible to use ``Bonsai.ONIX``
without the GUI library, it is not recommended. There are three major classes
of operators in the library:

#. :ref:`bonsai_onicontext` - This operator wraps an
   :ref:`oni_h_acquisition_context` and provides access to the device table for
   a hardware slot. At least one of these operators is required in every
   workflow.
#. ``<Some>Device`` - These operators wrap individual :ref:`ONI Device
   <onidatasheets>`'s and provide access to their data IO and configuration
   registers.
#. Various helper operators that provide data conditioning functionality. E.g.
   for converting raw sensor data into 3D positions, etc.

Using this Documentation
--------------------------
This documentation contains functional workflows and operators. You can
download workflows by clicking the |download_image| icon.  Alternatively, you
can copy and paste them into the `Bonsai Workflow Editor
<https://bonsai-rx.org/docs/editor/>`__ by clicking the |copy_image| icon and
using ``Ctrl+v`` or equivalent in the editor:

.. raw:: html

    {% with static_path = '../../_static', name = 'HelloWorld' %}
        {% include 'workflow.html' %}
    {% endwith %}
