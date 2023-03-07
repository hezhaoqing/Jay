import os
import logging as log  # 引入logging模块
import shutil
import sys

log.basicConfig(level = log.INFO, format = '%(asctime)s, %(filename)s, %(levelname)s, %(message)s',
                datefmt = '%a, %d %b %Y %H:%M:%S',
                filename = os.path.join('./','exec.log'),
                filemode = 'a')
if len(sys.argv) == 1:
    log.error("请输入执行目录")
    raise Exception("请输入执行目录")

param = sys.argv[1]
params = param.split("-")

project_name = "-".join(params[:-1])
port = params[-1]

log.info("项目名称：" + project_name)
log.info("端口：" + port)

if not port.isdigit():
    log.error("端口号不是数字")
    raise Exception("端口号不是数字")


# 从执行脚本中获取目录
# 将目录下的jar copy到工程目录
# 从目录中拆解出工程名称和端口
# 复制模板文件
# 将复制的模板文件替换工程名
# 将复制的文件拷贝到工程目录config下
# 启动程序 指定jar 端口
project_dir = "/home/app01/"

jenkins_dir = os.path.join(project_dir, "jenkins")
jenkins_jar_dir = os.path.join(jenkins_dir, "jar")
jenkins_config_dir = os.path.join(jenkins_dir, "config")
bootstrap = "bootstrap.yaml"
logback = "logback.xml"

project_home_dir = os.path.join(project_dir, param)
project_config_dir = os.path.join(project_home_dir, "config")

if not os.path.exists(project_home_dir):
    os.makedirs(project_home_dir)
if not os.path.exists(project_config_dir):
    os.makedirs(project_config_dir)

resp = ""
jar = ""
# 拷贝jar包
for file in os.listdir(os.path.join(jenkins_jar_dir, param)):
    log.info("jar包：" + file)
    if "jar" in file:
        jar = file
if jar == "":
    log.error("jar包 不存在")
    raise Exception("jar包 不存在")

shutil.copyfile(os.path.join(jenkins_jar_dir, param, jar), os.path.join(project_home_dir, jar))

# 拷贝bootstrap.yaml
with open(os.path.join(jenkins_config_dir, bootstrap), "r") as fp:
    content = fp.read()
    resp = content.replace("$(project-name)", project_name)
    # log.info("配置文件信息：" + resp)
with open(os.path.join(project_config_dir, bootstrap), 'w') as fp2:
    fp2.write(resp)
# 拷贝logback
if not os.path.exists(os.path.join(project_config_dir, logback)):
    shutil.copyfile(os.path.join(jenkins_config_dir, logback), os.path.join(project_config_dir, logback))

# 启动脚本
ps_script = 'ps -ef|grep '+jar+'| grep ' + port + '|grep -v grep'

log.info(ps_script)
val = os.popen(ps_script).read()
log.info(val)
if len(val) > 0:
    for v in val.split("\n"):
        if not len(v) ==0:
            pid = list(filter(None, v.split(' ')))[1]
            log.info("进程PID:" + pid)
            os.popen('kill -9 ' + pid).read()
os.chdir(project_home_dir)
start_script = "nohup java  -javaagent:/home/app01/volcengine/apmplus-agent.jar -Dapmplus.agent.service_name="+param+" -Dapmplus.agent.service_type=http -jar " + jar + " --spring.config.location=config/bootstrap.yaml --server.port=" + port + " >/dev/null 2>&1 &"
log.info("执行启动脚本："+start_script)
os.popen(start_script)
