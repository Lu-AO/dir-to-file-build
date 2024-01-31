封装
  将Compiler.py放入与目标文件夹同级的目录中，在这个目录打开命令行，输入python Compiler.py <目标文件夹> <目标文件夹内的主可执行文件> 按下Enter键，即可封装为一个后缀为.lexe的文件.
解包
  将Interpreter.py放入与生成的.lexe文件的同一个目录中，并且在这个目录打开命令行，输入python Interpreter.py <.lexe文件> 按下Enter键，即可解包为一个完整的目录.

或下载releases中的.exe文件，这样就不必须拥有Python环境了，也可以将.exe文件添加到系统环境变量Path中，这样就可以随时随地使用Compiler与Interpreter命令了.
