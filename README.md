####一个EayunOS Engine的管理工具，用户可以通过该工具方便、快捷的管理Engine系统。
=============
#####使用方法：

* Note：第一次登陆后需要对系统进行初始化配置，配置流程：1-->2-->3-->7(3)-->6，配置完成后浏览器访问"http://{Web Portal IP}/ovirt-engine/services/health"，返回"DB Up!Welcome to Health Status!"说明初始化成功。

* 登陆到控制台后首先看到的是系统的状态信息：

```
    Welcome to the EayunOS 4.1 Engine Appliance.
    
    To manage your appliance please browse to Web Portal.
    
    	Hostname:		    aa.bb.cc
    	IP Address:		    192.168.2.195
    	Netmask:		    255.255.252.0
    	Gateway:		    192.168.0.1
    	DNS:                8.8.8.8
    	MAC Address:	    00:1A:4A:81:E3:67
    	System Time:        2014年 10月 17日 星期五 13:30:33 CST
    	
    	Engine Version:		3.5.0.1
    	Engine State:		Running
    	Web Portal:		    http://192.168.2.195
    
    
    Press any key to continue.
```

* 按任意键可以进入配置页面

```
    Advanced Setting
    
    1) Network Configuration
    2) Test Network Configuration
    3) Set Hostname
    4) Set Date and Time
    5) Hosts File Configuration
    6) Engine Restart
    7) Engine Advance Setting
    8) System Restart or Shutdown
    9) Shell
    10) Summary Information
    11) Help
    12) Log OFF
    
    
    Choose the advanced setting: 
```

* 输入“1”，回车，配置系统的IP/Netmask/Gateway/DNS信息

```
    Network Configuration
    
    Enter the new network configuration settings.
    
    Enter the IP Address: |192.168.2.195| 
    Enter the Netmask: |255.255.252.0| 
    Enter the Gateway: |192.168.0.1| 
    Enter the DNS: |8.8.8.8| 
```

* 输入“2”，回车，可进行网络连通性测试（直接回车返回上级配置页面）

```
    Test Network Configuration
    
    Enter the hostname, ip address, or none to continue: 192.168.0.1
    192.168.0.1: Success!
    Enter the hostname, ip address, or none to continue:
```

* 输入“3”，回车，可修改主机名

```
    Please enter the hostname: aa.bb.cc
```

* 输入“4”，回车，可设置系统时间

```
    Date and Time Configuration
    
    Enter the current date (YYYY-MM-DD) or "c" to Cancel : 2014-10-17
    Enter the current time in 24 hour format (HH:MM:SS) or "c" to Cancel : 13:40:00

    Date and Time Configuration
    
    	Date :		2014-10-17
    	Time :		13:40:00
    
    Apply Date and Time configuration? (Y/N): Y
```

* 输入“5”，回车，可修改系统“/etc/hosts”文件

```
    127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
    ::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
    
    192.168.2.195 aa.bb.cc
```

* 输入“6”，回车，可重启“ovirt-engine”服务

```
    Engine Restart (Y/N): Y
```

* 输入“7”，回车，可重新配置“ovirt-engine”服务。输入“1”，回车，可清除engine的配置；输入“2”，回车，可配置engine；输入“3”，回车，可重新配置Web Portal admin用户密码；输入“4”，回车，可返回上级配置页面。

```
    Engine Advanced Configuration
    
    
    1) Engine Cleanup 
    2) Engine Setup 
    3) Reset Web Portal admin password 
    4) Back
    
    
    Choose the advanced setting:
```

* 输入“8”，回车，可重启或关闭系统

```
    Restart or Shutdown the System.
    
    1) Restart the System 
    2) Shutdown the System
    3) Back
    
    Choose the advanced setting: 
```

* 输入“9”，回车，可获得系统Shell

* 输入“10”，回车，可返回查看系统状态信息

* 输入“11”，回车，可查看帮助信息

* 输入“12”，回车，退出登陆


