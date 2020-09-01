..
.. ## oni_init_ctx
.. Initialize a context, opening all file streams etc.
..
.. ```` {.c}
.. int oni_init_ctx(oni_ctx ctx)
.. ````
..
.. ### Arguments
.. - ``ctx`` context
..
.. ### Returns ``int``
.. - 0: success
.. - Less than 0: ``oni_error_t``
..
.. ### Description
.. Upon a call to ``oni_init_ctx``, the following actions take place
..
.. 1. All required data streams are opened.
.. 2. A device table is read from the firmware. It can be examined via calls t
..    ``oni_get_opt``.
.. 3. The data transmission packet size is calculated and stored. It can be
..    examined via calls to ``oni_get_opt``.
..
.. Following a successful call to ``oni_init_ctx``, the hardware's acquisition
.. parameters and run state can be manipulated using calls to ``oni_get_opt``.
..
.. ## oni_destroy_ctx
.. Terminate a context and free bound resources.
..
.. ```` {.c}
.. int oni_destroy_ctx(oni_ctx ctx)
.. ````
..
.. ### Arguments
.. - ``ctx`` context
..
.. ### Returns ``int``
.. - 0: success
.. - Less than 0: ``oni_error_t``
..
.. ### Description
.. During context destruction, all resources allocated by ``oni_create_ctx`` are
.. freed. This function can be called from any context run state. When called, an
.. interrupt signal (TODO: Which?) is raised and any blocking operations will
.. return immediately. Attached resources (e.g. file descriptors and allocated
.. memory) are closed and their resources freed.
..
.. ## oni_get_opt
.. Get context options.
..
.. ```` {.c}
.. int oni_get_opt(const oni_ctx ctx, int option, void* value, size_t *size);
.. ````
..
.. ### Arguments
.. - ``ctx`` context to read from
.. - ``option`` option to read
.. - ``value`` buffer to store value of ``option``
.. - ``size`` pointer to the size of ``value`` (including terminating null character,
..   if applicable) in bytes
..
.. ### Returns ``int``
.. - 0: success
.. - Less than 0: ``oni_error_t``
..
.. ### Description
.. The ``oni_get_opt`` function sets the option specified by the ``option`` argument
.. to the value pointed to by the ``value`` argument for the context pointed to by
.. the ``ctx`` argument. The ``size`` provides a pointer to the size of the option
.. value in bytes. Upon successful completion ``oni_get_opt`` shall modify the value
.. pointed to by ``size`` to indicate the actual size of the option value stored in
.. the buffer.
..
.. Following a successful call to ``oni_init_ctx``, the following socket options
.. can be read:
..
.. #### ``OE_CONFIGSTREAMPATH``\*
.. Obtain path specifying config data stream.
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``char *`` |
.. | option description  | A character string specifying the configuration stream path |
.. | default value       | /dev/xillybus_oni_config_32, \\\\.\\xillybus_oni_config_32 (Windows) |
..
.. #### ``OE_READSTREAMPATH``\*
.. Obtain path specifying input data stream.
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``char *`` |
.. | option description  | A character string specifying the input stream path |
.. | default value       | /dev/xillybus_oni_input_32 \\\\.\\xillybus_oni_input_32 (Windows) |
..
.. #### ``OE_WRITESTREAMPATH``\*
.. Obtain path specifying input data stream.
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``char *`` |
.. | option description  | A character string specifying the output stream path |
.. | default value       | /dev/xillybus_oni_output_32, \\\\.\\xillybus_oni_output_32 (Windows) |
..
.. #### ``OE_SIGNALSTREAMPATH``\*
.. Obtain path specifying hardware signal data stream
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``char *`` |
.. | option description  | A character string specifying the signal stream path |
.. | default value       | /dev/xillybus_oni_signal_8, \\\\.\\xillybus_oni_signal_8 (Windows) |
..
.. #### ``OE_DEVICEMAP``
.. The device table.
..
.. | | |
..
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``oni_device_t *`` |
.. | option description  | Pointer to a pre-allocated array of ``oni_device_t`` structs |
.. | default value       | N/A |
..
.. #### ``OE_NUMDEVICES``
.. The number of devices in the device table.
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``oni_reg_val_t`` |
.. | option description  | The number of devices supported by the firmware |
.. | default value       | N/A |
..
.. #### ``OE_MAXREADFRAMESIZE``
.. The maximal size of a frame produced by a call to ``oni_read_frame`` in bytes.
.. This number is the size of the frame produced by every device within the device
.. table that generates read data.
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``oni_reg_val_t`` |
.. | option description  | Maximal read frame size in bytes |
.. | default value       | N/A |
..
.. #### ``OE_WRITEFRAMESIZE``
.. The maximal size of a frame accepted by a call to ``oni_write_frame`` in bytes.
.. This number is the size of the frame provided to ``oni_write_frame`` to update
.. all output devices synchronously.
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``oni_reg_val_t`` |
.. | option description  | Maximal write frame size in bytes |
.. | default value       | N/A |
..
.. #### ``OE_RUNNING``
.. Hardware acquisition run state. Any value greater than 0 indicates that acquisition is
.. running.
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``oni_reg_val_t`` |
.. | option description  | Any value greater than 0 will start acquisition |
.. | default value       | False |
..
.. #### ``OE_SYSCLKHZ``
.. System clock frequency in Hz. The PCIe bus is operated at this rate. Read-frame clock values
.. are incremented at this rate.
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``oni_reg_val_t`` |
.. | option description  | System clock frequency in Hz |
.. | default value       | N/A |
..
.. #### ``OE_ACQCLKHZ``
.. Acquisition clock frequency in Hz. Reads from devices are synchronized to this clock.
.. Clock values within frame data are incremented at this rate.
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``oni_reg_val_t`` |
.. | option description  | Acquisition clock frequency in Hz |
.. | default value       | 42000000 |
..
..
.. #### ``OE_BLOCKREADSIZE``
.. Number of bytes read during each ``read()`` syscall to the data read stream. This
.. option allows control over a fundamental trade-off between closed-loop response
.. time and overall performance. The minimum (default) value will provide the
.. lowest response latency. Larger values will reduce syscall frequency and may
.. improve processing performance for high-bandwidth data sources.
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``size_t`` |
.. | option description  | Size, in bytes, of ``read()`` syscalls |
.. | default value       | value of ``OE_MAXREADFRAMESIZE`` |
..
.. ## oni_set_opt
.. Set context options.
..
.. ```` {.c}
.. int oni_set_opt(oni_ctx ctx, int option, const void* value, size_t size);
.. ````
..
.. ### Arguments
.. - ``ctx`` context
.. - ``option`` option to set
.. - ``value`` value to set ``option`` to
.. - ``size`` length of ``value`` in bytes
..
.. ### Returns ``int``
.. - 0: success
.. - Less than 0: ``oni_error_t``
..
.. ### Description
.. The ``oni_set_opt`` function sets the option specified by the ``option`` argument to
.. the value pointed to by the ``value`` argument within ``ctx``. The ``size`` indicates
.. the size of the ``value`` in bytes.
..
.. The following context options can be set:
..
.. #### ``OE_CONFIGSTREAMPATH``\*
.. Set path specifying configuration data stream.
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``char *`` |
.. | option description  | A character string specifying the configuration stream path |
.. | default value       | /dev/xillybus_oni_config_32, \\\\.\\xillybus_oni_config_32 (Windows) |
..
.. #### ``OE_READSTREAMPATH``\*
.. Set path specifying input data stream.
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``char *`` |
.. | option description  | A character string specifying the input stream path |
.. | default value       | /dev/xillybus_oni_input_32, \\\\.\\xillybus_oni_input_32 (Windows) |
..
.. #### ``OE_WRITESTREAMPATH``\*
.. Set path specifying input data stream.
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``char *`` |
.. | option description  | A character string specifying the output stream path |
.. | default value       | /dev/xillybus_oni_output_32, \\\\.\\xillybus_oni_output_32 (Windows) |
..
.. #### ``OE_SIGNALSTREAMPATH``\*
.. Set path specifying hardware signal data stream
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``char *`` |
.. | option description  | A character string specifying the signal stream path |
.. | default value       | /dev/xillybus_oni_signal_8, \\\\.\\xillybus_oni_signal_8 (Windows) |
..
.. #### ``OE_RUNNING``\*\*
.. Set/clear data input gate. Any value greater than 0 will start acquisition.
.. Writing 0 to this option will stop acquisition, but will not reset context
.. options or the sample counter. All data not shifted out of hardware will be
.. cleared. To obtain the very first samples produced by high-bandwidth devices,
.. set ``OE_RUNNING`` _before_ a call to OE_RESET.
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type         | ``oni_reg_val_t`` |
.. | option description        | Any value greater than 0 will start acquisition |
.. | default value             | 0 |
..
.. #### ``OE_RESET``\*\*
.. Trigger global hardware reset. Any value great than 0 will trigger a hardware
.. reset. In this case, acquisition is stopped and all global hardware state (e.g.
.. sample counters, etc) is defaulted.
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type         | ``oni_reg_val_t`` |
.. | option description        | Any value greater than 0 will trigger a reset |
.. | default value             | Untriggered |
..
.. #### ``OE_BLOCKREADSIZE``\*\*\*
.. Number of bytes read during each ``read()`` syscall to the data read stream. This
.. option allows control over a fundamental trade-off between closed-loop response
.. time and overall performance. The minimum (default) value will provide the
.. lowest response latency. Larger values will reduce syscall frequency and may
.. improve processing performance for high-bandwidth data sources.
..
.. | | |
.. -|---------------------|--------------------------------------------------------------------|
.. | option value type   | ``size_t`` |
.. | option description  | Size, in bytes, of ``read()`` syscalls |
.. | default value       | value of ``OE_MAXREADFRAMESIZE`` |
..
.. \* Invalid following a successful call to ``oni_init_ctx``. Before this, will
.. return with error code ``OE_EINVALSTATE``.
..
.. \*\* Invalid until a successful call to ``oni_init_ctx``. After this, will
.. return with error code ``OE_EINVALSTATE``.
..
.. \*\*\* Invalid until a successful call to ``oni_init_ctx`` and before acquisition
.. is started by setting the ``OE_RUNNING`` context option. In other states, will
.. return with error code ``OE_EINVALSTATE``.
..
.. ## oni_read_reg
.. Read a configuration register on a specific device.
..
.. ```` {.c}
.. int oni_read_reg(const oni_ctx ctx, size_t dev_idx, oni_reg_addr_t addr, oni_reg_val_t *value);
.. ````
..
.. ### Arguments
.. - ``ctx`` context
.. - ``dev_idx`` physical index number
.. - ``addr`` The address of register to write to
.. - ``value`` pointer to an int that will store the value of the register at ``addr``
..   on ``dev_idx``. This contents of this pointer will first be written to register
..   programming bus, since some devices need to use it to recieve a valid read.
..   e.g. using an SPI bus where reads are initialized by the value on MOSI one
..   transation prior.
..
.. ### Returns ``int``
.. - 0: success
.. - Less than 0: ``oni_error_t``
..
.. ### Description
.. ``oni_read_reg`` is used to read the value of configuration registers from devices
.. within the current device table. This can be used to verify the success of calls
.. to ``oni_read_reg`` or to obtain state information about devices managed by the
.. current context.
..
.. ## oni_write_reg
.. Set a configuration register on a specific device.
..
.. ```` {.c}
.. int oni_write_reg(const oni_ctx ctx, size_t dev_idx, oni_reg_addr_t addr, oni_reg_val_t value);
.. ````
..
.. ### Arguments
.. - ``ctx`` context
.. - ``dev_idx`` the device index to read from
.. - ``addr`` register address within the device specified by ``dev_idx`` to write
..   to
.. - ``value`` value with which to set the register at ``addr`` on the device
..   specified by ``dev_idx``
..
.. ### Returns ``int``
.. - 0: success
.. - Less than 0: ``oni_error_t``
..
.. ### Description
.. ``oni_write_reg`` is used to write the value of configuration registers from
.. devices within the current device table. This can be used to set configuraiton
.. registers for devices managed by the current context. For example, this is used
.. to perform configuration of ADCs that exist in a device table. Note that
.. successful return from this function does not guarantee that the register has
.. been properly set. Confirmation of the register value can be made using a call
.. to ``oni_read_reg``.
..
.. ## oni_read_frame
.. Read high-bandwidth data from the read channel.
..
.. ```` {.c}
.. int oni_read_frame(const oni_ctx ctx, oni_frame_t **frame)
.. ````
..
.. ### Arguments
.. - ``ctx`` context
.. - ``frame`` Pointer to a ``oni_frame_t`` pointer
..
.. ### Returns ``int``
.. - 0: success
.. - Less than 0: ``oni_error_t``
..
.. ### Description
.. ``oni_read_frame`` allocates host memory and populates it with an ``oni_frame_t``
.. struct corresponding to a single [frame](#frame), with a read header, from the
.. data input channel. This call will block until either enough data to construct
.. a frame is available on the data input stream or
.. [``oni_destroy_ctx``](#oni_destroy_ctx) is called. It is the user's repsonisbility
.. to free the resources allocated by this call by passing the resulting frame
.. pointer to [``oni_destroy_frame``](#oni_destroy_frame).
..
.. ## oni_destroy_frame
.. Free heap-allocated frame.
..
.. ````{.c}
.. void oni_destroy_frame(oni_frame_t *frame);
.. ````
..
.. ### Arguments
.. - ``frame`` pointer to an ``oni_frame_t``
..
.. ### Returns ``void``
.. There is no return value.
..
.. ### Description
.. ``oni_destroy_frame`` frees a heap-allocated frame. It is generally used to clean
.. up the resources allocated by [``oni_read_frame``](#oni_read_frame).
..
.. ## oni_write
.. Write data to the data write channel.
..
.. ```` {.c}
.. int oni_write_frame(const oni_ctx ctx, size_t dev_idx, const void *data, size_t data_sz)
.. ````
..
.. ### Arguments
.. - ``ctx`` context
.. - ``dev_idx`` device to write to
.. - ``data`` pointer to data to write
.. - ``data_sz`` number of bytes to write
..
.. ### Returns ``int``
.. - 0: success
.. - Less than 0: ``oni_error_t``
..
.. ### Description
.. ``oni_write_frame`` writes block data to a particular device from the device table
.. using the asynchronous data write channel. If ``dev_idx`` is not a writable
.. device, or if ``data_sz`` does not equal to ``write_size`` the of the device, this
.. function will return ``OE_EDEVIDX`` and ``OE_EWRITESIZE``, respectively.
..
.. ## oni_version
.. Report the oepcie library version.
..
.. ```` {.c}
.. void oni_version(int major, int minor, int patch)
.. ````
..
.. ### Arguments
.. - ``major`` major library version
.. - ``minor`` minor library version
.. - ``patch`` patch number
..
.. ### Returns ``void``
.. There is no return value.
..
.. ### Description
.. This library uses [semantic versioning](www.semver.org). Briefly, the major
.. revision is for incompatible API changes. Minor version is for backwards
.. compatible changes. The patch number is for backwards-compatible bug fixes.
..
.. ## oni_error_st
.. Convert an [error number](#oni_error_t) into a human readable string.
..
.. ```` {.c}
.. const char *oni_error_str(int err)
.. ````
..
.. ### arguments
.. - ``err`` error code
..
.. ### returns ``const char *``
.. Pointer to an error message string
..
.. ## oni_device_str
.. Convert a [device ID](#oni_device_t) into human readable string. _Note_: This is
.. an extension function available in oedevices.h.
..
.. ```` {.c}
.. const char *oni_device(ind dev_id)
.. ````
..
.. ### Arguments
.. - ``dev_id`` device id
..
.. ### Returns ``const char *``
.. Pointer to a device id string
