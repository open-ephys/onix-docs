.. include:: ../deprecation-notice.rst

.. _bonsai_headstage_neuropix1e:

Headstage Neuropixels 1.0e Workflow
============================================
This example workflow shows how the data streams produced by
:ref:`headstage_neuropix1e` can be acquired and saved, as well as used for commutation. Each group workflow at the top
level contains acquisition code for a different sensor on the headstage. A probe visualizer is included.

.. important:: \Bonsai workflows that contain the :ref:`bonsai_NeuropixelsV1edev` node such as this one will not
    open/load unless the headstage is on. Make sure to configure the headstage port voltage and mode correctly using the :ref:`bonsai_onicontext` node with the parameters for the :ref:`headstage_neuropix1e` before connecting the headstage. This example is programmed to use a headstage on Port A, so it will only work in that configuration.
    
.. raw:: html

    {% with static_path = '../../../_static', name = 'HeadstageNeuropixelsV1e' %}
        {% include 'workflow-zip.html' %}
    {% endwith %}


BNO055 9-Axis IMU
    Absolute orientation measurement of the headstage along with a lot of other information

Neuropixels V1.0e Device
    384 channels of extracellular electrophysiology input from 960 selectable neuropixels 1.0 probe electrodes

.. note:: \Remember to configure the probe as described in :ref:`bonsai_NeuropixelsV1edev`. To save data, remember to configure and enable the appropriate workflow nodes.
    
Loading Scripts
--------------------------
The following script can be used to load the data produced by this workflow in Python (using Numpy):

- Python: :download:`load_headstage64.py <../../../_static/bonsai/workflows/load_neuropixelsv1e.py>` 
