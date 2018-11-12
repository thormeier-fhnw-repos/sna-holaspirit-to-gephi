def error(msg):
    """
    Prints an error message and quits with exit code 1
    :param msg: The error message
    """
    print("ERROR:", msg)
    sys.exit(1)
