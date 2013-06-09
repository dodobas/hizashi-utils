import os


def is_writable(path):
    """
    Checks if a path exists and it's writeable by current user
    """
    if os.path.exists(path) and os.access(path, os.W_OK):
        return True
    else:
        return False


def is_hizashi_project():
    """
    Checks if current path is a Django Hizashi project
    """
    cur_dir = os.getcwd()
    hz_project_path = os.path.join(cur_dir, 'core', 'settings')

    return is_writable(hz_project_path)


def is_hizashi_root():
    """
    Checks if current path is a root of Django Hizashi project
    """
    cur_dir = os.getcwd()
    hz_project_path = os.path.join(cur_dir, 'django_project', 'core')

    return is_writable(hz_project_path)
