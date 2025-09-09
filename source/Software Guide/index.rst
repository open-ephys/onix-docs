.. |software_logo| image:: /_static/noun_macbook.svg
  :height: 60

.. _software_guide:

|software_logo| Software Guide
===================================

.. toctree::
    :hidden:

    Bonsai Package Docs <https://open-ephys.github.io/bonsai-onix1-docs/>
    Open Ephys GUI <https://open-ephys.github.io/gui-docs/User-Manual/Plugins/Onix-Source.html>
    oni-repl/index
    Deprecated Software<Bonsai.ONIX/index>

There are two recommended software programs to acquire data from the ONIX system. Click on the cards below to navigate to their respective documentation sites.  


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

Both are free and open-source and widely used. Some considerations to choose between them are:
 
- The Open Ephys GUI is an application while Bonsai is a programming language. In the OE GUI users configure a signal processing pipeline from modules that have standalone functionality while in Bonsai are performed step by step with individual nodes connected in sequence. The Open Ephys GUI has extensive visualizers for ephys data, pre-defined data formats and file management and error reporting.

- The Open Ephys GUI was developed to acquire, visualize and process extracellular electrophysiology data and analog and digital lines from a variety of acquisition devices. It can drive output to a few devices such as the Open Ephys Acquisition Board, PulsePal and Arduino boards. Bonsai can work extensively with ephys and image data, and can be used to build task logic and stimuli presentation. It interfaces with acquisition systems, industrial behavioral cameras, miniscopes, photometry systems, Arduino boards, Harp devices and many more.
  
- Both the Open Ephys GUI and Bonsai have many online data processing modules available (phase detection, spike sorting, centroid tracking, pose estimation, machine learning algorithms). Having Bonsai control all the experimental hardware makes it more flexible, easier to prototype and scale different experiments. For example, triggering ephys or miniscope recording to file based on the animal's location in space, or closed-loop applications.

- ONIX in Bonsai can achieve sub-ms closed-loop latencies while the Open Ephys GUI latencies are in the order of 20ms and more variable.

- In addition to having numerous modules, both are extensible: you can write your own plug-ins/packages and you can interact with other applications via communication protocols such as OSC, ZMQ and TCP. Bonsai also supports C# and Python scripting within workflows. 

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
package which has been superseded by `OpenEphys.Onix1 <https://open-ephys.github.io/bonsai-onix1-docs/>`__.

