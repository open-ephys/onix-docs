.. _tether_voltage:

Headstage Voltages
==============================
Each ONIX headstage has a required operating voltage that is specified on its
documentation page. Because ONIX hardware supports headstages that have
different voltage requirements, it must be changed to match the requirements
of the headstage that is plugged into a port. If the headstage voltage is too
low, it will not function reliably. If the voltage is too high, the headstage 
will dissipate excess heat and it may be damaged.


Setting Headstage Voltage
--------------------------
The headstage voltage is set using :ref:`onidatasheet_fmc_link_control` devices
on the :ref:`pcie_host`.  Each headstage has a minimum and maximum voltage
requirement (e.g. 5.3 to  5.7 Volts for :ref:`headstage_64`) in order for
circuits on the board to function properly. If the voltage is far too low, the
host computer will not be able to detect the headstage. A borderline
voltage can still cause connectivity issues as the headstage occasionally dips
below the level it needs to function properly.

..  attention:: 
    The `OpenEphys.Onix1 <https://open-ephys.github.io/bonsai-onix1-docs/index.html>`__ 
    Bonsai package automatically sets the headstage port voltage by default, but allows 
    the user to override the voltage setting as well. The documentation linked shows how 
    to use this functionality and what valid voltage ranges are for each headstage. This
    functionality has been been tuned for the tethers that are shipped with each
    headstage. The voltage override is available when custom tethers are used
    (see :ref:`measure_voltage`).

The voltage set in software is not identical to the voltage supplied to the
headstage, as some voltage drop will occur over the tether that connects them. The
amount of voltage drop is proportional to the current draw of the headstage and
inversely proportional to the thickness of the tether. The thin tethers used
with ONIX headstages can result in significant voltage drops that need to be
compensated for. For very long (5 to 10m) and thin (diameter of 0.2mm) coaxial
tethers, the voltage drop can be on the order of 2 volts. For this reason, the
headstage voltage must be measured on the headstage itself.

.. _measure_voltage:

Measuring Headstage Voltage
-------------------------------
Use a multimeter to probe the headstage at the two points marked below: the
ground pin and either terminal of the large inductor on the headstage.

.. list-table:: GND and Vcoax location
   :class: borderless
   :widths: 30 30 30

   * - .. figure :: ../../_static/images/tether-voltage/measure-voltage-64.png

          Headstage-64

     - .. figure :: ../../_static/images/tether-voltage/measure-voltage-npix.png

          Neuropixels-1.0f Headstage

     - .. figure :: ../../_static/images/tether-voltage/measure-voltage-rhs2116.webp

          RHS2116 Headstage

   * - .. figure :: ../../_static/images/tether-voltage/measure-voltage-np1e.webp

          Neuropixels-1.0e Headstage

     - .. figure :: ../../_static/images/tether-voltage/measure-voltage-np2e.png

          Neuropixels-2.0e Headstage

     - .. figure :: ../../_static/images/tether-voltage/measure-voltage-np2eBeta.png

          Neuropixels-2.0eBeta Headstage
