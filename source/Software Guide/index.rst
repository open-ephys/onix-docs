.. |software_logo| image:: /_static/noun_macbook.svg
  :height: 60

.. _software_guide:

|software_logo| Software Guide
===================================


.. toctree::
    :hidden:

    Bonsai Package Docs <https://open-ephys.github.io/bonsai-onix1-docs/>
    Open Ephys GUI Plugin ONIX Source <https://open-ephys.github.io/gui-docs/User-Manual/Plugins/Onix-Source.html>
    oni-repl/index
    Deprecated Software<Bonsai.ONIX/index>

There are two recommended software programs to acquire data from the ONIX
system. Click on the cards below to navigate to their respective documentation
sites.  

..  grid::

    ..  grid-item-card:: Bonsai Package OpenEphys.Onix1
        :link-type: url
        :link: https://open-ephys.github.io/bonsai-onix1-docs/
        :class-card: intro-card
        :img-top: /_static/images/bonsai-logo.svg
        :img-alt: bonsai logo
        :class-img-top: software-card-img
        :columns: 5

        Acquire data from ONIX in Bonsai, a visual programming language for more extensive data
        processing and sub-ms latency feedback.

    ..  grid-item-card:: Open Ephys GUI Plugin ONIX Source 
        :link-type: url
        :link: https://open-ephys.github.io/gui-docs/User-Manual/Plugins/Onix-Source.html
        :class-card: intro-card
        :img-top: /_static/images/oe-gui-logo.png
        :img-alt: open ephys gui logo
        :class-img-top: software-card-img
        :columns: 5

        Acquire data from ONIX in the Open Ephys GUI, a turnkey solution for acquiring and
        visualizing electrophysiology data.  

Both platforms are free, open-source, and widely adopted in the neuroscience
community. There are a few important considerations when selecting which to use, which you can read about below.

Software Comparison
___________________________________

|   **User Experience and Types of Data**
|   The Open Ephys GUI is a turnkey application specialized in electrophysiology voltage data acquisition and online processing. Data processing pipelines are made up of a sequence of processors, called a signal chain. Typically, each processor performs one signal processing step so it is straightforward to build signal chains by successively combining different functionalities. 
    Bonsai is a visual programming language which can be used to acquire and process different types of data (analog and digital signals as well as images). It is designed to handle asynchronous datastreams, i.e. that are not sampled continuously, making it possible to flexibly coordinate, combine, and condition datastreams across time. Data acquisition and signal processing pipelines are constructed by connecting operators to make up each function. The Open Ephys GUI is more user-friendly whereas expertise is helpful to build upon the example workflows provided in our documentation and take full advantage of Bonsai. 

|   **Hardware and Software Scope**
|   
    The Open Ephys GUI can acquire headstage and analog and digital data from different neural data acquisition systems (see the `User Manual introduction page <https://open-ephys.github.io/gui-docs/User-Manual/index.html>`_), and actuation is limited to a few external device options (Arduino, PulsePal). Bonsai offers broader compatibility with more hardware options such as
    behavioral cameras, miniscopes, photometry systems, Arduino boards, Harp
    devices, stimulators and numerous other instruments. Bonsai programming elements can be used to structure experimental task logic and stimuli presentation. Additionally, Bonsai integrates third-party algorithms such as SLEAP and DeepLabCut for pose estimation and other machine learning packages for online data processing, and native packages for stimuli presentation such as BonVision, mathematical operations and much more.
    
..  grid::
    :margin: 0
    :padding: 0
    
    ..  grid-item::
        :child-align: center
        :margin: 0
        :padding: 0

        ..  figure:: /_static/images/software/example-signal-chain.png
            :alt: Example signal chain in the Open Ephys GUI
            
            Example signal chain in the Open Ephys GUI

    ..  grid-item::
        :child-align: center
        :margin: 0
        :padding: 0

        ..  figure:: /_static/images/software/example-workflow.png
            :alt: Example workflow in Bonsai
            
            Example workflow in Bonsai

