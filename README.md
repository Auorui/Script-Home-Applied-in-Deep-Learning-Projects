# Script-Home-Applied-in-Deep-Learning-Projects
This is a repository for storing scripts, where you can find suitable ones or easily modify them.
数据划分会用到的一些使用脚本。

# [Script01.py](https://github.com/Auorui/Script-Home-Applied-in-Deep-Learning-Projects/blob/main/Script01.py) : 按照后缀名不同划分入不同的文件夹中
* 用法：主要是将相同后缀的数据划分到同一文件夹当中

原本目录结构：

data

    -001.jpg

    -001.png
    
    -001.txt
  
    ...
  
脚本转换后Script transform：

savedata

    -jpg
  
      -001.jpg
  
    -png
  
      -001.png
  
    -txt
    
      -001.txt
    
# [Script02.py](https://github.com/Auorui/Script-Home-Applied-in-Deep-Learning-Projects/blob/main/Script02.py) : 修改图片的大小并存放在指定的文件路径
* 用法：主要是将训练过程中不符合网络要求的图像进行reshape。
  
    Example：
  
        - original_img 1440x1080
  
        -> reshaped_img 864x640
  
# [Script03.py](https://github.com/Auorui/Script-Home-Applied-in-Deep-Learning-Projects/blob/main/Script03.py) : 修改图片后缀并存放在指定的文件路径
* 用法：主要是将训练过程中不符合网络要求的图像进行reshape。
  
    Example：
  
        - originalimg.png
  
        -> reshaped.jpg
  
