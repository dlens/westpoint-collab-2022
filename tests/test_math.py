from numpy import testing as npt
import wpt.math as wptm


def test_min_rank_changes():
    v1 = [1, 2, 3]
    v2 = [2, 1, 3]
    npt.assert_equal(2, wptm.min_rank_changes(v1, v2))
    npt.assert_equal(0, wptm.min_rank_changes(v1, v2, min_change=2))


def test_taxi_dist():
    v1 = [1, 2, 3]
    v2 = [2, 1, 3]
    npt.assert_equal(2, wptm.taxi_dist(v1, v2))


def test_count_diffs_dist():
    v1 = [1, 2, 3]
    v2 = [2, 1, 3]
    npt.assert_equal(2, wptm.count_diffs_dist(v1, v2))
    npt.assert_equal(2, wptm.count_diffs_dist(v2, v1))
    npt.assert_equal(2 / 3, wptm.count_diffs_dist(v2, v1, return_percent=True))
    npt.assert_equal(0, wptm.count_diffs_dist(v1, v2, min_dist=1.1))


def test_total_vec_diff():
    v1 = [0.5, 0.2, 0.3]
    v2 = [0.3, 0.2, 0.5]
    npt.assert_almost_equal((0.2 + 0.2) / 3, wptm.total_vec_diff(v1, v2, return_percent=False))
    npt.assert_almost_equal((0.2 / 0.5 + 0.2 / 0.3) / 3, wptm.total_vec_diff(v1, v2))


def test_family_wts():
    w0 = [0.5, 0.3, 0.2]
    w1 = wptm.family_wts(0, w0, 0)
    npt.assert_array_almost_equal(w0, w1)
    w1 = wptm.family_wts(1, w0, 0)
    npt.assert_array_almost_equal([1, 0, 0], w1)
    w1 = wptm.family_wts(0.5, w0, 0)
    npt.assert_array_almost_equal([0.75, 0.15, 0.10], w1)
