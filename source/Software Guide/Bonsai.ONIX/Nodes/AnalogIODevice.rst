.. _bonsai_analogiodev:

AnalogIODevice
===============================
A `Bonsai source <https://bonsai-rx.org/docs/editor/#toolbox>`__ that wraps a
:ref:`onidatasheet_fmc_analog_io` device.

:Inputs:  A 12xN **OpenCV.Net.Mat**

          - Each column contains 12 analog values, one for each channel.
          - If a channel is set to an input, this will have no effect.
          - Data is immediately consumed by hardware. If N > 1, then samples
            will be produced as quickly as hardware allows.
          - The matrix must contain elements with **Depth.S16**
            when the ``DataType`` parameter is set to is "S16" and either **Depth.F32**
            or **Depth.F64** when ``DataType`` is set to "Volts".
          - When the ``DataType`` parameter is set to is "S16", analog output voltages
            are encoded in offset binary, with 0 resulting in -10V and 65355
            resulting in +10V.

:Outputs: An ``AnalogInputDataFrame`` that contains analog samples and sample
          timing information.

          - This type is a buffered set of :ref:`Device To Host Data Frames
            <onidatasheet_heartbeat_d2h>`.
          - The number of samples in each output is determined by the
            ``BlockSize`` parameter
          - Analog voltages are packaged into 12xBlockSize (**OpenCV.Net.Mat**)

.. raw:: html

    {% with static_path = '../../../_static', name = 'AnalogIO' %}
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

    * - BlockSize
      - uint
      - The number of samples that are included in each AnalogInputFrame.
        Larger numbers result in less overhead at the cost of larger buffering
        latencies.

    * - DataType
      - enum
      - The format of the analog data consumed and produced by this node.

        - S16: raw 16-bit signed integer conversion results or DAC values.
        - Volts: 32-bit floating-point voltages.

    * - InputRange<Channel>
      - enum
      - The analog input over which the 14-bit ADC conversion is applied.
        Smaller values have higher resolution.

    * - Direction<Channel>
      - enum
      - The direction of the channel. If set to Output, the measured voltage is
        automatically looped back through the analog input.

Loading Scripts
--------------------------
The following scripts can be used to load the data produced by this workflow in Python (using Numpy):

- :download:`load-analog-data.py <../../../_static/bonsai/workflows/load-analog-data.py>` 
