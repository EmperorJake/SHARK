#!/bin/bash
  ./src/build_fish.py \
  && nmlc fish.nml \
  && mv fish.grf ~/Documents/OpenTTD/data

