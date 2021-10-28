.. _tethers:

Making Coaxial Tethers
==========================
ONIX headstages communicate with host hardware using a `50-Ohm
<https://en.wikipedia.org/wiki/Nominal_impedance#50_%CE%A9_and_75_%CE%A9>`__
`coaxial cable <https://en.wikipedia.org/wiki/Coaxial_cable>`__. Because these
tethers only have two conductors, replacing them or making tethers of custom
lengths is quite simple. This page describes methods for creating light and
flexible coaxial headstage tethers.

#. Obtain a suitable miniature 50-Ohm coaxial cable. These instructions use
   Axon Cable PCX40K10AK. It should be light, flexible (silicone or thin FEP), and
   thin (less than 1 mm in diameter) and made by a reputable supplier that can
   supply information on the cable's electrical characteristics. Most important
   are its `DC Resistance
   <https://en.wikipedia.org/wiki/Electrical_resistivity_and_conductivity>`__and
   `RF Loss** in the 1 GHz regime.

    .. note:: Although the actual quantities matter, and **smaller values are
        better**, the major hurdle is simply finding a supplier that will
        clearly characterize them as this an indication of quality. We have
        used cables from `axon
        <https://www.axon-cable.com/en/02_products/06_coaxial-cables/02/index.aspx>`__
        and `cooner wire <http://www.coonerwire.com/mini-coax/>`__ with good
        results.

    :DC Resistance: For DC signals, resistance is proportional to the inner
        conductor's resistivity and cross-sectional and inversely proportional
        to its length. Larger DC resistance will cause a higher voltage drop in
        the cable and require increase compensation at the voltage source. DC
        resistance is a strict function of the cable's size and smaller cables
        will have higher resistance.

        .. figure:: /_static/images/tether/resistivity_geometry.png
            :alt: A piece of resistive material with electrical contacts on both
                ends.  By User:Omegatron - Created by User:Omegatron using the
                GIMP, CC BY-SA 3.0,
                https://commons.wikimedia.org/w/index.php?curid=1699802
            :scale: 50%

            A piece of resistive material with electrical contacts on both
            ends. https://commons.wikimedia.org/w/index.php?curid=1699802

    :RF Loss: For radio-frequency signals, frequency-dependent resistance
        ("loss") is determined by the `skin effect
        <https://en.wikipedia.org/wiki/Skin_effect>`__ rather than conductor
        cross sectional area. Higher loss at a particular frequency will limit
        the length of cable over which signals can be reliably sent and
        received. RF loss is a complicated function of the cable's design (e.g.
        the use of `Litz wire
        <https://en.wikipedia.org/wiki/Litz_wire>`__ bundles will limit unused
        inner conductor area). Minimizing RF loss while maintaing
        characteristic impedance characteristics and impedance uniformity is
        and engineering challenge and requires precision manufacturing.

        .. figure:: /_static/images/tether/skin_depth.svg
            :alt: For alternating current, the current density decreases
                exponentially from the surface towards the inside.
                https://commons.wikimedia.org/w/index.php?curid=4453931
            :scale: 80%

            For alternating current, the current density decreases exponentially
            from the surface towards the inside.
            https://commons.wikimedia.org/w/index.php?curid=4453931
