# -*- coding: UTF-8 -*-
import os,sys
def compiler(path, main_exe, file, mod):
    if os.path.isfile(f"{path}/{file}"):
        print(f"编译{file}")
        with open(f'{path}/{file}', 'rb') as rfile:
            content = rfile.read()
        with open(f'{main_exe}_compile.lexe', f'{mod}') as wfile:
            if mod =="wb":
                wfile.write(f"The main file is {main_exe}.\nThe main dir is {path}.".encode("utf-8"))
            wfile.write(f'\n\n{path}/{file}:\n{"luaoluao{"}\n'.encode("utf-8"))
            wfile.write(content)
            wfile.write(f'\n{"}luaoluao"}\n'.encode("utf-8"))
    else:
        main(f"{path}/{file}", main_exe)
def main(path,main_exe,pdirs=''):
    if pdirs=="":
        pdirs = os.listdir(path)
    for file in pdirs:
        compiler(path,main_exe, file,"ab")
def Compile(argv):
    if len(argv) > 1:
        global dirs
        path = argv[1]
        main_exe = argv[2]
        # 输出所有文件和文件夹
        dirs = os.listdir(path)
        ##率先编译主文件
        compiler(path, main_exe, main_exe,"wb")
        dirs.remove(main_exe)
        main(path, main_exe,dirs)
    else:
        print("Compiler --virsion 1.0.0")
if __name__=="__main__":
    Compile(sys.argv)