.. _oni_repl:

Command Line Application
===================================

.. toctree::
    :hidden:
    :maxdepth: 1

    usage

``oni-repl`` is a simple `read-eval-print loop (REPL)
<https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop>`__ for
`liboni <https://open-ephys.github.io/ONI/api/liboni/index.html>`__. 

:Code: https://github.com/open-ephys/liboni/tree/main/api/liboni/oni-repl
:Compatibility: Any ONI-compliant hardware
:Download: :ref:`Latest Version <oni_repl_download>`

This program provides low-level control over a single
**Acquisition Context** and can be used to control ONI-compliant
hardware to perform the following:

- Parameterize and initialize an **Acquisition Context**
- Examine the **Device Table**
- Examine device hub information
- Interact with individual devices
  
  - Read device registers
  - Write device registers
  - Stream **Frame** data

- Write data from device streaming channels to disk
- Bulk initialize device register state

.. note:: ``oni-repl`` was created for hardware debugging and as a test program
   for `liboni <https://open-ephys.github.io/ONI/api/liboni/index.html>`__.
   However, its simplicity and lack of abstraction compared to
   :ref:`bonsai_onixref` make it useful as an example of how to use `liboni
   <https://open-ephys.github.io/ONI/api/liboni/index.html>`__ and for quickly
   examining hardware state and hub firmware versions.

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

