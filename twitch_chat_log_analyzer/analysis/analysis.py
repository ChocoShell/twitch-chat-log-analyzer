import pandas as pd
from pybursts import pybursts


def kleinburg_gauntlet(offsets):
    """Running Kleinburg burst detection

    Args:
        offsets (list): list of offset in seconds
    """
    possible_s = [1.5, 2, 3]
    possible_gamma = [0.5, 1, 2, 3]
    for s in possible_s:
        for gamma in possible_gamma:
            pd.DataFrame(pybursts.kleinberg(offsets, s=s, gamma=gamma)).to_csv(
                f"{s}{gamma}.csv", index=False
            )
