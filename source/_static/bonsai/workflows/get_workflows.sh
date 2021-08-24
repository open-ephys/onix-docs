#!/bin/bash

# Doesn't work
# wget -r -nd --no-parent -A '*.bonsai' https://github.com/jonnew/Bonsai.ONIX/tree/main/ExampleWorkflows/

wget -N https://github.com/jonnew/Bonsai.ONIX/tree/main/ExampleWorkflows/AnalogIO/AnalogIO.bonsai \
        https://github.com/jonnew/Bonsai.ONIX/tree/main/ExampleWorkflows/BNO055/BNO055.bonsai \
        https://github.com/jonnew/Bonsai.ONIX/tree/main/ExampleWorkflows/ClockOutput/ClockOutput.bonsai \
        https://github.com/jonnew/Bonsai.ONIX/tree/main/ExampleWorkflows/DigitalIO/DigitalIO.bonsai \
        https://github.com/jonnew/Bonsai.ONIX/tree/main/ExampleWorkflows/ElectricalStimulator/ElectricalStimulator.bonsai \
        https://github.com/jonnew/Bonsai.ONIX/tree/main/ExampleWorkflows/HeadstagePortControl/HeadstagePortControl.bonsai \
        https://github.com/jonnew/Bonsai.ONIX/tree/main/ExampleWorkflows/NeuropixelsV1/NeuropixelsV1.bonsai \
        https://github.com/jonnew/Bonsai.ONIX/tree/main/ExampleWorkflows/OpticalStimulator/OpticalStimulator.bonsai \
        https://github.com/jonnew/Bonsai.ONIX/tree/main/ExampleWorkflows/RHD2164/RHD2164.bonsai \
        https://github.com/jonnew/Bonsai.ONIX/tree/main/ExampleWorkflows/TS4231/TS4231.bonsai

# TODO: Get workflows for examples
