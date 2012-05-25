#!/usr/bin/python

import os, errno
from distutils.core import setup
from distutils import sysconfig, cmd
from distutils.util import change_root
from distutils.dir_util import remove_tree, copy_tree, mkpath


if __name__=='__main__':
    setup(name="ldaptor",
          version="0.0.2",
          description="Pure-Python library for LDAP",
          long_description="""

Ldaptor is a pure-Python library that implements

- LDAP client logic.

- separately-accessible LDAP and BER protocol message
generation/parsing.

- ASCII-format LDAP filter generation and parsing.

- LDIF format data generation.

- Samba password changing logic.

Also included is a web-based user interface to search and edit
information in an LDAP directory and a set of LDAP utilities for use
from the command line.

""".strip(),
          author="Tommi Virtanen",
          author_email="tv@debian.org",
          license="GNU LGPL",
          packages=[
              "ldaptor",
              "ldaptor.protocols",
              "ldaptor.protocols.ldap",
              "ldaptor.protocols.ldap.autofill",
              "ldaptor.samba",
              "ldaptor.test",
          ])
