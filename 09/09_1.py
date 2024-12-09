from utils.file_loader import load

def main():
    solution(load('09.txt'))


def solution(lines: list[str]):
    drive: str = lines[0].strip('\n')
    print(calc_checksum(drive))

def calc_checksum(drive: str):
    left: int = 0
    left_id: int = 0
    position: int = 0
    right: int = len(drive) - 1
    right_id = right // 2
    remaining_right_len: int = int(drive[right])
    checksum: int = 0
    while left < right:
        # Checksum for file at left index
        file_len = int(drive[left])
        checksum += val_based_on_position_and_id(position, left_id, file_len)
        position += file_len
        left += 1
        left_id += 1
        # Checksum for file being moved from right
        empty_len: int = int(drive[left])
        while empty_len > 0:
            if remaining_right_len > empty_len:
                checksum += val_based_on_position_and_id(position, right_id, empty_len)
                remaining_right_len -= empty_len
                position += empty_len
                empty_len = 0
            else:
                checksum += val_based_on_position_and_id(position, right_id, remaining_right_len)
                empty_len -= remaining_right_len
                position += remaining_right_len
                right -= 2
                right_id -= 1
                remaining_right_len = int(drive[right])
                if left > right:
                    return checksum
        left += 1
    if remaining_right_len > 0:
        checksum += val_based_on_position_and_id(position, right_id, remaining_right_len)
    return checksum

def val_based_on_position_and_id(position: int, file_id: int, file_len: int) -> int:
    # a1 + a2 + a3 + ... + an = ((a1 + an) * n) / 2 = [with r=1] = ((2a1 + n - 1) * n) / 2
    return file_id * ((2 * position + file_len - 1) * file_len) // 2

main()