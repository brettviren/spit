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
#     spack install py-sphinx-inline-tabs
#
# You can edit this file again by typing:
#
#     spack edit py-sphinx-inline-tabs
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PySphinxInlineTabs(PythonPackage):
    """A sphinx extension giving inline tabs."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    pypi = "sphinx-inline-tabs/sphinx_inline_tabs-2022.1.2b11.tar.gz"

    version('2022.1.2b11', sha256='afb9142772ec05ccb07f05d8181b518188fc55631b26ee803c694e812b3fdd73')

    depends_on('py-setuptools', type='build')
    depends_on('py-flit-core')
    depends_on('py-sphinx@1.8:')

    
