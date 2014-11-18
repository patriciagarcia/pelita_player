# -*- coding: utf-8 -*-

# (Specifying utf-8 is always a good idea in Python 2.)

from pelita.player import AbstractPlayer
from pelita.datamodel import stop
from pelita.graph import AdjacencyList, NoPathException, diff_pos

# use relative imports for things inside your module
from .utils import utility_function

class HungryPlayer(AbstractPlayer):
    """ Basically a clone of the FoodEatingPlayer. """

    def __init__(self):
        # Do some basic initialisation here. You may also accept additional
        # parameters which you can specify in your factory.
        # Note that any other game variables have not been set yet. So there is
        # no ``self.current_uni`` or ``self.current_state``
        pass

    def set_initial(self):
        # Now ``self.current_uni`` and ``self.current_state`` are known.
        # ``set_initial`` is always called before ``get_move``, so we can do some
        # additional initialisation here

        # Initialize an AdjacencyList for all reachable positions
        # This will help us find shortest paths
        # see in graph.py for more details
        self.adjacency = AdjacencyList(self.current_uni.reachable([self.initial_pos]))

        # Once we have picked a food item to go to, we’ll note it here
        # Otherwise we risk flapping between two states
        self.next_food = None

    def path_to(self, pos):
        """ Given a position, this return a shortest path from the current position. """
        return self.adjacency.a_star(self.current_pos, pos)

    def get_move(self):
        # check, if food is still present, otherwise go somewhere else

        if (self.next_food is None
                or self.next_food not in self.enemy_food):
            if not self.enemy_food:
                # all food has been eaten? ok. i’ll stop
                self.say("I am hungry.")
                return stop

            # all the food is in self.enemy_food
            # we just pick one to go to
            # (of course, there may be a smarter choice than just going random)

            self.next_food = self.rnd.choice(self.enemy_food)

        try:
            # figure out the path to take
            shortest_path = self.path_to(self.next_food)

            # our next position is the last element in the path
            next_pos = shortest_path[-1]

            # we are a little exited about eating
            # (this does not account for any food we additionally eat on our way
            # to the food we have picked.)
            if len(shortest_path) == 1:
                self.say("Yay. Food next.")
            else:
                self.say("Eating in {0} steps.".format(len(shortest_path)))

            # should we check for the enemy at this position?
            # self.enemy_bots ?
            # Naah – we risk it :)

            # the difference between here and there
            # is the direction we need to go to
            move = diff_pos(self.current_pos, next_pos)
            return move
        except NoPathException:
            # whoops, there is no path possible
            # we better wait
            return stop


