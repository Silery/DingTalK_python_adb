# -
校园钉钉打卡
环境配置

PC
安装adb，python3 都加入环境变量
Android

1，打开开发者模式（不会的可以百度，我的手机是红米例如：红米手机打开开发者模式）
2. 勾选usb调试
3. 用数据线连接手机和电脑
4. ![image](https://user-images.githubusercontent.com/61609966/163714669-54fa9178-4466-4a13-85c1-81a526c9ef45.png)


关于代码的详细解析
主要就是利用adb shell 的命令 实现手机点击、输入、左滑、右滑、上滑的操作

可以打开开发者选项里的指针位置自定义软件的位置

点击check(x，y):	

  ![image](https://user-images.githubusercontent.com/61609966/163714785-0992b790-3cfe-4148-9518-a4441d6bf880.png)
  ![image](https://user-images.githubusercontent.com/61609966/163714872-d21c8867-6f1f-4102-8e51-3cc45a9a48e1.png)
  
swipe_up(x1,y1,x2,y2)


指定位置移动到另一位置实现滑动
  
