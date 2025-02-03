.. include:: deprecation-notice.rst

.. |download_image| image:: /_static/download.svg
  :height: 18
.. |copy_image| image:: /_static/copy.svg
  :height: 18

.. _bonsai_onixref:

Bonsai.ONIX (DEPRECATED)
===================================
..
    Important: The names of pages for nodes must match their Bonsai.ONIX class
    names so that documentation can be opened from the Bonsai Editor!

.. toctree::
    :maxdepth: 2
    :hidden:

    Installation
    GettingStarted
    Nodes/index
    Bonsai Examples/index

`Bonsai.ONIX <https://www.nuget.org/packages/Bonsai.ONIX/>`__ is a `Bonsai
<https://bonsai-rx.org/>`__ package for ONIX hardware. This package contains
`Bonsai Operators <https://bonsai-rx.org/docs/articles/operators.html>`__ for
acquiring and sending data to ONIX hardware. An additional package,
``Bonsai.ONIX.Design``, contains GUI elements for the core package. Although it
is possible to use ``Bonsai.ONIX`` without the GUI package, it is not
recommended. There are three major classes of operators in the package:

#. :ref:`bonsai_onicontext` - This operator wraps the underlying **Acquisition Context**
   and provides access to the device table for a hardware slot. At least one of these 
   operators is required in every workflow.
#. ``<Some>Device`` - These operators wrap individual :ref:`ONI Device
   <onidatasheets>`'s and provide access to their data IO and configuration
   registers.
#. Various helper operators that provide data conditioning functionality. E.g.
   for converting raw sensor data into 3D positions, etc.

Using this Documentation
--------------------------
This documentation contains functional workflows and operators. You can
download workflows by clicking the |download_image| icon.  Alternatively, you
can copy and paste them into the `Bonsai Workflow Editor
<https://bonsai-rx.org/docs/editor/>`__ by clicking the |copy_image| icon and
using ``Ctrl+v`` or equivalent in the editor:

.. raw:: html

    {% with static_path = '../../_static', name = 'HelloWorld' %}
        {% include 'workflow.html' %}
    {% endwith %}
