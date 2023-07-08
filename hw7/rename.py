import os


def rename_file(new_name: str, extention: str):
    direct = [i.name for i in list(os.scandir()) if i.is_file()]
    k = 1
    for i in direct:
        file_name = i.rsplit(".")[0]
        file_extention = i.rsplit(".")[1]
        if file_extention == extention:
            os.rename(
                i, f'{file_name}_{new_name}_{k}.{file_extention}')
            k += 1


rename_file("ogo", "txt")
