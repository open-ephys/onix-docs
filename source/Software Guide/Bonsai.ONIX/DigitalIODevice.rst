.. _bonsai_digitaliodev:

DigitalIODevice
===============================
A `Bonsai source <https://bonsai-rx.org/docs/editor/#toolbox>`__ that wraps a
:ref:`onidatasheet_fmc_digital_io` device.

:Inputs:  An ``int`` that sets the output port state

          - The 8 least significant bits of the integer input are used to set
            the output port state.

:Outputs: An ``DigitalInputDataFrame`` that contains digital input, button, and
          headstage power switch state

          - A sample is produced only when a change in port, button, or
            headstage power switch state occurs
          - This type is a wrapper around the :ref:`Device To Host Data Frame
            <onidatasheet_fmc_digital_io_d2h>` specified on the
            :ref:`onidatasheet_fmc_digital_io` device datasheet.

.. raw:: html

    {% with static_path = '../../_static', name = 'DigitalIO' %}
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
      - The brightness of the breakout board indication LEDs. 0 = off, 100 =
        full brightness.