|   **ONIX Support**
|   The OpenEphys.Onix1 package in Bonsai has support for all ONIX
    capabilities while the ONIX Source plugin in the Open Ephys GUI can only support a subset of them. For more information on this, visit the `ONIX Source plugin page <https://open-ephys.github.io/gui-docs/User-Manual/Plugins/Onix-Source.html#onix-support>`_.

|   **Performance/Closed-Loop Latency**
|   Bonsai is capable of operating with sub-millisecond closed-loop latencies, with onboard stimulation devices.
    The Open Ephys GUI operates on the order of 20ms and has more variable
    latencies, using external devices for stimulation.

|   **Data Visualization**
|   The Open Ephys GUI provides visualization tools specialized for presenting electrophysiology voltage data such as the
    `LFP viewer <https://open-ephys.github.io/gui-docs/User-Manual/Plugins/LFP-Viewer.html>`_ with different waveform and raster views, and the
    `Probe viewer <https://open-ephys.github.io/gui-docs/User-Manual/Plugins/Probe-Viewer.html>`_ for displaying high-density probe data.
    Bonsai provides type visualizers which are more agnostic to the kind of data
    that is being streamed.
        
..  grid::
    :margin: 0
    :padding: 0

    ..  grid-item::
        :child-align: center
        :margin: 0
        :padding: 0

        ..  figure:: /_static/images/software/lfp-viewer.png
            :alt: LFP Viewer in the Open Ephys GUI

            LFP Viewer in the Open Ephys GUI

    ..  grid-item::
        :child-align: center
        :margin: 0
        :padding: 0
        
        ..  figure:: /_static/images/software/type-visualizer.png
            :alt: Type visualizer in Bonsai

            Type visualizer in Bonsai

Note, however, that the Open Ephys GUI visualization tools can be used to visualize data acquired from Bonsai using sockets, as explained in `this tutorial <https://open-ephys.github.io/bonsai-onix1-docs/articles/tutorials/ephys-socket.html>`_.
Visualization of multichannel ephys voltage data in Bonsai is improving with the integration of `Dear ImGUI <https://github.com/ocornut/imgui>`_ in the Bonsai.Ephys package.

..  grid::
    :margin: 0
    :padding: 0

    ..  grid-item::
        :child-align: center
        :margin: 0
        :padding: 0

        ..  figure:: /_static/images/software/sockets-end-result_GUI.jpg
            :alt: Sockets to visualize Bonsai data in the Open Ephys GUI visualizers

            Sockets to visualize Bonsai data in the Open Ephys GUI visualizers

    ..  grid-item::
        :child-align: center
        :margin: 0
        :padding: 0
        
        .. figure:: /_static/images/software/imgui-visualizer.png
            :alt: ImGUI visualizer in Bonsai

            ImGUI visualizer in Bonsai

|   **Extensibility**
|   Both options are open-source and provide options for extending functionality
    by providing the capability for users to create 
    `custom processors <https://open-ephys.github.io/gui-docs/Developer-Guide/index.html>`_ 
    (in the Open Ephys GUI) or 
    `custom operators <https://bonsai-rx.org/docs/articles/scripting-extensions.html>`_ and `packages <https://bonsai-rx.org/docs/articles/create-package.html>`_  
    (in Bonsai). Scripting packages to include Python code in Bonsai workflows are also available, and both the Open Ephys GUI and Bonsai can stream data to external applications using sockets.

Troubleshooting & Development
___________________________________

:doc:`oni_repl <oni-repl/index>` is a simple command-line application that can be used for
debugging and basic streaming IO with ONIX hardware.

..  tip:: ONIX uses an `ONI-compliant API
    <https://open-ephys.github.io/ONI/v1.0/api/index.html>`__ that is software
    agnostic. If you want to use ONIX hardware with your acquisition software,
    please :ref:`get in touch <support>`.

Deprecated Software
___________________________________

:doc:`Bonsai.ONIX <Bonsai.ONIX/index>` is the deprecated Bonsai ONIX
package which has been superseded by `OpenEphys.Onix1 <https://open-ephys.github.io/bonsai-onix1-docs/>`_.

