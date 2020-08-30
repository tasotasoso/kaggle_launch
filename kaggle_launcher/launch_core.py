# -*- coding: utf-8 -*-
"""Core functions.
"""

from .auth import *
from .create_project import *
from .input import *





def launch():
    """launch your project.

    This function execute flow to launch project.

    --------

    Args: 
         None

    Returns:
         None

    """
    api = authenticate()
    competitions = show_and_get_competitions_list(api)
    choice = input_competition_number()
    competition_number = valid_choice(choice, len(competitions))
    ref = getattr(competitions[competition_number], "ref")

    create_project(ref)


if __name__ == "__main__":
    launch()
