# Base images
FROM centos

# ADD使用这个命令拷贝文件或目录（压缩包会自动解压）；必须把文件拷贝到Dockerfile同目录下
ADD pcre-8.39.tar.gz /usr/local/src
ADD nginx-1.10.1.tar.gz /usr/local/src

# RUN
RUN yum install -y wget gcc gcc-c++ makeopenssl-devel
RUN useradd -s /sbin/nologin -M www

# WORKDIR --相当于cd，切换到目录
WORKDIR /usr/local/src/nginx-1.10.1
RUN ./configure--prefix=/usr/local/nginx-1.10 --user=www --group=www --with-http_ssl_module--with-http_stb_module --with-pcre=/usr/local/pcre-8.39http_stb_module--with-pcre=/usr/local/pcre-8.39 && make && make install
RUN echo "daemon off;" >>/usr/local/nginx-1.10/conf/nginx.conf


ENV PATH /usr/local/nginx-1.10/sbin:$PATH 

# 对外开放80端口
EXPOSE 80

 

# 容器启动时自动执行“nginx”命令
CMD ["nginx"]
