.. _bonsai_ostimdev:

OpticalStimulationDevice
===============================
A `Bonsai sink <https://bonsai-rx.org/docs/editor/#toolbox>`__  that wraps a
dual-channel :ref:`onidatasheet_ostim_hs64` device.

:Inputs:    A ``boolean`` that triggers stimulus delivery

            - True: deliver stimulus
            - False: Do nothing

:Outputs:   None

.. raw:: html

    {% with static_path = '../../_static', name = 'OpticalStimulator' %}
        {% include 'workflow.html' %}
    {% endwith %}

Configuration
--------------------------
Configuration is performed using either the property pane or a configuration
GUI which provides a graphical representation of the stimulus waveform.

.. figure:: /_static/bonsai/ostim/OpticalStimulationDevice_parameters.png
    :alt: OpticalStimulationDevice parameter definitions
    :align: center
    :scale: 35%

    Example stimulus waveform with parameter definitions.

Property Pane
_________________________
Parameters available through the property pane are as follows:

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Name
      - Type
      - Description

    * - Enable
      - boolean
      - Enable or disable the stimulator. If the stimulator is disabled, it
        will not respond to trigger inputs. This setting is useful if you wish
        to interleave electrical and optical stimuli, since they share a
        trigger line on some headstages.

    * - MaxCurrent
      - double
      - Maximum current per channel per pulse (mA). This value is used by both
        channels. To get different amplitudes for each channel use the
        Channel0Level and Channel1Level parameters.

    * - ChannelZeroCurrent
      - double
      - Channel 0 percent of max current. If greater than 0, channel 0 will
        respond to triggers.

    * - ChannelOneCurrent
      - double
      - Channel 1 percent of max current. If greater than 0, channel 1 will
        respond to triggers.

    * - PulseDuration
      - double
      - Pulse duration (msec).

    * - PulsePeriod
      - double
      - Pulse period (msec).

    * - BurstPulseCount
      - unit
      - Number of pulses to deliver in a burst.

    * - InterBurstInterval
      - double
      - Interburst interval (msec).

    * - TrainBurstCount
      - uint
      - Number of bursts to deliver in a train.

    * - TrainDelay
      - double
      - Delay between issue of trigger and start of train (msec).

Configuration GUI
_________________________
The configuration GUI is identical to the property pane, but provides a plot of
the stimulus waveform.

.. figure:: /_static/bonsai/ostim/ostim-gui.png
    :align: left
    :alt: The OpticalStimulationDevice configuration GUI

    The OpticalStimulationDevice configuration GUI

GUI Controls
**********************************

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Mouse action
      - Function

    * - Left click + drag
      - Zoom selection

        .. image:: /_static/bonsai/ostim/ostim-gui-do-zoom.png
            :align: left
            :alt: Left click and drag to zoom in on the waveform. Middle click and drag to pan.
            :scale: 50%

    * - Middle click + drag
      - Pan

    * - Right click
      - Open waveform plot context menu

        .. image:: /_static/bonsai/ostim/ostim-gui-right-click-plot.png
            :align: left
            :alt: Right click to open the waveform plot context menu
            :scale: 50%

    * - Scroll forward
      - Zoom in

    * - Scroll backward
      - Zoom out
