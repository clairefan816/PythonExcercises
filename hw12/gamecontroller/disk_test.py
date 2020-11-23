from disk import Disk

disk_a = Disk(0, 0, 100, 100, 0, 0, 1)
disk_b = Disk(0, 0, 100, 200, 0, 0, 2)


def test_constructor():
    assert (disk_a.x, disk_a.y) == (0, 0)
    assert (disk_a.target_x, disk_a.target_y) == (100, 100)
    assert (disk_b.x, disk_b.y) == (0, 0)
    assert (disk_b.target_x, disk_b.target_y) == (100, 200)
    assert (disk_a.count) == 1
    assert (disk_b.count) == 2


def test_disk_flying():
    disk_a.intact = False
    disk_a.disk_flying()
    assert disk_a.y == 10
    disk_b.intact = True
    assert disk_b.y == 0


def test_arrived():
    disk_a.x = 100
    disk_a.y = 100
    assert disk_a.arrived() is True
    disk_b.x = 100
    disk_b.y = 100
    assert disk_b.arrived() is False
