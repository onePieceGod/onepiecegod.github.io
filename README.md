# [GitHub上传文档方式](https://blog.csdn.net/u011108439/article/details/80609235)
## 建立本地仓库
1. 安装git客户端；  
2. 创建本地项目；
3. 进入到自己的项目文件下右键选择Git Bash Here打开git客户端；  
4. 输入命令：git init  
5. 将项目中的文件添加到本地仓库，输入指令：git add .  
6. 将文件提交到仓库，输入指令：git commit -m "这是注释内容"
## 创建GitHub仓库
1. 登录github账户，选择New repository；（首次注册并登录选择Start a project）;  
2. 根据提示创建仓库（如图）；
![](https://img-blog.csdn.net/20180607151546800)
3. 关联github仓库，获取到仓库地址并复制（如图）；
![](https://img-blog.csdn.net/20180607152042288)
4. 输入指令：git remote add origin https://github.com/xxxx/xxx.git（https://github.com/xxxx/xxx.git就是仓库地址 ）
5. 如果有弹窗对话框需要输入你的github账户密码，按照提示输入即可；如果没有请进行下一步  
6. 输入指令：git push -u origin master
按照这步骤走完之后你的本地文件就已经推送到github上去了，然后就是刷新你的github页面即可。
## 更新文件到github
1. 输入指令：git add 文件名称或者 git add.  
2. 输入指令：git commit -m "这是注释内容"  
3. 这一步从本地仓库或本地分支获取并集成(整合)，输入指令：git pull origin master  
4. 如果过程中出现‘please enter a commit message…’,首先按下esc退出键然后输入 ：wq即可  
5. 输入指令：git push -u origin master  
按照这些更新步骤走完之后刷新你的github主页就能看到文件已经推送到仓库，从仓库中的文件推送时间就可以知道。
