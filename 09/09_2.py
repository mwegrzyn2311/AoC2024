from utils.file_loader import load

class StoragePart:
    file_id: int
    file_len: int
    is_free: bool

    def __init__(self, file_id: int, file_len: int, is_free: bool):
        self.file_id = file_id
        self.file_len = file_len
        self.is_free = is_free

    def override(self, other):
        self.file_id = other.file_id
        self.file_len = other.file_len
        self.is_free = other.is_free

    def __str__(self):
        return ('.' if self.is_free else f'{self.file_id},') * self.file_len

    def __repr__(self):
        return self.__str__()


class Drive:
    storage_parts: list[StoragePart]

    def __init__(self, drive_str: str):
        self.storage_parts = [StoragePart(0, int(drive_str[0]), False)]
        i = 1
        file_id = 1
        while i < len(drive_str):
            free_space: int = int(drive_str[i])
            if free_space > 0:
                self.storage_parts.append(StoragePart(0, free_space, True))
            i += 1
            self.storage_parts.append(StoragePart(file_id, int(drive_str[i]), False))
            i += 1
            file_id += 1

    def reorganize(self):
        i = len(self.storage_parts) - 1
        while i >= 0:
            curr_file = self.storage_parts[i]
            if curr_file.is_free:
                i -= 1
                continue
            j = 1
            while j < i:
                curr_part: StoragePart = self.storage_parts[j]
                if curr_part.is_free:
                    free_remaining: int = curr_part.file_len - curr_file.file_len
                    if free_remaining >= 0:
                        curr_part.override(curr_file)
                        curr_file.file_id = 0
                        curr_file.is_free = True
                        # Merge free spaces
                        left_free: bool = i - 1 >= 0 and self.storage_parts[i - 1].is_free
                        right_free: bool = i + 1 < len(self.storage_parts) and self.storage_parts[i + 1].is_free
                        total_space: int = curr_file.file_len + (self.storage_parts[i - 1].file_len if left_free else 0) + (self.storage_parts[i + 1].file_len if right_free else 0)
                        if right_free:
                            self.storage_parts.pop(i + 1)
                        if left_free:
                            self.storage_parts.pop(i)
                            i -= 1
                        self.storage_parts[i].file_len = total_space
                        # Create empty space if not whole was occupied
                        if free_remaining > 0:
                            self.storage_parts.insert(j + 1, StoragePart(0, free_remaining, True))
                            i += 1
                        break
                j += 1
            i -= 1

    def checksum(self):
        position: int = 0
        checksum: int = 0
        for part in self.storage_parts:
            if not part.is_free:
                checksum += val_based_on_position_and_id(position, part.file_id, part.file_len)
            position += part.file_len
        return checksum

    def __str__(self):
        return "|".join([part.__str__() for part in self.storage_parts])

    def __repr__(self):
        return self.__str__()

def main():
    solution(load('09.txt'))

def solution(lines: list[str]):
    drive: Drive = Drive(lines[0].strip('\n'))
    #print(drive)
    drive.reorganize()
    #print(drive)
    print(drive.checksum())

def val_based_on_position_and_id(position: int, file_id: int, file_len: int) -> int:
    # a1 + a2 + a3 + ... + an = ((a1 + an) * n) / 2 = [with r=1] = ((2a1 + n - 1) * n) / 2
    return file_id * ((2 * position + file_len - 1) * file_len) // 2


main()