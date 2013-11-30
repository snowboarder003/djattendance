""" BADGES util.py 

Utility functions for badges module
"""

def construct_upload_path(badge_type):
    path = ""
    if badge_type == 'T':
        path += "trainees/" + Term.current_term().code + '/'
    elif badge_type == 'S':
        path += "staff/"
    else:
        return path