
os.getcwd()：获得当前工作目录
os.curdir:返回当前目录（'.')
os.chdir(dirname):改变工作目录到dirname

os.path.isdir(name):判断name是不是一个目录，name不是目录就返回false
os.path.isfile(name):判断name是不是一个文件，不存在name也返回false
os.path.exists(name):判断是否存在文件或目录name

os.path.getsize(name):获得文件大小，如果name是目录返回0
os.path.abspath(name):获得绝对路径

os.path.split(name):列表形式分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
os.path.splitext():列表形式分离文件名与扩展名 （同样不会判断文件是否存在）
os.path.join(path,name):连接目录与文件名或目录
os.path.basename(path):返回文件名
os.path.dirname(path):返回文件路径

os.remove(dir) #dir为要删除的文件路径
os.rmdir(path) #path要删除的目录的路径。需要说明的是，使用os.rmdir删除的目录必须为空目录，否则函数出错。

os.path.getmtime(name) ＃获取文件的修改时间
os.stat(path).st_mtime ＃获取文件的修改时间
os.stat(path).st_ctime #获取文件的创建时间
os.path.getctime(name) #获取文件的创建时间

os.walk(dir)               ### 遍历dir下的所有子目录以及文件，返回多个3元素的元组。格式：（本目录，子目录，文件）（子目录1，孙目录，文件）......
                               子目录、文件 为列表，没有则为[]，
                               os.listdir()的区别是只返回当前一层的所有目录和文件
os.listdir(dirname)        ### 列出dirname下的目录和文件                          
                               目录要加引号，Windows路径的\需要转义。
  
os.system()      ### 执行系统命令,如果有变量存储该执行的结果,该变量只会存储该命令执行成功或者失败返回值,不会存储命令执行的结果
                     需要保存命令执行的结果需使用os.popen("系统命令").read(),然后使用变量赋值输出即可
os.popen()       ### 执行系统命令，用.read()取得命令执行结果。
