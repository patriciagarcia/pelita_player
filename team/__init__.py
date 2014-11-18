#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pelita.player import SimpleTeam
from .hungry_player import HungryPlayer
from .braindead_player import BraindeadPlayer
# (please use relative imports inside your module)

# The default factory method, which this module must export.
# It must return an instance of `SimpleTeam`  containing
# the name of the team and the respective instances for
# the first and second player.

def factory():
    return SimpleTeam("Brain deads", BraindeadPlayer(), BraindeadPlayer())

# For testing purposes, one may use alternate factory methods::
#
#     def alternate_factory():
#          return SimpleTeam("Our alternate Team", AlternatePlayer(), AlternatePlayer())
#
# To be used as follows::
#
#     $ ./pelitagame path_to/groupN/:alternate_factory

