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



view=$spit/view

spack view rm -a $view   || echo "it's okay"
spack uninstall -ya spit || echo "it's okay"
spack   install     spit
spack view add -i $view spit
