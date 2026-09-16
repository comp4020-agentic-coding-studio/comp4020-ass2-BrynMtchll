"""Percentile conversion without a scipy dependency."""

import numpy as np


def percentile_of(x):
    """Map values to their percentile rank in 0-100."""
    order = np.argsort(np.argsort(x))
    return 100.0 * order / (len(x) - 1)
