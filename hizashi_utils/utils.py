import os
import sys

HIZASHI_ID = '.hizashi_project'


class CHDir:
    """
    Context manager for directory change operation
    """
    def __init__(self, newPath):
        self.newPath = newPath

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


def is_writable(path):
    """
    Checks if a path exists and it's writeable by current user
    """
    if os.path.exists(path) and os.access(path, os.W_OK):
        return True
    else:
        print(
            'Path "{0}" is not writeable by the current user or it doesn\'t '
            'exist.'.format(path))
        # terminate
        sys.exit(1)


def is_file(path):
    """
    Checks if a path exists and it's a file
    """
    if os.path.exists(path) and os.path.isfile(path):
        return True
    else:
        return False


def get_hizashi_project():
    """
    Returns root path of a Django Hizashi project
    """
    root_path = get_hizashi_root()
    if root_path:
        project_path = os.path.join(root_path, 'django_project')
        return project_path if is_writable(project_path) else None
    else:
        print(
            'Path "{0}" is not a subdirectory of a Django Hizashi project.\n'
            'Please change your current working directory to a Django '
            'Hizashi project folder.'.format(os.getcwd())
        )
        # terminate
        sys.exit(1)


def get_hizashi_root():
    """
    Searches for Django Hizashi project root

    returns 'path'
    """
    cur_dir = os.getcwd()
    while cur_dir != '/':
        if is_file(os.path.join(cur_dir, HIZASHI_ID)):
            return cur_dir
        else:
            # go back one folder
            cur_dir = os.path.normpath(os.path.join(cur_dir, '..'))
    else:
        return None
