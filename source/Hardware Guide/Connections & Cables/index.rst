.. _connection_overview:

Connections and Cables
==========================================

.. image:: ../../_static/images/connections/connections.png
  :align: center

Connection types
******************************************
.. _headstage_link:

Headstage Link
--------------------------------
The headstage link allows fast data communication between an ONI compliant headstage and the PCIe host board. This connection is formed by a single coaxial cable for each attached headstage (or other ONI compliant hub, such as a UCLA Miniscope V4). This connection also provides power to the headstage from the PCIe host board.

The headstage link can be formed directly between the host PCIe board and a headstage. Alternatively, a headstage link can include an active commutator and/or breakout board between the PCIe board and headstage.

.. image:: ../../_static/images/connections/headstage.png
  :align: center
  :width: 70%

Connectors used for headstage link:

.. image:: ../../_static/images/connections/3_connectors_annotated.jpg
  :align: center
  :width: 50%

* PCIe host board: MMCX connectors
* Breakout board: MMCX connectors (to link to PCIe host) & SMA connectors (to link to commutator or headstage).
* Commutator: SMA connectors to link to both breakout board and headstage. To
  learn how to use an elastic string and the hook on the commutator gear to
  counterweigh the headstage and keep the tether out of the
  animal's way while it explores the behavioral arena, visit the `Tether
  Management & Headstage Counterweight
  <https://open-ephys.github.io/commutator-docs/user-guide/tether-management_counterweight.html>`_
  page from the `Commutator Docs <https://open-ephys.github.io/commutator-docs/index.html>`_. 
* The :ref:`headstage_64` & :ref:`headstage_neuropix1`:  Hirose X.FL-PR-SMT1-2(80) X.FL coaxial socket connector.


Digital and Analog I/O
--------------------------------
.. image:: ../../_static/images/connections/IO.png
  :align: center
  :width: 70%

* `High speed digital cable
  <https://multimedia.3m.com/mws/media/585365O/3mtm-shrunk-delta-ribbon-sdr-cable-assembly-ts2287.pdf>`_
  to connect Host and Breakout Board.

Lighthouses
--------------------------------
.. image:: ../../_static/images/connections/lighthouse.png
  :align: center
  :width: 70%

* Audio (Lighthouse A) to Audio (Lighthouse B) - to synchronise lighthouses
  (only necessary for V1 Basestations)
* Power cables for lighthouses (x2, provided with lighthouses)

Commutator link
--------------------------------
.. image:: ../../_static/images/connections/commutator.png
  :align: center
  :width: 70%

* Computer (USB) to commutator (micro-USB) cable, to power the commutator &
  provide orientation data.

.. _cable_list:

Cable List
******************************************

.. raw:: html

    <div class="row">
      <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12 d-flex">
      <div class="gallery-card">
          <img src="../../_static/images/connections/breakout_IO_cable.jpg" alt="Breakout Board IO cable">
          <div class="card-body flex-fill">
              <h5 class="gallery-card. card-header d-flex">Digital & Analog I/O Cable</h5>
              <p>- SDR to SDR 26 POS</p>
              <p>- Breakout Board to PCIe Host, Digital and Analog I/O</p>
          </div>
        </div>
      </div>
      <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12 d-flex">
        <div class="gallery-card">
          <img src="../../_static/images/connections/audio_synch_cable.jpg" alt="Audio jack cable to synchronise lighthouses">
          <div class="card-body flex-fill">
              <h5 class="card-header">Lighthouse Sync Cable</h5>
              <p>- 3.5 mm Stereo Jack Plug to Plug </p>
              <p>- Connects two Vive Basestations</p>
          </div>
        </div>
      </div>
      <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12 d-flex">
      <div class="gallery-card">
          <img src="../../_static/images/connections/sma_cable.jpg" alt="SMA-SMA Cable">
          <div class="card-body flex-fill">
              <h5 class="card-header">Headstage Link: SMA Cable</h5>
              <p>- SMA to SMA cable</p>
              <p>- Breakout Board to Commutator, Headstage Link</p>
          </div>
        </div>
      </div>
      </div>

      <div class="row">
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12 d-flex">
        <div class="gallery-card">
            <img src="../../_static/images/connections/adaptor_headstage.jpg" alt="Adaptor cable connecting SMA to MMCX">
            <div class="card-body flex-fill">
                <h5 class="card-header">Headstage Link: Adaptor</h5>
                <p>- SMA to MMCX</p>
                <p>- Connects headstage tether to PCIe Host board</p>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12 d-flex">
        <div class="gallery-card">
            <img src="../../_static/images/connections/MMCX_cable.jpg" alt="MMCX to MMCX cable">
            <div class="card-body flex-fill">
                <h5 class="card-header">Headstage Link: MMCX cable</h5>
                <p>- MMCX to MMCX </p>
                <p>- PCIe Host to Breakout Board</p>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12 d-flex">
        <div class="gallery-card">
            <img src="../../_static/images/connections/tether.jpg" alt="Micro-coax headstage tether">
            <div class="card-body flex-fill">
                <h5 class="card-header">Headstage Link: Micro-Coax Headstage Tether</h5>
                <p>- SMA to Hirose X.FL, Coaxial, 0.38 mm OD</p>
                <p>- Breakout Board to Headstage, PCIe to Headstage (with adaptor)</p>
            </div>
          </div>
        </div>
      </div>


.. _mmcx_cable:

Connecting MMCX
------------------------------

The MMCX connectors at the end of these cables can easily break off if used incorrectly. When connecting or disconnecting, hold the connector itself instead of pulling at the cabling.

.. raw:: html

  <details open><summary> View how to connect and disconnect MMCX:
  </summary>
  <div class="row">
    <div class="col-lg-3 col-md-3 col-sm-0 col-xs-0 d-flex">
    </div>
    <div class="col-lg-3 col-md-3 col-sm-12 col-xs-12 d-flex">
      <img src="../../_static/images/connections/insertMMCX.gif" alt="GIF of cable inserted while holding connector" style="margin: 2em; width: 135px; height: 240px">
    </div>
    <div class="col-lg-3 col-md-3 col-sm-12 col-xs-12 d-flex">
      <img class="card-img-top" src="../../_static/images/connections/removeMMCX.gif" alt="GIF of cable removed while holding connector" style="margin: 2em; width: 135px; height: 240px">
    </div>
    <div class="col-lg-3 col-md-3 col-sm-0 col-xs-0 d-flex">
    </div>
  </div>
  </details>

Connecting Micro-Coax Headstage Tethers
-----------------------------------------

The micro-coax tether is attached to the headstage via a Hirose X.FL coaxial connector and we use a red piece of tubing as a grip sleeve to secure the tether to the tether anchor tab present on the headstage so as to provide strain relief. 

.. image:: ../../_static/images/connections/connect_microcoax_tether.png
  :align: center
  :width: 70%

It is possible to remove the tether, but since it is made to have a snug fit we don't recommend doing this often - only for replacing the tether.