.. toctree::
    :hidden:
    
Updating Headstage Firmware
######################################

#.  If you have not already, download and unzip the
    :ref:`headstage_updater_download`.
    
#.  Download the latest :ref:`firmware image <headstage_image_download>` for
    the headstage you want to update. 

#.  Connect the headstage that you want to update to either Port A or Port B of
    your breakout board.

#.  Flip on the corresponding switch.

#.  Open the "ONIX Hub Updater" dialog by double-clicking the "CsHubUpdater.exe"
    file in file explorer.

    .. image:: /_static/images/hub-updater/onix-hub-updater_fields-empty.webp

#.  Populate the fields in the "ONIX Hub Updater" dialog.

    -   Select the firmware image by clicking on the :kbd:`...` button and
        navigating to where the firmware image was downloaded or entering its
        directory directly into the "Firmware File" field.
    -   Select the port where the headstage you want to update is connected.

    For example:

    .. image:: /_static/images/hub-updater/onix-hub-updater_fields-populated.webp

#.  Click the :kbd:`program` button in the "ONIX Hub Updater" dialog to open the
    "Update ready" dialog. This window provides information about the hardware
    that the selected firmware image targets in the left column and the hardware
    that is connected to the selected port in the right column. Make sure the
    "Hub Name", "HW revision", and "FW Version" fields in the left column match
    their respective fields in the right column before proceeding. If they
    don't, click :kbd:`Cancel` and confirm the following:

    -   The headstage you want to update is connected to the selected port.
    -   The firmware image you selected is for the headstage you want to update.  

    These fields must match before proceeding. For example:

    .. image:: /_static/images/hub-updater/update-ready_matching-fields.webp

#.  Click the :kbd:`program` button in the "Update ready" dialog to initiate the
    firmware flash process. The progress bar indicates that the flash process is
    underway. Do not touch the headstage or its port while waiting for this
    process is underway. 
    
    .. image:: /_static/images/hub-updater/update-ready_progress-bar.webp
    
    A "Success" dialog will appear when this process is completed, indicating
    your headstage is now updated.

    .. image:: /_static/images/hub-updater/success.webp
