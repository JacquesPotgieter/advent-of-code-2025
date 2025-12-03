from lock_position import LockPosition

def test_01():
    lock_position = LockPosition()

    assert lock_position.position == 50
    assert lock_position.password_count == 0

    lock_position.increase(50)

    assert lock_position.position == 0
    assert lock_position.password_count == 1

    print("Test 01 - Success")

def test_02():
    lock_position = LockPosition()

    assert lock_position.position == 50
    assert lock_position.password_count == 0

    lock_position.increase(100)

    assert lock_position.position == 50
    assert lock_position.password_count == 1

    print("Test 02 - Success")


def test_03():
    lock_position = LockPosition()

    assert lock_position.position == 50
    assert lock_position.password_count == 0

    lock_position.increase(200)

    assert lock_position.position == 50
    assert lock_position.password_count == 2

    print("Test 03 - Success")


def test_04():
    lock_position = LockPosition()

    assert lock_position.position == 50
    assert lock_position.password_count == 0

    lock_position.decrease(50)

    assert lock_position.position == 0
    assert lock_position.password_count == 1

    print("Test 04 - Success")

def test_05():
    lock_position = LockPosition()

    assert lock_position.position == 50
    assert lock_position.password_count == 0

    lock_position.decrease(100)

    assert lock_position.position == 50
    assert lock_position.password_count == 1

    print("Test 05 - Success")

def test_06():
    lock_position = LockPosition()

    assert lock_position.position == 50
    assert lock_position.password_count == 0

    lock_position.decrease(200)

    assert lock_position.position == 50
    assert lock_position.password_count == 2

    print("Test 06 - Success")

def test_07():
    lock_position = LockPosition()

    assert lock_position.position == 50
    assert lock_position.password_count == 0

    lock_position.decrease(50)

    assert lock_position.position == 0
    assert lock_position.password_count == 1

    lock_position.increase(100)

    assert lock_position.position == 0
    assert lock_position.password_count == 2

    print("Test 07 - Success")

def test_08():
    lock_position = LockPosition()

    assert lock_position.position == 50
    assert lock_position.password_count == 0

    lock_position.decrease(50)

    assert lock_position.position == 0
    assert lock_position.password_count == 1

    lock_position.increase(100)

    assert lock_position.position == 0
    assert lock_position.password_count == 2

    print("Test 08 - Success")

def test_example():
    lock_position = LockPosition()
    print(lock_position.to_string())
    assert lock_position.position == 50
    assert lock_position.password_count == 0

    lock_position.decrease(68)
    print(lock_position.to_string())
    assert lock_position.position == 82
    assert lock_position.password_count == 1

    lock_position.decrease(30)
    print(lock_position.to_string())
    assert lock_position.position == 52
    assert lock_position.password_count == 1

    lock_position.increase(48)
    print(lock_position.to_string())
    assert lock_position.position == 0
    assert lock_position.password_count == 2

    lock_position.decrease(5)
    print(lock_position.to_string())
    assert lock_position.position == 95
    assert lock_position.password_count == 2

    lock_position.increase(60)
    print(lock_position.to_string())
    assert lock_position.position == 55
    assert lock_position.password_count == 3

    lock_position.decrease(55)
    print(lock_position.to_string())
    assert lock_position.position == 0
    assert lock_position.password_count == 4

    lock_position.decrease(1)
    print(lock_position.to_string())
    assert lock_position.position == 99
    assert lock_position.password_count == 4

    lock_position.decrease(99)
    print(lock_position.to_string())
    assert lock_position.position == 0
    assert lock_position.password_count == 5

    lock_position.increase(14)
    print(lock_position.to_string())
    assert lock_position.position == 14
    assert lock_position.password_count == 5

    lock_position.decrease(82)
    print(lock_position.to_string())
    assert lock_position.position == 32
    assert lock_position.password_count == 6


    print("Test Example - Success")

test_01()
test_02()
test_03()
test_04()
test_05()
test_06()
test_07()

test_example()