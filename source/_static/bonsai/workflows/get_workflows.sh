#!/bin/bash
git clone --depth 1 git@github.com:jonnew/Bonsai.ONIX.git
find ./Bonsai.ONIX/ExampleWorkflows -mindepth 2 -type f -exec mv -t ./ -f '{}' +
