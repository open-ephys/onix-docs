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
        {% include 'workflow-zip.html' %}
    {% endwith %}

Configuration
--------------------------
Configuration is performed using a combination of the property pane and a
dedicated configuration GUI.

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
      - Enable the device data stream

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
      - Editing this parameter will open the Configuration GUI, just like
        double clicking on the node.

Configuration GUI
_________________________
The **Neuropixels 1.0 Configuration GUI**, which is a part of the
``Bonsai.ONIX.Design`` library, is opened by double clicking on the
NeuropixelsV1Device node when editing the workflow or clicking the ellipsis
next to the ``NueuropixelsV1Configuration`` parameter option in the property
pane.

.. figure:: /_static/bonsai/neuropixelsv1/neuropixelsv1_configuration-gui-callouts.png
    :align: left
    :alt: The Neuropixels 1.0 configuration GUI.

    The Neuropixels 1.0 configuration GUI.

Importing IMEC Calibration Data
***********************************
Neuropixels 1.0 probes are shipped with two calibration files that must be
uploaded to the probe for proper operation. For example, the calibration files
for probe 19051023592 are:

- :download:`19051023592_ADCCalibration.csv <../../_static/bonsai/neuropixelsv1/19051023592_ADCCalibration.csv>`
- :download:`19051023592_gainCalValues.csv <../../_static/bonsai/neuropixelsv1/19051023592_gainCalValues.csv>`

The calibration files for your probe will have "19051023592" replaced with your
probe's serial number. These files contain parameters that are used to correct
probe-specific ADC zero-crossing nonlinearities, set on-chip biases, and
linearize individual electrode responses.  For a complete explanation of the
content of these files, please consult the `Neuropixels documentation site
<https://www.neuropixels.org/support>`__.

.. warning:: Failure to upload IMEC-provided calibration and gain correction
    files will result in data that is not standardized and therefore not
    comparable with other Neuropixels 1.0 recordings.

To load the IMEC calibration files for your probe, follow these steps:

#. Select **Load Calibration** from the **File** menu.

    .. image:: /_static/bonsai/neuropixelsv1/neuropixelsv1_load-calibration_cropped.png
       :alt: Load IMEC calibration selected
       :align: left

#. On the file selection dialog, navigate to the folder containing the
   calibration files with serial numbers matching the currently attached probe.

    .. image:: /_static/bonsai/neuropixelsv1/neuropixelsv1_select-calibration_annotated.png
       :alt: Navigate to IMEC calibration files with matching serial numbers
       :align: left
       :scale: 70%

#. The **Channels** and **ADCs** tabs will now show proper calibration
   parameters.

    .. image:: /_static/bonsai/neuropixelsv1/neuropixelsv1_adcs-tab.png
       :alt: The ADC tab with the correct IMEC calibration parameters populated
       :align: left

Configuring the Probe
**********************************
The easiest way to select active electrodes is by using the GUI on the
**Probe** tab. This simple user interface lets you pan around the probe, zoom
in and out, and set the properties of individual electrodes or groups of them.

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Mouse action
      - Function

    * - Left click + drag
      - Block select

    * - Middle click + drag
      - Pan

    * - Right click
      - Open electrode configuration context menu

    * - Scroll forward
      - Zoom in

    * - Scroll backward
      - Zoom out

Active electrodes are colored blue, inactive are white, and selected electrodes
are orange. Groups of electrodes can be selected by left clicking and dragging.
Once highlighted, their properties can be changed using right click to open the
configuration context menu.

    .. image:: /_static/bonsai/neuropixelsv1/neuropixelsv1_adjust-electrode-parameters-with-gui.png
       :alt: Probe GUI with right click to edit electrode parameters
       :align: center
       :scale: 62%

Aside form the Probe tab, the **Channels** tab can be used to examine and tune
the probe parameters. If you want to apply a from one electrode to the entire
probe, right-click it and select **Apply to column**.

.. todo:: Image of apply all dialog

Uploading to the Probe
**********************************
To upload your configuration to the probe, click the **Upload** button in the
bottom left of the GUI. A progress bar will indicate the upload progress.

.. image:: /_static/bonsai/neuropixelsv1/neuropixelsv1_upload-process.png
   :alt: Uploading the configuration to the probe
   :align: center

.. note:: To ensure that this process has occurred correctly, the **Perform Read
    Check** option can be selected from the **Settings** menu:

    .. image:: /_static/bonsai/neuropixelsv1/neuropixelsv1_read-check_cropped.png
       :alt: Selecting the perform read check option
       :align: center
       
    If this option is checked, then the upload will occur two times. The first
    will load the configuration and the second will do a comparison of the
    values stored on the probe to the redundant upload and report an error if
    there is a mismatch. This option is active by default.



Saving Configurations
**********************************
Complete probe configurations can be saved in easy to parse JSON or XML
formats. These fikes contain complete information about the state of a given
probe. This includes all calibration file information, active electrodes, gains
etc, and therefore can be useful metadata during analysis.

#. Select **Export...** from the **File** menu;

    .. image:: /_static/bonsai/neuropixelsv1/neuropixelsv1_export_cropped.png
       :alt: The configuraiton GUI with export selected
       :align: left

#. Choose if JSON or XML should be used in the file selection dialog and save:

    .. image:: /_static/bonsai/neuropixelsv1/neuropixelsv1_export-select-format_cropped.png
       :alt: File dialog to indicate where configuration should be saved.
       :align: left

Loading Configurations
**********************************
Configuration files can be imported to, for instance, recall a pattern of
active electrodes.

.. warning:: You can import the configuration data from a previous probe, for
    instance to re-create a custom electrode layout. However, you will need to
    replace the calibration parameters from the previous probe with the current
    one before using it.

#. Select **Import** from the **File** menu:

    .. image:: /_static/bonsai/neuropixelsv1/neuropixelsv1_import_cropped.png
       :alt: The configuraiton GUI with import selected
       :align: left

#. Select a previously exported configuration file:

    .. image:: /_static/bonsai/neuropixelsv1/neuropixelsv1_import-select-file.png
       :alt: File dialog to find configuration to load
       :align: left
