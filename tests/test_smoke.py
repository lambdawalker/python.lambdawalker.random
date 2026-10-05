def test_smoke():
    from lambdawalker.random.selection.select_random_file import select_random_file
    assert select_random_file is not None
    print("random OK")
