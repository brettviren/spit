#!/bin/bash

# This variable is referred to in .yaml files.
export spit="$(dirname $(realpath "$BASH_SOURCE"))"
    
if [ ! -f "$spit/scope/repos.yaml" ] ; then
    cat <<EOF > "$spit/scope/repos.yaml"
repos:
  - $spit/scope/repo
  - \$spack/var/spack/repos/builtin
EOF
fi

spack () {
    PKG_CONFIG_PATH=/usr/share/pkgconfig:/usr/lib/x86_64-linux-gnu/pkgconfig "$spit/spack/bin/spack" -C "$spit/scope" $@
}




spack uninstall -ya spit || echo "Above error is okay"
spack   install     spit

spitview="$spit/view"
if [ -d "$spitview" ] ; then
    rm -rf "$spitview"
fi
spack view add -i "$spitview" spit 2>&1 | grep -v 'Warning:'
