.. _oni_repl_usage:

Usage
====================================
.. toctree::
    :maxdepth: 3
    :hidden:

.. code-block:: console

    oni-repl <driver> [slot] [-d] [-D <value>] [-n <value>] [-i <device index>] 
    [--rbytes=<bytes>] [--wbytes=<bytes>] [--dumppath=<path>] [-h,--help] [-v,--version] 

Required Arguments
-----------------------------------
<driver>        
    Hardware driver to dynamically link (e.g. :ref:`riffa`,
    :ref:`ft600`, :ref:`test<test_driver>`, etc.)
[slot]           
    Index specifying the physical slot occupied by hardware being controlled.
    If none is provided, the driver-defined default will be used.

Command Line Options
-----------------------------------
-d 			Display frames. If specified, frames produced by the oni hardware will be printed to the console.
-D <percent> 		The percent of frames printed to the console if frames are displayed. Percent should be a value in (0, 100.0].
-n <count> 		Display at most count frames. Reset only on program restart. Useful for examining the start of the data stream.
-i <index> 		Only display frames from device with specified index value.
--rbytes=<bytes>   Set block read size in bytes. This number determines the latency/bandwidth tradeoff. Large block read sizes will reuslt in less frequent data transfers from hardware that can increase overall streaming bandwith of the system. This number imposes a lower bound on real-time latency since the system will need to accumulate the entire read block before data is transmitted.
--wbytes=<bytes>   Set write preallocation size in bytes. This number indicates the amount of memory is reserved for use by the write stream. Tuning my improve real-time performance depending on write frequency.
--dumppath=<path> 	Path to folder to dump raw device data. If not defined, no data will be written. A flat binary file with name <index>_idx-<id>_id-<datetime>.raw will be created for each device in the device table that produces streaming data. The bit-wise frame definition in the ONI device datasheet (as required by the ONI spec) will describe frame data is organized in each file.
--regpath=<path>   Path to a text file containing a table of the form:

                   .. code-block::

                       dev_addr_0 reg_address reg_value
                       dev_addr_1 reg_address reg_value
                       ...
                       dev_addr_n reg_address reg_value

                   that is used to bulk write device registers following context intialization.

--help, -h         Display this message and exit.
--version, -v      Display software version information.


REPL Commands
-----------------------------------
When the program is started with valid command line arguments, the user is
presented with an ASCII Open Ephys logo followed by the current Device Table
governed by the newly opened acquisition context along with a set of messages
reporting various option configurations that occurred during context
initialization. As indicated by these messages, acquisition is started
automatically when the program starts. Finally, a set of REPL commands is
presented for the user to interact with the hardware. These commands can be
used to change the runtime behavior of the hardware, read and write device
registers (as defined on their ONI-required datasheet), and display streaming
data. For example, here is the output when using the :ref:`riffa` for the
required ``<driver>`` command along with ONIX hardware (starting at device
index 0) and a single headstage (starting at device index 256).

.. code-block:: console

   $ ./liboni-test riffa 0 

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
          |                    |       |Firm.  |Read   |Wrt.   |
          |Dev. idx            |ID     |ver.   |size   |size   |Desc.
          +--------------------+-------+-------+-------+-------+---------------------
       00 |00000: 0x00.0x00    |12     |1      |8      |0      |Heartbeat
       01 |00001: 0x00.0x01    |23     |1      |10     |0      |Open Ephys FMC Host Board coaxial headstage link control circuit
       02 |00002: 0x00.0x02    |23     |1      |10     |0      |Open Ephys FMC Host Board coaxial headstage link control circuit
       03 |00003: 0x00.0x03    |7      |1      |12     |0      |32-bit digital input port
       04 |00004: 0x00.0x04    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       05 |00005: 0x00.0x05    |20     |1      |0      |0      |Open Ephys FMC Host Board rev. 1.3 clock output subcircuit
       06 |00006: 0x00.0x06    |22     |1      |32     |24     |Open Ephys FMC Host Board rev. 1.3 analog IO subcircuit
       07 |00007: 0x00.0x07    |18     |1      |12     |4      |Open Ephys Breakout Board rev. 1.3 digital and user IO
       08 |00008: 0x00.0x08    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       09 |00009: 0x00.0x09    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       10 |00010: 0x00.0x0a    |28     |1      |12     |0      |Acquisition hardware buffer usage reporting device
       11 |00011: 0x00.0x0b    |27     |1      |16     |8      |Variable load testing device
       12 |00012: 0x00.0x0c    |30     |1      |12     |0      |HARP Synchronization time input
       13 |00256: 0x01.0x00    |31     |1      |72     |0      |Intan RHS2116 bioamplifier and stimulator
       14 |00257: 0x01.0x01    |31     |1      |72     |0      |Intan RHS2116 bioamplifier and stimulator
       15 |00258: 0x01.0x02    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       16 |00259: 0x01.0x03    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       17 |00260: 0x01.0x04    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       18 |00261: 0x01.0x05    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       19 |00262: 0x01.0x06    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       20 |00263: 0x01.0x07    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       21 |00264: 0x01.0x08    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       22 |00265: 0x01.0x09    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       23 |00512: 0x02.0x00    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       24 |00513: 0x02.0x01    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       25 |00514: 0x02.0x02    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       26 |00515: 0x02.0x03    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       27 |00516: 0x02.0x04    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       28 |00517: 0x02.0x05    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       29 |00518: 0x02.0x06    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       30 |00519: 0x02.0x07    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       31 |00520: 0x02.0x08    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
       32 |00521: 0x02.0x09    |0      |0      |0      |0      |Placeholder device: neither generates or accepts data
          +--------------------+-------+-------+-------+-------+---------------------
       Max. read frame size: 88 bytes
       Max. write frame size: 32 bytes
       Setting block read size to: 2048 bytes
       Block read size: 2048 bytes
       Setting write pre-allocation buffer to: 2048 bytes
       Write pre-allocation size: 2048 bytes
       System clock rate: 250000000 Hz
       Frame counter clock rate: 250000000 Hz
       Hardware run state: 0
       Resetting acquisition clock and starting hardware run simultaneously...
       Hardware run state: 1
       Some commands can cause hardware malfunction if issued in the wrong order!
       Enter a command and press enter:
               d - toggle frame display
               D - change the percent of frames displayed
               i - Set in order to display frames only from a particular device
               t - print current device table
               p - toggle running/pause register (used for internal testing)
               s - toggle running/pause register & r/w thread operation (used for internal testing)
               r - read from device register
               w - write to device register
               h - get hub information about a device
               H - print all hubs in the current configuration
               a - reset the acquisition clock counter
               x - issue a hardware reset
               q - quit
       >>> 
