#!/bin/bash

spit="$(dirname "$BASE_SOURCE")"
    
spack () {
    PKG_CONFIG_PATH=/usr/share/pkgconfig:/usr/lib/x86_64-linux-gnu/pkgconfig "$spit/spack/bin/spack" -C "$spit/scope" $@
}

view=$spidir/view

spack view rm -a $view
spack uninstall -ya spit
spack   install     spit
spack view add -i $view spit
