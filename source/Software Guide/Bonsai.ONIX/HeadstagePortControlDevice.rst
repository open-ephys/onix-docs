.. _bonsai_headstageportcontroldev:

HeadstagePortControlDevice
===============================
A `Bonsai source <https://bonsai-rx.org/docs/editor/#toolbox>`__ that wraps a
:ref:`onidatasheet_fmc_link_control` device.

:Inputs:    None 
:Outputs:   A single ``HeadstagePortControlFrame`` that is produced whenever
            triggered by hardware events pertaining to the link connectivity
            status.  This type is a wrapper around the :ref:`Device To Host
            Data Frame <onidatasheet_fmc_link_control_d2h>` specified on the
            :ref:`onidatasheet_fmc_link_control` device datasheet.

.. raw:: html

    {% with static_path = '../../_static', name = 'HeadstagePortControl' %}
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

    * - EnableExtendedVoltageRange
      - string
      - By default, the maximum link voltage is limited to 8V. If you have a
        very long, thin tether, this may need to be increased. By typing "BE
        CAREFUL" into this field, the link voltage can be adjusted up to 10V.

    * - LinkVoltage
      - double
      - The DC voltage applied on the coaxial headstage port that provides
        power to the headstage. This needs to be applied to compensate for the
        tether's series resistance.

    * - GPO1
      - boolean
      - The SERDES GPO1 digital state. This GPO is tied to some stimulation
        features on some headstages and can be used for very rapid closed loop
        stimulation. Check the headstage documentation for more information.
