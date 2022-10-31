.. _oni_repl:

ONI REPL
===================================

.. toctree::
    :maxdepth: 3
    :hidden:

    installation
    usage

``oni-repl`` is a simple `read-eval-print loop (REPL)
<https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop>`__ for
:ref:`liboni`. This program provides low-level control over a single :ref:`oni_h_acquisition_context` and can be used to control ONI-compliant
hardware to perform the following:

- Parameterize and initialize an :ref:`oni_h_acquisition_context`
- Examine and the :ref:`oni_h_device` table
- Examine device hub information
- Interact with inidividual devices
  
  - Read registers
  - Write registers
  - Stream :ref:`oni_h_frame` data

- Write data from device streaming channels to disk
- Bulk initialize device register state

.. code-block:: none

       Jon Newman @ MIT                     **                
       Jie Zhang @ MIT                     ////               
       Aarón Cuevas López @ UPV             ///.              
       Josh Seigle @ Allen                  ///,.             
       Jakob Voigts @ MIT                   *///,             
                         *.                  ///,,            
                       ,####/                ///,,,           
                     ,,,,/####//             *///,,.          
                   ,,,,,   //##////           ///,,,          
                 ,,,,,      ,///#/////        ///.,,,         
               ,,,,,          //// //////     *///,,,,        
             ,,,,,             ,////  /////,   /// ,,,,       
            ,,,,                 ////   ,/////.///  ,,,       
         .,,,,                    .////    ,///##//  ,,,      
       .,,,,                        ////      */###/ .,,,     
      ,///***,,..........,,,...      ,////      /##(///,,,    
         .,,,,,,**,,..................,((((,..../(((((((((.   
              .,......,                .*(((/...,(((,,,(###   
                   .........              ////   ///.  ///,   
                        ........,          ,///* */// ////    
       Open Ephys Org.       .,......,       //// ///.///     
                                  ........,   *///(/////      
       Supporting open science         .,......,//((((//      
       since 2010.                          ....,/(##(/       
                                                 .,###.       
                                                              
       +--------------------+-------+-------+-------+-------+---------------------
       |                    |       |Firm.  |Read   |Wrt.   |     
       |Dev. idx            |ID     |ver.   |size   |size   |Desc.
       +--------------------+-------+-------+-------+-------+---------------------
    00 |00000: 0x00.0x00    |10     |1      |12     |32     |Open Ephys test device
    01 |00256: 0x01.0x00    |10     |1      |12     |32     |Open Ephys test device
    02 |00512: 0x02.0x00    |10     |1      |12     |32     |Open Ephys test device
    03 |00768: 0x03.0x00    |10     |1      |12     |32     |Open Ephys test device
       +--------------------+-------+-------+-------+-------+---------------------

