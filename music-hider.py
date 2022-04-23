from pick import pick
from hide import hide
from sys import argv


if "--help" in set(argv):  # 含有选项--help
    print(
        '''
        以一个wav文件为载体，加密或解密一个文件。
        用法：
        music-hider hide [-f/-t] src -c car -o out -s space  (隐藏)
        src 要隐藏的事物
        car 载体wav文件
        out 输出文件名
        space 加密时的步长(>3的正整数)
        -f 后接src，表示src是一个文件
        -t 后接src，表示src是一串文本
        -c 后接car
        -o 后接out
        -s 后接space
        music-hider pick -i src -o out -s space  (提取)
        src 已加密的文件名
        out 输出文件名（包含扩展名）
        space 必须与加密时一直才能解密成功
        -i 后接src
        -o 后接out
        -s 后接space
        '''
    )
elif argv[1] == 'hide':
    if ('-f' not in argv and '-t' not in argv) or '-c' not in argv or '-o' not in argv or '-s' not in argv:
        raise ValueError("缺少参数")
    hide(typ=("file" if '-f' in argv else "text"), src=argv[argv.index(
        '-f' if '-f' in argv else '-t')+1], car=argv[argv.index('-c')+1], space=int(argv[argv.index('-s')+1]), out=argv[argv.index('-o')+1])
elif argv[1] == 'pick':
    if '-i' not in argv or '-o' not in argv or '-s' not in argv:
        raise ValueError("缺少参数")
    pick(src=argv[argv.index('-i')+1],
         out=argv[argv.index('-o')+1], space=int(argv[argv.index('-s')+1]))
else:
    raise ValueError("无效的启动参数: "+argv[1])
