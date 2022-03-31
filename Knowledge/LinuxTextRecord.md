##### Date:	2022-3-31

##### Result:	4/5

##### KeyPoint:

- 符号连接文件判认 -- 正确
- 命令返回代码 -- 正确
- 搭建DHCP服务器，给客户机指定默认网关地址 -- 错误
- 查看当前Linux系统状态命令 -- 正确
- 死锁的必要条件 -- 正确

##### Parse：

```
# DHCP 配置文件 -- dhcpd.conf
option routers 192.168.0.1;			   	  # 配置默认网关
option subnet-mask 255.255.255.0;		   # 配置子网掩码
option domain-name-servers 192.168.1.1;	    # 指定DNS服务器
option domain-name-servers 			     # 配置多个DNS服务器

# Linux系统状态相关命令
top命令：# Linux下常用的性能分析工具。能够实时显示系统中各个进程对资源的占用状况。
free命令：# 可以显示Linux系统中空闲的、已用的物理内存及swap内存，及被内核使用的buffer。
df命令：# 用于显示当前在Linux系统上的文件系统的磁盘使用情况的统计信息。
cat /proc/meminfo # 可以查看内存更详细的情况

# 死锁必要条件四个
互斥条件，请求与保持条件，不剥夺条件，循环等待条件。
```

