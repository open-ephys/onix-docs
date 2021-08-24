.. _bonsai_rhd2164dev:

RHD2164Device
===============================
A `Bonsai source <https://bonsai-rx.org/docs/editor/#toolbox>`__  that wraps a
:ref:`onidatasheet_rhd2164` device.

:Inputs:    None
:Outputs:   A ``RHD2164DataFrame`` that contains one or more samples from all
            64 analog inputs and auxiliary channels. 

            - This type is a buffered set of the :ref:`Device To Host Data Frame
              <onidatasheet_rhd2164_d2h>` specified on the
              :ref:`onidatasheet_rhd2164` device datasheet.
            - The number of samples in each output is determined by the
              ``BlockSize`` parameter

.. raw:: html

    {% with static_path = '../../_static', name = 'RHD2164' %}
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
      - The numbEnable the device data stream

    * - BlockSize
      - integer
      - The number of 64-channel ephys + auxiliary channel samples that are
        included in each RHD2164DataFrame. Larger numbers result in less
        overhead at the cost of larger buffering latencies.

    * - AnalogHighCutoff
      - enum
      - Select a high-frequency cutoff from allowable options. This filtering
        is performed prior to analog to digital conversion.

    * - AnalogLowCutoff
      - enum
      - Select a low-frequency cutoff from allowable options. This filtering is
        performed prior to analog to digital conversion.

    * - DSPCuttoff
      - enum
      - Select the low-frequency cutoff for the integrated digtial offset
        removal filter. This fitering is performed following analog to digital
        conversion.

    * - EphysDataFormat
      - enum
      - The format of the ephys samples within the  RHD2164DataFrame.

        - Unsigned: raw 16-bit unsigned integer conversion results.
        - TwosCompliment: raw 16-bit signed integer conversion results.
        - MicroVolts: 32-bit floating-point voltages.

    * - AuxDataFormat
      - enum
      - The format of the auxiliary samples within the  RHD2164DataFrame.

        - Unsigned: raw 16-bit unsigned integer conversion results.
        - Volts: 32-bit floating-point voltages.
