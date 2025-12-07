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
community. There are a few important considerations when selecting which to use,
which you can read about below.

Software Comparison
___________________________________

|   **User Experience**
|   Open Ephys GUI is a user-friendly application specialized for acquiring,
    processing, and visualizing electrophysiology data by connecting processors
    to form signal chains. Bonsai is a visual programming language for
    acquiring, processing, and visualizing a variety of data types by connecting
    nodes/operators to form workflows. The Open Ephys GUI is typically easier
    for beginners, while Bonsai rewards expertise with greater flexibility such
    as the integration of complex logic into the workflow for behavioral
    experiments/stimulus delivery. 

|   **3rd Party Hardware and Software Support**
|   The Open Ephys GUI natively supports various neural data acquisition systems
    (see the `User Manual introduction page
    <https://open-ephys.github.io/gui-docs/User-Manual/index.html>`_) as well as
    a few other 3rd party devices (view the list of plugins in the `table of
    contents
    <https://open-ephys.github.io/gui-docs/User-Manual/Plugins/index.html>`_).
    Bonsai offers a larger array of 3rd party hardware options. Some families of
    devices that are supported in Bonsai and not in the Open Ephys GUI include
    cameras, miniscopes, Harp, and more. Additionally, Bonsai is capable of
    integrating SLEAP and DeepLabCut for pose estimation or BonVision for the
    presentation of virtual environments or visual stimuli. The Open Ephys GUI
    does not have video capabities.
    
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
|   The OpenEphys.Onix1 package in Bonsai supports the full set ONIX's features.
    The ONIX Source plugin in the Open Ephys GUI supports a subset. For more
    details, visit the `ONIX Source plugin page
    <https://open-ephys.github.io/gui-docs/User-Manual/Plugins/Onix-Source.html#onix-support>`_.

|   **Performance/Closed-Loop Latency**
|   The Open Ephys GUI operates on the order of 20ms closed-loop latencies.
    Bonsai is capable of operating on the order of sub-millisecond closed-loop
    latencies and with lower variability of latencies.

|   **Data Visualization**
|   The Open Ephys GUI provides visualization tools specialized for presenting
    electrophysiology voltage data such as the `LFP viewer
    <https://open-ephys.github.io/gui-docs/User-Manual/Plugins/LFP-Viewer.html>`_
    with different waveform and raster views, and the `Probe viewer
    <https://open-ephys.github.io/gui-docs/User-Manual/Plugins/Probe-Viewer.html>`_
    for displaying high-density probe data. Bonsai provides type visualizers
    which are more agnostic to the kind of data that is being streamed.
        
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

Visualization of ephys data in Bonsai is undergoing improvement with the
integration of `Dear ImGUI <https://github.com/ocornut/imgui>`_ in the
Bonsai.Ephys package. Also, Open Ephys GUI visualization tools can be used to
visualize data acquired from Bonsai using sockets, as explained in `this
tutorial
<https://open-ephys.github.io/bonsai-onix1-docs/articles/tutorials/ephys-socket.html>`_.

..  grid::
    :margin: 0
    :padding: 0

    ..  grid-item::
        :child-align: center
        :margin: 0
        :padding: 0

        ..  figure:: /_static/images/software/sockets-end-result_GUI.jpg
            :alt: Sockets to visualize Bonsai data in the Open Ephys GUI visualizers

            Neuropixels Open Ephys GUI visualizer used for data acquired in Bonsai

    ..  grid-item::
        :child-align: center
        :margin: 0
        :padding: 0
        
        .. figure:: /_static/images/software/imgui-visualizer.png
            :alt: ImGUI visualizer in Bonsai

            ImGUI visualizer in Bonsai

|   **Extensibility**
|   Both options are open-source and provide options for extending functionality
    by providing the capability for users to create `custom processors
    <https://open-ephys.github.io/gui-docs/Developer-Guide/index.html>`_ in the
    Open Ephys GUI or `custom operators
    <https://bonsai-rx.org/docs/articles/scripting-extensions.html>`_ and
    `packages <https://bonsai-rx.org/docs/articles/create-package.html>`_ in
    Bonsai. Both can also stream data to external applications using sockets.
    Bonsai additionally provides packages for including Python code in Bonsai
    workflows. 

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

:doc:`Bonsai.ONIX <Bonsai.ONIX/index>` is the deprecated Bonsai ONIX package
which has been superseded by `OpenEphys.Onix1
<https://open-ephys.github.io/bonsai-onix1-docs/>`_.

