import sys
import pygame

class EventList:
    class eve:
        def __init__(self , image , text , choice_num , choice_text , resulttext):
            self.image = image
            self.text = text
            self.choice_num = choice_num
            self.choice_text = choice_text
            self.resulttext = resulttext
            
    #事件总数，每次加事件的时候记得改
    event_num = 4
    
    evelist = []
    #属性增减 饥饿值 口渴值 san值 智商 清洁值 时间(单位15min) (单个事件的时间不要超过37)
    effect = []
    #无要求就是-1 时间要求不计在此处
    limit = []

    message = []
    

    #0
    evelist.append(eve("../res/image/test事件.png","睡迟了，要不要翘课呢",2 ,["翘！","不翘！"] , ["翘的好！","冲去上课，满身是汗"]))
    effect.append([[0,0,0,-1,0,4],[0,0,0,0,-1,4]])
    limit.append([[-1,-1,-1,1,-1],[-1,-1,-1,-1,-1]])
    message.append(["翘课睡觉咯，智商-1","冲去上课，满身是汗，清洁值-1"])
    #1
    evelist.append(eve("../res/image/test事件.png","隔壁老铁送来老坛酸菜牛肉面，要不要吃捏",2 ,["吃","不吃！"] , ["就这味儿！干净又卫生！","..."]))
    effect.append([[+1,0,0,0,-1, 1],[0,0,0,0,0, 1]])
    limit.append([[-1,-1,-1,-1,1],[-1,-1,-1,-1,-1]])
    message.append(["吃了老坛酸菜牛肉面，饥饿值+1，清洁值-1","谢绝了隔壁老铁的老坛酸菜牛肉面"])
    #2 test用 记得替换掉
    evelist.append(eve("../res/image/test事件.png","小咪亿下",1 ,["睡！"] , ["zzZZZZZZZZ..."]))
    effect.append([[0,0,0,0,0,36]])
    limit.append([[-1,-1,-1,-1,-1]])
    message.append(["小睡了亿下"])
    #3 test用 记得替换掉
    evelist.append(eve("../res/image/test事件.png","开挂！！！",1 ,["上上下下左右左右BA！"] , ["外挂已付费"]))
    effect.append([[10,10,10,10,10,0]])
    limit.append([[-1,-1,-1,-1,-1]])
    message.append(["开个小挂 不过分吧 全属性回满"])
    #4
