.. _bonsai_estimdev:

ElectricalStimulationDevice
===============================
A `Bonsai sink <https://bonsai-rx.org/docs/editor/#toolbox>`__  that wraps a
:ref:`onidatasheet_estim_hs64` device.

:Inputs:    A ``boolean`` that triggers stimulus delivery

            - True: deliver stimulus
            - False: Do nothing

:Outputs:   None

.. raw:: html

    {% with static_path = '../../_static', name = 'ElectricalStimulator' %}
        {% include 'workflow.html' %}
    {% endwith %}

Configuration
--------------------------
Configuration is performed using either the property pane or a configuration
GUI which provides a graphical representation of the stimulus waveform.

.. figure:: /_static/bonsai/estim/ElectricalStimulationDevice_parameters.png
    :alt: ElectricalStimulationDevice parameter definitions
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

    * - PowerOn
      - boolean
      - If true, the stimulator power circutiry is turned on. When not in
        use, its a good idea to keep this false to reduce headstage power
        consumption and possible increased noise.

    * - PhaseOneCurrent
      - double
      - Phase 1 pulse current (uA).

    * - PhaseTwoCurrent
      - public double
      - Phase 2 pulse current (uA).

    * - InterPhaseCurrent
      - double
      - Resting current between pulse phases(uA).

    * - PhaseOneDuration
      - double
      - Phase 1 pulse duration (msec). This value can be 0 for monophasic stimuluation.

    * - InterPhaseDuration
      - double
      - Inter-pulse phase duration (msec).This value can be 0 if no inter-phase
        current is required.

    * - PhaseTwoDuration
      - double
      - Phase 2 pulse duration (msec). This value can be 0 for monophasic stimuluation.

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

.. figure:: /_static/bonsai/estim/estim-gui.png
    :align: left
    :alt: The ElectricalStimulationDevice configuration GUI

    The ElectricalStimulationDevice configuration GUI

GUI Controls
**********************************

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Mouse action
      - Function

    * - Left click + drag
      - Zoom selection

        .. image:: /_static/bonsai/estim/estim-gui-do-zoom.png
            :align: left
            :alt: Left click and drag to zoom in on the waveform. Middle click and drag to pan.
            :scale: 50%

    * - Middle click + drag
      - Pan

    * - Right click
      - Open waveform plot context menu

        .. image:: /_static/bonsai/estim/estim-gui-right-click-plot.png
            :align: left
            :alt: Right click to open the waveform plot context menu
            :scale: 50%

    * - Scroll forward
      - Zoom in

    * - Scroll backward
      - Zoom out
