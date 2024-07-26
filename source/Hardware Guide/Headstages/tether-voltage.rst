.. _tether_voltage:

Tethered Headstage Voltages
==============================
The voltage on the headstage must be carefully regulated: if its too low the
headstage will not function reliably. If the voltage is too high sensitive
components could be damaged. Many issues with the system can be traced back to
inadequate headstage voltage supply.


Setting headstage voltage
--------------------------
Each headstage has a minimum and maximum voltage requirement (e.g. 5.3 to  5.7
Volts for :ref:`headstage_64`) circuits on the board to function properly. If
the voltage is far too low, the green LED on the headstage will be dim and
Bonsai will not detect the headstage. Even if the LED is bright, a borderline
voltage can still cause connectivity issues as the headstage occasionally dips
beneath the power it needs to function properly.

.. raw:: html

    <div class="container">
    <p>The voltage output at the FMC-host can be set in Bonsai:</p>
    <div class="figure align-default" id="id1">
      <a class="reference internal" href="../../_static/images/tether-voltage/setting_hs_voltage_default.png"><img src="../../_static/images/tether-voltage/setting_hs_voltage_default_low.png" /></a>
      <p class="caption"><span class="caption-text">Default headstage voltage is 4.9 V</span></p>
    </div>
    <div class="figure align-default" id="id2">
      <a class="reference internal" href="../../_static/images/tether-voltage/second_headstage.png"><img src="../../_static/images/tether-voltage/second_headstage_low.png" /></a>
      <p class="caption"><span class="caption-text">Increasing the voltage to 7V in Bonsai (measured as 5V at the headstage) allows the second headstage to connect.</span></p>
    </div>
    </div>

The voltage set in Bonsai is not identical to the voltage supplied to the
headstage, as some voltage drop will occur over the coaxial cable tether that
connects them. The amount of voltage drop will depend on the cable properties
(e.g. thickness) and even the temperature of the cable. These very thin tethers
can cause large voltage drops, so that even when the voltage setting in Bonsai
seems high, the headstage is only seeing 3 or 4 Volts and becomes unreliable.
Voltage should therefore always be measured on the headstage itself. The
voltage setting is persistent until computer power off. It gets stored in the
hardware, so even after a reboot, it will be set to the latest value.

.. _measure_voltage:

Measuring headstage voltage
----------------------------
Use a multimeter to probe the headstage at the two points marked below: the
ground pin and either terminal of the large inductor on the headstage.

.. list-table:: GND and Vcoax location
   :class: borderless
   :widths: 30 30 30

   * - .. figure :: ../../_static/images/tether-voltage/measure-voltage-64.png

          Headstage-64

     - .. figure :: ../../_static/images/tether-voltage/measure-voltage-npix.png

          Neuropixels-1.0 Headstage

     - .. figure :: ../../_static/images/tether-voltage/measure-voltage-rhs2116.webp

          RHS2116 Headstage

   * - .. figure :: ../../_static/images/tether-voltage/measure-voltage-np1e.webp

          Neuropixels-1.0e Headstage

     - .. figure :: ../../_static/images/tether-voltage/measure-voltage-np2e.png

          Neuropixels-2.0e Headstage

     - .. figure :: ../../_static/images/tether-voltage/measure-voltage-np2eBeta.png

          Neuropixels-2.0eBeta Headstage

Rebooting
--------------------------
If you have slowly increased the voltage supplied to a headstage, but it does
not appear as a tab in the ONI-Context, try turning the voltage supply to 0 and
back to the higher value before refreshing the ONI-Context.
