from misaligned import calculate_color_code, print_color_map

# test_misaligned.py


def test_calculate_color_code_basic():
    assert calculate_color_code(0, 0) == 0
    assert calculate_color_code(1, 1) == 1
    assert calculate_color_code(2, 3) == 8
    assert calculate_color_code(3, 4) == 14
    assert calculate_color_code(4, 2) == 27
    assert calculate_color_code(5, 1) == 21

def test_calculate_color_code_edge_cases():
    assert calculate_color_code(0, 4) == 0
    assert calculate_color_code(4, 0) == 0

def test_print_color_map_no_args():
    assert print_color_map() == 25

def test_print_color_map_with_indices():
    assert print_color_map(1, 1) == calculate_color_code(1, 1)
    assert print_color_map(2, 3) == calculate_color_code(2, 3)
    assert print_color_map(4, 2) == calculate_color_code(4, 2)

def test_print_color_map_only_one_index():
    # Should return total count if one index is None
    assert print_color_map(major_index=1) == 5
    assert print_color_map(minor_index=2) == 10