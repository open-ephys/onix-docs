.. _lighthouse_setup:

Setup
#########################

1. Mount 2 Vive Base Station Lighthouse over the setup.

   .. image:: ../../_static/images/lighthouses/vive_front.jpg
     :width: 48 %
   .. image:: ../../_static/images/lighthouses/vive_front.jpg
     :width: 48 %

   Follow these guidelines to decide where to mount your two Lighthouse base stations:

   - They should be centered above and facing the area that will be occupied by the lighthouse receivers.   
   - The distance between the receiver and the transmitters should not exceed 3 meters, and each base station 
     has a 120° field of view. However, position measurements are noisier when receivers are at the boundary 
     of the transmitters' range, so leave a safe margin. A receiver must be in range of both transmitters 
     in order to measure position. 
   - Secure the base stations such that they can't be easily jostled or moved.
      
   .. tip::
      To confirm if the base station configuration covers the entire desired range, slowly move 
      the TS4231 device through the entire desired range while running 
      `an example workflow <https://open-ephys.github.io/bonsai-onix1-docs/articles/hardware/hs64/workflow.html>`_ and
      `inspecting the TS4231V1PositionData position data visualizer <https://open-ephys.github.io/bonsai-onix1-docs/articles/getting-started/visualize-data.html>`_. 
      If the TS4231V1PositionData operator ceases to produce data (i.e. if the visualizer stops updating) 
      at a certain spot, the current base station configuration does not cover that spot. If you are unfamiliar with 
      using Bonsai to acquire Onix data, visit the OpenEphys.Onix1 Bonsai package 
      `Getting Started page <https://open-ephys.github.io/bonsai-onix1-docs/articles/getting-started/index.html>`_.


   The image below shows an example of what a lighthouse setup might look with a commutator as well. 
   The overlapping green area represents the region where a TS4231 device is in range of both base stations 
   and can measure position.

   .. image:: ../../_static/images/lighthouses/lighthouse_active-range.svg

   The image below shows an example of how you can actually mount on extruded aluminum rail. 

   .. image:: ../../_static/images/lighthouses/lighthouse-mount-example.png

2. Connect one power adaptor to each base station.

3. Using an audio to audio cable, connect the basestations to each other to
   synchronise them.

   .. image:: ../../_static/images/connections/audio_synch_cable.jpg
       :width: 48%
   .. image:: ../../_static/images/lighthouses/vive_back.jpg
       :width: 48%

4. Manage the cables such that they don't occlude the TS4231 receivers from the Lighthouse base station transmitters.

5. Set one base station to 'A' and one to 'b' using the channel button
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
