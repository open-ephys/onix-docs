.. |software_logo| image:: /_static/noun_macbook.svg
  :height: 60

.. |_| unicode:: 0xA0 
   :trim:

.. _software_guide:

|software_logo| Software Guide
===================================

.. toctree::
    :hidden:

    Bonsai Package Docs <https://open-ephys.github.io/bonsai-onix1-docs/>
    Open Ephys GUI/index
    oni-repl/index
    Bonsai.ONIX/index

There are various software to acquire data from the ONIX system:  

..  grid:: 3

    ..  grid-item-card:: Bonsai Package OpenEphys.Onix1
        :link-type: url
        :link: https://open-ephys.github.io/bonsai-onix1-docs/
        :class-card: intro-card
        :img-top: /_static/images/bonsai-logo.svg
        :img-alt: bonsai logo
        :class-img-top: software-card-img

        Acquire data from ONIX in Bonsai, a visual programming language for more extensive data
        processing and low-latency (<1 ms latencies) feedback.

    ..  grid-item-card:: Open Ephys GUI plugin ONIX |_| Source 
        :link-type: ref
        :link: open_ephys_gui
        :class-card: intro-card
        :img-top: /_static/images/oe-gui-logo.svg
        :img-alt: open ephys gui logo
        :class-img-top: software-card-img

        Acquire data from ONIX in the Open Ephys GUI, a turnkey solution for acquiring and
        visualizing electrophysiology data.  


Troubleshooting & Development
___________________________________

:doc:`oni_repl <oni-repl/index>` is a simple command-line application that can be used for
debugging and basic streaming IO with ONIX hardware.

..  tip:: ONIX uses an `ONI-compliant API
    <https://open-ephys.github.io/ONI/api/index.html>`__ that is software
    agnostic. If you want to use ONIX hardware with your acquisition software,
    please :ref:`get in touch <support>`.

Deprecated Software
___________________________________

-   :doc:`Bonsai.ONIX <Bonsai.ONIX/index>` is the deprecated Bonsai ONIX
    package which has been superseded by `OpenEphys.Onix1 <https://open-ephys.github.io/bonsai-onix1-docs/>`__.

