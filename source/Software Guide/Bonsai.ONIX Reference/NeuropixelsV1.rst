.. _bonsai_neuropixelsv1dev:

NeuropixelsV1Device
===============================
A `Bonsai source <https://bonsai-rx.org/docs/editor/#toolbox>`__  that wraps a
:ref:`onidatasheet_neuropixels_v1` device.

:Inputs:    None
:Outputs:   A single ``NeuropixelsV1DataFrame`` that contains one or more
            Neuropixels 1.0 "Ultraframes". One Ultraframe contains the
            following elements:

            - A single LFP-band sample from all 384 electrodes
            - 12 spike-band samples from all 384 electrodes
            - A 20-bit counter that increments for each "Frame" transmitted
              by the probe. 156 frames are required to make a single
              Ultraframe. This counter can be checked to ensure no data is
              dropped.

            The number of Ultraframes in each output is determined by the
            ``BlockSize`` parameter

.. raw:: html

    {% with static_path = '../../_static', name = 'NeuropixelsV1' %}
        {% include 'workflow.html' %}
    {% endwith %}

Configuration
--------------------------
Configuration is performed using a combination of the property pane and a
dedicated configuratoin GUI.

Property Pane
_________________________
Parameters available through the property pane are as follows:

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
      - The number of Ultraframes that are included in each
        NeuropixelsV1DataFrame. Larger numbers result in less overhead at the
        cost of larger buffering latencies.

    * - RequireSNMatch
      - boolean
      - If true, then require configuration and probe serial numbers to match
        to start acqusition. Keeping this parameter set to True is good
        practice because the correct calibration files must be loaded in order
        for the probe to function properly.

    * - NueuropixelsV1Configuration
      - N/A
      - Editing this parameter will open the configuration GUI, just like
        double clicking on the node.

GUI
_________________________
The GUI is opened by double clicking on the NeuropixelsV1Device node when
editing the workflow or clicking the ellipsis next to the
``NueuropixelsV1Configuration`` parameter option in the property pane.

    .. figure:: /_static/bonsai/neuropixelsv1/neuropixelsv1_configuration-gui-callouts.png
       :align: left

    The Neuropixels 1.0 configuration GUI.

.. todo:: Fill these in

Uploading IMEC Calibration Data
***********************************

Selecting Electrodes
*************************

Changing Probe Parameters
*************************

Uploading
*************************

Saving Configurations
*************************


