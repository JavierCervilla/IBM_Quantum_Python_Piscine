# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: javier <javier@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 03:50:29 by javier            #+#    #+#              #
#    Updated: 2023/03/15 03:58:09 by javier           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:
    """A class representing a GOT Character."""
    def __init__(self, first_name=None, is_alive = True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is coming"
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False