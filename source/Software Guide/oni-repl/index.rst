.. _oni_repl:

oni-repl
===================================

.. toctree::
    :maxdepth: 3
    :hidden:

    usage

``oni-repl`` is a simple `read-eval-print loop (REPL)
<https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop>`__ for
:ref:`liboni`. 

:Code: https://github.com/open-ephys/liboni/tree/main/api/liboni/liboni-test
:Compatibility: Any ONI-compliant hardware
:Download: :ref:`Latest Version <oni_repl_download>`

This program provides low-level control over a single
:ref:`oni_h_acquisition_context` and can be used to control ONI-compliant
hardware to perform the following:

- Parameterize and initialize an :ref:`oni_h_acquisition_context`
- Examine the :ref:`oni_h_device` table
- Examine device hub information
- Interact with individual devices
  
  - Read device registers
  - Write device registers
  - Stream :ref:`oni_h_frame` data

- Write data from device streaming channels to disk
- Bulk initialize device register state

.. note:: ``oni-repl`` was created for hardware debugging and as a test program
    for :ref:`liboni`. However, its simplicity and lack of abstraction compared to
    :ref:`bonsai_onixref` make it useful as an example of how to use :ref:`liboni` and
    quickly examining hardware state and hub firmware versions.

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

