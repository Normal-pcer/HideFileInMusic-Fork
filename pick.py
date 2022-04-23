# 关于这个程序的视频教程：https://www.bilibili.com/video/BV1NF411i7Zh/
# 作者：B站@偶尔有点小迷糊
# 我的口号是：用不正经的风格 讲正经编程知识
#
# 二次修改：Github@Normal-pcer Bilibili@普通的PC君
# 使用本代码请保留以上信息

import wave


def pick(src, out, space=4):
    # 打开藏有其它文件的歌曲文件，读取数据
    with wave.open(src, 'rb') as f:
        wav_data = f.readframes(-1)

    # 提取wav_data中的特殊位置数据
    extract_data = bytearray()
    for index in range(0, len(wav_data), space):
        extract_data += (wav_data[index]).to_bytes(1, byteorder='little')

    # 得到被隐藏的文件的大小
    file_len = int.from_bytes(extract_data[0:4], 'little')
    print("内容长度:", file_len, "字节")

    # 重新生成被隐藏的文件
    with open(out, 'wb') as f:
        f.write(extract_data[4: file_len+4])


'''
with wave.open('隐藏后-音乐.wav', 'rb') as f:
    wav_data = f.readframes(-1)

# 提取wav_data中的特殊位置数据
extract_data = bytearray()
for index in range(0, len(wav_data), 4):
    extract_data += (wav_data[index]).to_bytes(1, byteorder = 'little')

# 得到被隐藏的文件的大小
file_len = int.from_bytes(extract_data[0:3], 'little')

# 重新生成被隐藏的文件
with open('提取结果-三体.txt', 'wb') as f:
    f.write(extract_data[3 : file_len+3])
'''
