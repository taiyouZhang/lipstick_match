# lipstick_match 
## Introduction
Find an interesting [blog](https://mp.weixin.qq.com/s/Y3kGNaslGBArh-seI15c0w), and try to implement the whole functionality.<br>
By the way, distinguish lipsticks is too hard for me. I hope this tool can help me in some ways.

## Dependencies
+ PIL/Pillow
+ dlib
+ opencv

## Data structure
+ src/main.py<br> 
    This file is the main source codes to classify lipsticks from screenshots.
+ data/pic<br>
    All screenshots are put into this folder. **Notes:** Since we use os.path.listdir, all files in this folder should only serve for single task. 
+ data/lipstick.json<br> 
    Copied from [Project:lipstick](http://zhangwenli.com/lipstick/)

## Commands
There are 2 kinds of tasks:
1. Distinguish the kind of lipstick from portraits `python3 main.py ../data/pic/face`
2. Distinguish the kind of lipstick from color block `python3 main.py ../data/pic/color/ -m match`

## Next
At first, we should put screenshots or photos on laptop.<br> Then, maybe we can install the program on phones.

## Warning
Since I have downloaded some pictures of lipsticks from websites, the precision of results is not good enough. Maybe the filter on photos is a big problem.
