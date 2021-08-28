#!/bin/bash

# Doesn't work
# wget -r -nd --no-parent -A '*.bonsai' https://raw.githubusercontent.com/jonnew/Bonsai.ONIX/main/ExampleWorkflows/

wget -N https://raw.githubusercontent.com/jonnew/Bonsai.ONIX/main/ExampleWorkflows/AnalogIO/AnalogIO.bonsai \
        https://raw.githubusercontent.com/jonnew/Bonsai.ONIX/main/ExampleWorkflows/AnalogIO/AnalogIO.bonsai \
        https://raw.githubusercontent.com/jonnew/Bonsai.ONIX/main/ExampleWorkflows/BNO055/BNO055.bonsai \
        https://raw.githubusercontent.com/jonnew/Bonsai.ONIX/main/ExampleWorkflows/ClockOutput/ClockOutput.bonsai \
        https://raw.githubusercontent.com/jonnew/Bonsai.ONIX/main/ExampleWorkflows/DigitalIO/DigitalIO.bonsai \
        https://raw.githubusercontent.com/jonnew/Bonsai.ONIX/main/ExampleWorkflows/ElectricalStimulator/ElectricalStimulator.bonsai \
        https://raw.githubusercontent.com/jonnew/Bonsai.ONIX/main/ExampleWorkflows/HeadstagePortControl/HeadstagePortControl.bonsai \
        https://raw.githubusercontent.com/jonnew/Bonsai.ONIX/main/ExampleWorkflows/NeuropixelsV1/NeuropixelsV1.bonsai \
        https://raw.githubusercontent.com/jonnew/Bonsai.ONIX/main/ExampleWorkflows/OpticalStimulator/OpticalStimulator.bonsai \
        https://raw.githubusercontent.com/jonnew/Bonsai.ONIX/main/ExampleWorkflows/RHD2164/RHD2164.bonsai \
        https://raw.githubusercontent.com/jonnew/Bonsai.ONIX/main/ExampleWorkflows/TS4231/TS4231.bonsai

# TODO: Get workflows for examples
