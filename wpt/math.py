from __future__ import print_function
import numpy as np
from copy import deepcopy
from scipy.stats import rankdata
from enum import Enum


def min_rank_changes(vec1, vec2, min_change=1)->int:
    """
    Ranks vec1 and vec2 and calculates the number of places where the
    rank differs by at least min_change.
    :param vec1: THe first vector, anything that can have scip.stats.rankdata() applied to it.
    :param vec2: The other vector
    :param min_change: The minimum rank change to look for
    :return:
    """
    rk1 = rankdata(vec1)
    rk2 = rankdata(vec2)
    diff = np.abs(rk1-rk2)
    count = 0
    for val in diff:
        if val >= min_change:
            count += 1
    return count


def taxi_dist(r1, r2):
    """
    Calculates the basic taxi-cab metric distance between 2 vectors
    :param r1:
    :param r2:
    :return:
    """
    diff = np.subtract(r1, r2)
    rval = np.sum(np.abs(diff))
    return rval


def count_diffs_dist(r1, r2, return_percent=False, min_dist=1):
    """
    Counts the number of entries in r1 that differ from r2 by at least min_dist
    :param r1: The first vector
    :param r2: The second vector
    :param return_percent: Should we return the count, or the percent of positions where the differences occured
    :param min_dist: The minimum distance between r1[i] and r2[i] for i to be counted as a differing location.
    This min_dist is a >=, so if the distance between r1 and r2 at i is min_dist, it counts
    :return: Either the percentage of locations with a diff, or the count
    """
    count = 0
    for v1, v2 in zip(r1, r2):
        if np.abs(v1 - v2) >= min_dist:
            count += 1
    if return_percent:
        return count / len(r1)
    else:
        return count


def total_vec_diff(orig_wts, new_wts, return_percent=True, totaler=np.mean):
    """
    Calculates the difference between 2 vectors, where the first one is the original/known value
    and the 2nd is the new value/unknown/changed.  If we do_percent, then we calculate percent change
    from orig_wts to new_wts.  Otherwise it is just pure distance.
    :param orig_wts: The original/known values vector
    :param new_wts: The new/unknown/changed values vector
    :param return_percent: If true we do a percent change calculation, otherwise it is the raw diff
    :param totaler: For each entry we get a difference (either abs(diff) or percent_change) and we need to
    total those values.  We defeault to using the numpy.mean() function, but any other function could work here.
    :return: The calculated difference
    """
    diff = np.abs(np.subtract(orig_wts, new_wts))
    if return_percent:
        for i in range(len(diff)):
            if orig_wts[i] != 0:
                diff[i] = diff[i] / np.abs(orig_wts[i])
    rval = totaler(diff)
    return rval


def family_wts(t, w0, pos):
    """
    Changes the importance of the weight in w0 in position pos in the following fashion:
    when t=0 it is w0[pos], i.e. the initial value
    when t=1 its value is 1, i.e. the most important
    In between it scales linearly.
    And the remainder of values are scaled so that the total adds to one
    """
    rval = deepcopy(w0)
    prev_sum = sum(w0)
    rval[pos] = (1 - t) * w0[pos] + t * 1
    rest_sum = prev_sum - w0[pos]
    new_sum = 1 - rval[pos]
    factor = new_sum / rest_sum
    for i in range(len(w0)):
        if i != pos:
            rval[i] *= factor
    return rval









def firstTime(A, w0, f, d, gamma,
              step=0.001, wt_combine_loc=None,
              wt_changes_percent=True, wt_changes_totaler=np.mean,
              return_param_only=True):
    '''The actual algorithm to find the first time a ranking changes due to a parameter change'''
    score0 = np.array(np.matmul(A, w0).tolist())
    rank0 = rankdata(-score0)
    t = 0 + step
    while t <= 1:
        w = f(t)
        score = np.array(np.matmul(A, w).tolist())
        rank = rankdata(-score)
        dist = d(rank0, rank)
        if dist >= gamma:
            weight_changes_total = total_vec_diff(w0, w, return_percent=wt_changes_percent, totaler=wt_changes_totaler)
            weight_changes_local = total_vec_diff(w0[wt_combine_loc:(wt_combine_loc + 1)],
                                                w[wt_combine_loc:(wt_combine_loc + 1)],
                                                  return_percent=wt_changes_percent, totaler=wt_changes_totaler)
            if return_param_only:
                return t
            else:
                return {
                    "param": t,
                    "weight_changes_total": weight_changes_total,
                    "weight_changes_local": weight_changes_local,
                    "weights": w,
                    "scores": score,
                    "ranks": rank
                }
        t += step
    return None
