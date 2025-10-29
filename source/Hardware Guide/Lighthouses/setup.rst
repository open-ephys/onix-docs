.. _lighthouse_setup:

Setup
#########################

1.  Mount 2 HTC Vive Base Station v1.0 Lighthouses over the behavioral arena.

    .. image:: ../../_static/images/lighthouses/vive_front.jpg
      :width: 48 %
    .. image:: ../../_static/images/lighthouses/vive_front.jpg
      :width: 48 %
 
    Follow these guidelines when deciding where to mount your lighthouses:
 
    .. On the headstage64, the photodiodes allow can accommodate up to at least distance 3m between the lighthouse receivers and transmitters. THIS REQUIRES CONFIRMATION TO INCLUDE IN DOCS, OTHERWISE DELETE.

    - They should be centered above and facing the area the behavioral arena
    - The lighthouses should have the same orientation.
    - The distance between the receiver and the transmitters should not exceed
      the maximum range. This depends on the sensitivity of the receiver's
      photodiode on the headstage and is best determined experimentally. Each
      lighthouse has a 120° field of view. However, the lighthouse receivers
      have a higher chance loosing line of sight of the transmitters at these
      larger angles if the headstage tilts. 
    - Position measurements are noisier when receivers are at the boundary of the
      transmitters' range, so leave a safe margin. 
    - A receiver must be in range of *both* transmitters in order to measure
      position. 
    - Secure the lighthouses such that they can't be easily jostled or moved. The lighthouses interrupt their emission during movement.

    ..  figure:: ../../_static/images/lighthouses/lighthouse_active-range.svg

        A cartoon of what a lighthouse & commutator commutator might look
        mounted on extruded aluminum rail. The overlapping green area represents
        the region where a TS4231 device is in range of both lighthouses and
        can measure position.

    ..  figure:: ../../_static/images/lighthouses/lighthouse-onix-figures-cropped.webp

        Crops of figures from `ONIX: a unified open-source platform for
        multimodal neural recording and perturbation during naturalistic
        behavior <https://www.nature.com/articles/s41592-024-02521-1>`_. The
        lighthouse transmitters are mounted on the ceiling and their range cover
        the entire ~2m range. The blue line represents a mouse's movement over
        ~8 hours.

    .. tip::
      To confirm if the lighthouse configuration covers the entire behavioral arena, slowly move 
      the TS4231 device through the entire arena while running 
      `an example workflow <https://open-ephys.github.io/bonsai-onix1-docs/articles/hardware/hs64/workflow.html>`_ and
      `inspecting the TS4231V1PositionData position data visualizer <https://open-ephys.github.io/bonsai-onix1-docs/articles/getting-started/visualize-data.html>`_. 
      If the TS4231V1PositionData operator ceases to produce data (i.e. if the visualizer stops updating) 
      at a certain spot, the current lighthouse configuration does not cover that spot. If you are unfamiliar with 
      using Bonsai to acquire Onix data to do this, visit the OpenEphys.Onix1 Bonsai package 
      `Getting Started page <https://open-ephys.github.io/bonsai-onix1-docs/articles/getting-started/index.html>`_.

    ..  figure:: ../../_static/images/lighthouses/lighthouse-mount-example.png

        How the actual hardware could look for mounting on extruded aluminum
        rail. 

2. Connect one power adaptor to each lighthouse.

3. Using an audio to audio cable, connect the basestations to each other to
   synchronise them.

   .. image:: ../../_static/images/connections/audio_synch_cable.jpg
       :width: 48%
   .. image:: ../../_static/images/lighthouses/vive_back.jpg
       :width: 48%

4. Manage the cables such that they don't occlude the TS4231 receivers from the lighthouse transmitters.

5. Set one lighthouse to 'A' and one to 'b' using the channel button
   (illustration below is from the `Vive manual
   <https://www.vive.com/eu/support/vive/category_howto/about-the-base-stations.html>`_)

   .. raw:: html

      <div class="row">
        <div class="col-lg-7 col-md-7 col-sm-12 col-xs-12 d-flex">
          <div class="card border-light">
            <img class="card-img-top" src="https://www.vive.com/media/filer_public/support_zip_img/eu/www/vive/guid-ecaa213d-acf9-441c-923c-9d230934f25a-web.png" alt="Vive lighthouse use" style="margin: 0 auto">
          </div>
        </div>
        <div class="col-lg-5 col-md-5 col-sm-12 col-xs-12 d-flex" style="margin-top: 0em!important">
              <p class="card-text">
              <ul class="simple">
              <p>1.	Status light</p>
              <p>2.	Front panel</p>
              <p>3.	Channel indicator (recessed)</p>
              <p>4.	Power port</p>
              <p>5.	Channel button</p>
              <p>6.	Sync cable port (optional)</p>
              <p>7.	Micro-USB port (for firmware updates)</p>
              </ul>
        </div>
      </div>
