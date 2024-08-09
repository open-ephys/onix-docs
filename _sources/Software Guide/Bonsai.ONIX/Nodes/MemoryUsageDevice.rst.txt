.. include:: ../deprecation-notice.rst



#################
MemoryUsageDevice
#################


A `Bonsai source <https://bonsai-rx.org/docs/editor/#toolbox>`__ that wraps a
:ref:`onidatasheet_memory-usage` device.

:Inputs:  None
:Outputs: A single ``MemoryUsageDataFrame`` that is produced periodically by
          hardware containing information about data buffer memory status.
          This type is a wrapper around the :ref:`Device To Host Data Frame <onidatasheet_memory-usage_d2h>` specified 
          on the :ref:`onidatasheet_memory-usage` datasheet. To calculate the percentage of memory that is occupied, 
          divide the number of 32-bit memory words used by the hardware's total memory and multiply that quotient by 100. 

..  attention:: 
    The :ref:`Block Read Size <bonsai_onicontext_configuration>` property in the :ref:`bonsai_onicontext` node is set intentionally low so that the buffer accumulates data for demonstration purposes.

.. raw:: html

    {% with static_path = '../../../_static', name = 'MemoryMonitor' %}
        {% include 'workflow.html' %}
    {% endwith %}

*************
Configuration
*************

Configuration is performed using its property pane which contains the following
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

    * - UpdateHz
      - uint
      - Rate at which the hardware memory usage is polled in Hz.

    * - MemorySize
      - uint
      - Hardware buffer size in 32-bit words.
