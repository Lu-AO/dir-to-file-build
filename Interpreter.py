import sys,os
def main(argv):
    if len(argv) > 1:
        path = argv[1]
        with open(path,"rb") as file:
            infile = False
            linen=0
            for line in file:
                linen+=1
                if "The main dir is".encode("utf-8") in line:
                    main_dir = line[16:-2]
                    print(f"主目录:{main_dir.decode('utf-8')}")
                elif "The main file is".encode("utf-8") in line:
                    main_file = line[17:-2]
                    print(f"主文件:{main_file.decode('utf-8')}")
                elif (line==b'\n' or line==b'\r\n' or line==b"~\n") and not infile:
                    pass
                elif line!=b'luaoluao{\n' and line!=b'}luaoluao\n' and not infile:
                    name = line.decode("utf-8")[:-2]
                    index = name.rfind("/")
                    dir_name = name[:index]
                    if not os.path.exists(dir_name):
                        os.makedirs(dir_name)
                        print("还原目标文件所在目录")
                    with open(f"{name}","w") as a:
                        a.write("")
                    print(f"读取名称,写入空值",name)
                elif line==b'luaoluao{\n' and not infile:
                    scr = open(f"{name}","ab")
                    infile=True
                    print("建立文件")
                elif (line==b'}luaoluao' or line==b"}luaoluao\n") and infile:
                    scr.close()
                    infile=False
                    print(f"写入{name}完毕")
                elif infile:
                    scr.write(line)
        return [main_dir, main_file]
    else:
        print("Interpreter --virsion 1.0.0")
if __name__=='__main__':
    main(sys.argv)