.. _faq:

FAQ
==========================

.. glossary::

    What is ONIX?
        Read :ref:`this page <what_is_onix>` for a high-level introduction to this hardware and how it differs from classic neuroscience acquisition systems.

    What does ONIX stand for?
        Open Neuro Interface X, the Open Ephys implementation of the `Open
        Neuro Interface specification <https://github.com/open-ephys/ONI>`__.

    How is ONI different than ONIX?
        `Open Neuro Interface <https://github.com/open-ephys/ONI>`__ is a hardware and
        API specification designed to meet the needs of experimental neuroscientists.
        ONIX hardware and `liboni <https://github.com/open-ephys/liboni>`__ are
        implementations of the ONI specification.

    What is Open Ephys?
        Open Ephys is a company and team of neuroscientists, engineers, and
        hackers who believe that neuroscience benefits greatly from advanced,
        well-documented, open-source hardware and software.  Have a look at the
        `Open Ephys Website <https://open-ephys.org/about-us-overview>`_ for a
        comprehensive overview of our mission and projects.

    Is ONIX hardware available for purchase?
        Yes, its available on the `Open Ephys Store <https://open-ephys.org/store/onix>`_.

    Where do I get help when using the system?
        Have a look at the :ref:`support` page.

    Can I use :ref:`headstage_64` with a silicon probe instead of tetrodes?
        Yes. Have a look at :ref:`adapters_eibs` to see if an option exists for
        your probe. If not, :ref:`get in touch <support>` because making an adapter
        is quite simple.

    Can I use my older Intan headstages with the system?
        No. ONIX headstages use serialization hardware to allow mixtures of
        devices to exist on the headstage. This is incompatible with older,
        SPI-based headstages. Have a look at :ref:`serialization` for more
        information on why.

    Why is there no Open Ephys GUI plugin for ONIX hardware?
        Have a look at the :ref:`open_ephys_gui` page.

    I have existing acquisition hardware. Can I can use your API and software to acquire data from it?
        Yes. We tried to design our API so that it decouples hardware details
        from software in a generic way. Have a look at the
        `Driver Translators <https://open-ephys.github.io/ONI/api/liboni/driver-translators/index.html>`_ page
        for more information on how to use the ONIX API with your hardware.
        Depending on how your device communicates with the computer it may only
        take 10's of lines of C.

    I have existing acquisition software. Can I integrate support for ONIX hardware using your API?
        Yes. Have a look at the `ONI API Documentation <https://open-ephys.github.io/ONI/api/index.html>`_
        to get started. Also let us know if you want help.

