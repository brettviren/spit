# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-sphinxext-opengraph
#
# You can edit this file again by typing:
#
#     spack edit py-sphinxext-opengraph
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PySphinxextOpengraph(PythonPackage):
    """Sphinx extension to generate OpenGraph metadata."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    pypi = "sphinxext-opengraph/sphinxext-opengraph-0.6.2.tar.gz"

    version('0.6.2', sha256='30d4dbe345da991c210626795c05918c3f9ad9f7d14d9c48812ccfa7a1ec4bab')

    depends_on('py-setuptools', type='build')
    depends_on('py-sphinx@1.8:')
