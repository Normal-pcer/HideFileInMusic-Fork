# 关于这个程序的视频教程：https://www.bilibili.com/video/BV1NF411i7Zh/
# 作者：B站@偶尔有点小迷糊
# 我的口号是：用不正经的风格 讲正经编程知识
#
# 二次修改：Github@Normal-pcer Bilibili@普通的PC君
# 使用本代码请保留以上信息

import wave
import os


def hide(typ, src, car, out, space=4):
    # typ: 要加密的是文本还是文件
    # src:明文文件
    # car:载体文件
    # space:修改的字节之间的间距，原作者设定默认为4

    if typ == "text":
        with open("tmp.txt", "w") as f:
            f.write(src)
    src = 'tmp.txt'
    # 打开要隐藏的文件，读取数据
    with open(src, 'rb') as f:
        txt_data = f.read()
        file_len = len(txt_data)
        txt_data = file_len.to_bytes(4, byteorder='little') + txt_data
        print("内容长度:", file_len, "字节")
        ''' 
        上一行原本为
        txt_data = file_len.to_bytes(3, byteorder='little') + txt_data
        此处的3是存放文件占用空间的，预留3字节可以存放16MB以内的文件的大小。
        但我(Normal-pcer)觉得不够，改成了4字节，现在这个程序能存放的极限是4GB
        '''

    # 打开wav格式的歌曲文件，读取数据
    with wave.open(car, "rb") as f:
        attrib = f.getparams()    # 获取音频属性
        wav_data = bytearray(f.readframes(-1))  # -1表示读到结尾

    # 隐藏txt_data中的数据到wav_data中
    for index in range(len(txt_data)):
        wav_data[index * space] = txt_data[index]

    # 生成新的歌曲文件
    with wave.open(out, "wb") as f:
        f.setparams(attrib)     # 设置音频属性
        f.writeframes(wav_data)  # 写入数据

    if typ == "text":
        os.remove("tmp.txt")
