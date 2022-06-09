import os

class Sistema:
    def reduzir_ifs(**kwargs) -> bool:
        qtd_err = 0
        for key,value in kwargs.items():
            if value == None:
                print(key)
                qtd_err+=1
        if qtd_err == 0:
            return True
        else:
            return False

    def Delete_Image(path) -> None:
        if os.path.exists(path):
            try:
                os.unlink(path)
            except OSError as e:
                print(f"Error:{ e.strerror}")
