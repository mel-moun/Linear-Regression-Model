def ft_mean(args):
    """
        Calculates and returns the mean (average) of the given data.
    """
    return sum(args) / len(args)


def ft_var(args):
    """
        Calculates and returns the variance of the given data.
    """
    mean = ft_mean(args)
    return sum((x - mean) ** 2 for x in args) / len(args)


def ft_std(args):
    """
        Calculates and returns the standard deviation of the given data.
    """
    var = ft_var(args)
    return var ** 0.5
