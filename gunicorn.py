# -*- coding: utf-8 -*-
import os
from multiprocessing import cpu_count
port = 9898
bind = f"0.0.0.0:{port}"
daemon = True
workers = cpu_count()  + 1
threads = 2
worker_class = "gevent"
forwarded_allow_ips = '*'
#keepalive = 6
#timeout = 65
#graceful_timeout = 10
worker_connections = 65535
loglevel = 'error'
reload = True
#spew = True
#日志级别，这个日志级别指的是错误日志的级别，而访问日志的级别无法设置
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%({X-Real-IP}i)s"'
accesslog = f"./logs/logs.log"      #访问日志文件
errorlog = "./logs/error.log"  # 错误日志文件


# -c CONFIG    : CONFIG,配置文件的路径，通过配置文件启动；生产环境使用；

# -b ADDRESS   : ADDRESS，ip加端口，绑定运行的主机；

# -w INT, --workers INT：用于处理工作进程的数量，为正整数，默认为1；

# -k STRTING, --worker-class STRTING：要使用的工作模式，默认为sync异步，可以下载eventlet和gevent并指定

# --threads INT：处理请求的工作线程数，使用指定数量的线程运行每个worker。为正整数，默认为1。

#-worker_class:
    #"  sync"：同步工作模式，这是默认的工作模式。每个请求都会在独立的进程中处理。

    # "gevent"：使用gevent库来实现协程和非阻塞IO，可以在单个进程中处理多个并发请求。这种工作模式适合IO密集型的应用。

    # "eventlet"：类似于gevent，也是使用协程和非阻塞IO来处理请求的工作模式。

    # "tornado"：使用Tornado库来处理请求，适合于高性能的异步IO应用。

    # "gthread"：使用线程来处理并发请求。

    #选择合适的worker_class取决于您的应用程序的性质和要求。如果您的应用程序是IO密集型的，例如涉及网络请求或数据库查询，
    # 那么选择类似"gevent"或"eventlet"的协程模型可能会更适合。如果您的应用程序需要高度的并行性和低延迟，可以考虑异步模型如"tornado"。
# --worker-connections INT：最大客户端并发数量，默认情况下这个值为1000。

# --backlog int：未决连接的最大数量，即等待服务的客户的数量。默认2048个，一般不修改；

# -p FILE, --pid FILE：设置pid文件的文件名，如果不设置将不会创建pid文件


# --access-logfile FILE   ：  要写入的访问日志目录

# --access-logformat STRING：要写入的访问日志格式

# --error-logfile FILE, --log-file FILE  ：  要写入错误日志的文件目录。

# --log-level LEVEL   ：   错误日志输出等级。
    # "debug"：最详细的日志级别，用于调试目的。会显示所有详细的调试信息，通常用于排查问题。

    # "info"：默认的日志级别。会显示有关请求处理和服务器运行状态的基本信息，适用于正常的运行状态。

    # "warning"：显示警告级别的日志信息，用于指示一些可能的问题。

    # "error"：显示错误级别的日志信息，用于指示出现了一些错误，但服务器仍然在运行。

    # "critical"：显示严重级别的日志信息，用于指示服务器遇到了严重问题，可能需要中断运行。


# --limit-request-line INT   ：  HTTP请求头的行数的最大大小，此参数用于限制HTTP请求行的允许大小，默认情况下，这个值为4094。值是0~8190的数字。

# --limit-request-fields INT   ：  限制HTTP请求中请求头字段的数量。此字段用于限制请求头字段的数量以防止DDOS攻击，默认情况下，这个值为100，这个值不能超过32768

# --limit-request-field-size INT  ：  限制HTTP请求中请求头的大小，默认情况下这个值为8190字节。值是一个整数或者0，当该值为0时，表示将对请求头大小不做限制


# -t INT, --timeout INT：超过这么多秒后工作将被杀掉，并重新启动。一般设定为30秒；

# --daemon： 是否以守护进程启动，默认false；

# --chdir： 在加载应用程序之前切换目录；

# --graceful-timeout INT：默认情况下，这个值为30，在超时(从接收到重启信号开始)之后仍然活着的工作将被强行杀死；一般使用默认；

# --keep-alive INT：在keep-alive连接上等待请求的秒数，默认情况下值为2。一般设定在1~5秒之间。

# --reload：默认为False。此设置用于开发，每当应用程序发生更改时，都会导致工作重新启动。

# --spew：打印服务器执行过的每一条语句，默认False。此选择为原子性的，即要么全部打印，要么全部不打印；

# --check-config   ：显示现在的配置，默认值为False，即显示。

# -e ENV, --env ENV： 设置环境变量；
