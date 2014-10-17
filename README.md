###一个EayunOS Engine的管理工具，用户可以通过该工具方便、快捷的管理Engine系统。
=============
#####使用方法：

######登陆到控制台后首先看到的是系统的状态信息：

    Welcome to the EayunOS 4.1 Engine Appliance.
    
    To manage your appliance please browse to Web Portal.
    
    	Hostname:		    engine.test.eayun
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

######按任意键可以进入配置页面

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
    11) Log OFF
    
    
    Choose the advanced setting: 

######（1）输入“1”，回车，配置系统的IP/Netmask/Gateway/DNS信息

    Network Configuration
    
    Enter the new network configuration settings.
    
    Enter the IP Address: |192.168.2.195| 
    Enter the Netmask: |255.255.252.0| 
    Enter the Gateway: |192.168.0.1| 
    Enter the DNS: |8.8.8.8| 

######（2）输入“2”，回车，可进行网络连通性测试（直接回车返回上级配置页面）

    Test Network Configuration
    
    Enter the hostname, ip address, or none to continue: 192.168.0.1
    192.168.0.1: Success!
    Enter the hostname, ip address, or none to continue:

######（3）输入“3”，回车，可修改主机名

    Please enter the hostname: engine.test.eayun

######（4）输入“4”，回车，可设置系统时间

    Date and Time Configuration
    
    Enter the current date (YYYY-MM-DD) or "c" to Cancel : 2014-10-17
    Enter the current time in 24 hour format (HH:MM:SS) or "c" to Cancel : 13:40:00
    
    Date and Time Configuration
    
    	Date :		2014-10-17
    	Time :		13:40:00
    
    Apply Date and Time configuration? (Y/N): Y

######（5）输入“5”，回车，可修改系统“/etc/hosts”文件

    127.0.0.1       localhost.localdomain
    192.168.3.251   storage.test.eayun
    192.168.2.44    node1.test.eayun
    192.168.2.195 engine.test.eayun

######（6）输入“6”，回车，可重启“ovirt-engine”服务

    Engine Restart (Y/N): Y

######（7）输入“7”，回车，可重新配置“ovirt-engine”服务。输入“1”，回车，可清除engine的配置；输入“2”，回车，可配置engine；输入“3”，回车，可返回上级配置页面。

    Engine Advanced Configuration
    
    
    1) Engine Cleanup !
    2) Engine Setup !
    3) Back
    
    
    Choose the advanced setting: 

######（8）输入“8”，回车，可重启或关闭系统

    Restart or Shutdown the System.
    
    1) Restart the System 
    2) Shutdown the System
    3) Back
    
    Choose the advanced setting: 

######（9）输入“9”，回车，可获得系统Shell

######（10）输入“10”，回车，可返回查看系统状态信息

######（11）输入“11”，回车，退出登陆

---

#####Note：第一次登陆后需要对系统进行初始化配置，配置流程：1-->3-->4-->2-->6，配置成功后通过浏览器访问“系统状态信息”中显示的Web Portal地址即可。
