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
        directory directly into the "Firmware File" field. The image should have
        a .onix file extension.
    -   Select the port where the headstage you want to update is connected.

    For example:

    .. image:: /_static/images/hub-updater/onix-hub-updater_fields-populated.webp

#.  Click the :kbd:`program` button in the "ONIX Hub Updater" dialog. This
    should open the "Update ready" dialog. 

    .. image:: /_static/images/hub-updater/update-ready_matching-fields.webp

    Confirm the "Hub Name", "HW revision", and "FW Version" match in both
    columns.

    ..  note:: 
        
        -   If you click :kbd:`program` and receive the following error message:

            .. image:: /_static/images/hub-updater/no-onix-system.webp

            Make sure your :ref:`PCIe Controller <pcie_host_firmware_update>` and
            :ref:`Breakout Board <breakout_setup>` are properly setup.

        -   If you click :kbd:`program` and receive the following error message:

            ..  image:: /_static/images/hub-updater/mismatched-image&hardware.webp

            Confirm:
            -   The headstage you want to update is connected to the selected port.
            -   The firmware image you selected is for the headstage you want to update.  

#.  Click the :kbd:`program` button in the "Update ready" dialog to initiate the
    firmware flash process. The progress bar indicates that the flash process is
    underway. Do not touch the headstage, its port, or its port's power switch
    while waiting for this headstage to finish being updated. 
    
    .. image:: /_static/images/hub-updater/update-ready_progress-bar.webp
    
    A "Success" dialog will appear when this process is completed, indicating
    your headstage is now updated.

    .. image:: /_static/images/hub-updater/success.webp
