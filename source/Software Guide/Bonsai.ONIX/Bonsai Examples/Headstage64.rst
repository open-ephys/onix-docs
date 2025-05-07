.. include:: ../deprecation-notice.rst

.. _bonsai_headstage64:

Headstage-64 Workflow
===============================
This example workflow shows how the data streams produced by
:ref:`headstage_64` can be acquired and saved, as well as used for commutation. Each group workflow at the top
level contains acquisition code for a different sensor on the headstage. Example
Python and MATLAB scripts are provided to load the data produced by the
workflow. 

.. raw:: html

    {% with static_path = '../../../_static', name = 'Headstage64' %}
        {% include 'workflow.html' %}
    {% endwith %}


BNO055 9-Axis IMU
    Absolute orientation measurement of the headstage along with a lot of other
    information

RHD2164 Ephys Chip
    64-channels of extracellular electrophysiology input

TS4231 Lighthouse Receivers
    3D position of the headstage in space when used with appropriate lighthouse setup. 
    
Headstage Port Control
    Control over the headstage port and connectivity status logging 

.. note:: 
    This workflow does not demonstrate stimulation capabilities of the
    headstage. See :ref:`bonsai_estimdev` and :ref:`bonsai_ostimdev` for
    examples of how to control onboard stimulation.

Loading Scripts
--------------------------
The following scripts can be used to load the data produced by this workflow in Python (using Numpy) or MATLAB:

- Python: :download:`load_headstage64.py <../../../_static/bonsai/workflows/load_headstage64.py>` 
- MATLAB: :download:`load_headstage64.m <../../../_static/bonsai/workflows/load_headstage64.m>` 
