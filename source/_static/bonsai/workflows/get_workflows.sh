#!/bin/bash
rm -fr ./Bonsai.ONIX
git clone --depth 1 git@github.com:jonnew/Bonsai.ONIX.git
find ./Bonsai.ONIX/ExampleWorkflows -mindepth 2 -type f -exec mv -t ./ -f '{}' +

# Zip NeuropixelsV1 stuff
rm -f ./NeuropixelsV1.zip
zip -r NeuropixelsV1.zip NeuropixelsV1.bonsai NeuropixelsV1.bonsai.layout probe_image.frag quad.vert
rm NeuropixelsV1.bonsai NeuropixelsV1.bonsai.layout probe_image.frag quad.vert

rm -fr ./Bonsai.ONIX
