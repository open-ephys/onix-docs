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
community. There are a few important considerations when selecting which to use:

|   **User Experience**
|   The Open Ephys GUI is a turnkey application where data acquisition and
    signal processing pipelines are constructed by connecting processors.
    Bonsai is a visual programming language where data acquisition and
    signal processing pipelines are constructed by connecting operators. The
    Open Ephys GUI is more user-friendly whereas expertise is helpful to
    take full advantage of Bonsai. 

..  grid::
    :margin: 0
    :padding: 0
    
    ..  grid-item::
        :child-align: center
        :margin: 0
        :padding: 0

        ..  image:: /_static/images/software/example-signal-chain.png
            :alt: screenshot of example signal chain

    ..  grid-item::
        :child-align: center
        :margin: 0
        :padding: 0

        ..  image:: /_static/images/software/example-workflow.png
            :alt: screenshot of example workflow

|   **ONIX Support**
|   OpenEphys.Onix1 in Bonsai has a greater degree of support for ONIX
    capabilities than ONIX Source in the Open Ephys GUI. For more information on
    this, visit the `ONIX Source plugin page <https://open-ephys.github.io/gui-docs/User-Manual/Plugins/Onix-Source.html#onix-support>`_.

|   **Performance/Closed-Loop Latency**
|   Bonsai is capable of operating with sub-millisecond closed-loop latencies.
    The Open Ephys GUI operates on the order of 20ms and more variable
    latencies.

|   **Data Visualization**
|   The Open Ephys GUI provides visualization tools specialized for presenting
    electrophysiology data (such as the `LFP viewer
    <https://open-ephys.github.io/gui-docs/User-Manual/Plugins/LFP-Viewer.html#layout-selection>`_).
    Bonsai provides type visualizers which are more agnostic to the kind of data
    that is being streamed.
    
..  grid::
    :margin: 0
    :padding: 0

    ..  grid-item::
        :child-align: center
        :margin: 0
        :padding: 0

        ..  image:: /_static/images/software/lfp-viewer.png
            :alt: screenshot of lfp viewer

    ..  grid-item::
        :child-align: center
        :margin: 0
        :padding: 0
        
        ..  image:: /_static/images/software/type-visualizer.png
            :alt: screenshot of type visualizer

..  note::

    -   Open Ephys GUI visualization tools can be used to visualize data
        acquired from Bonsai using sockets:
        
        ..  image:: /_static/images/software/sockets-end-result.webp
            :alt: screenshot of sockets visualization

    -   Bonsai visualization is improving with the integration of `Dear ImGUI
        <https://github.com/ocornut/imgui>`_ in the Bonsai.Ephys package:

        .. image:: /_static/images/software/imgui-visualizer.png
            :alt: screenshot of imgui visualizer

|   **Hardware/Software Compatibility and 3rd Party Integration**
|   Bonsai offers broader compatibility with many more options such as
    behavioral cameras, miniscopes, photometry systems, Arduino boards, Harp
    devices, and numerous additional instruments, as well as 3rd party software
    such as SLEAP/Deep Lab Cut for pose estimation. The Open Ephys GUI supports
    a subset of the items that Bonsai supports. For more information on what the
    Open Ephys GUI natively supports, visit the `hardware compatibility
    page
    <https://open-ephys.github.io/gui-docs/User-Manual/Compatible-hardware.html>`_
    and `browse the plugins
    <https://open-ephys.github.io/gui-docs/User-Manual/Plugins/index.html>`_.

|   **Extensibility**
|   Both options are open-source and provide options for extending functionality
    by provided the capability for users to create 
    `custom processors <https://open-ephys.github.io/gui-docs/Developer-Guide/index.html>`_ 
    (in the OE GUI) or 
    `custom operators <https://bonsai-rx.org/docs/articles/scripting-extensions.html>`_ 
    (in Bonsai).

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

