#!/bin/bash

for iso in $(ls /var/local/lib/isolate/)
do
  isolate --cg -b $iso --cleanup
done
