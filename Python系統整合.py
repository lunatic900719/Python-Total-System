def menu():
    print("===================")
    print("Python系統整合\n")
    print("1.成績系統   2.點餐系統   3.計程車計費\n4.BMI計算機  5.1+~10迴圈  6.烏龜繪圖\n7.九九乘法表 8.函數面積   9.結束")
    num=input("請輸入選項:")
    return num

def grade():
    grade=0
    total=0
    average=0
    nA=nB=nC=nD=nF=0
    people=0
    while grade!=-1:
        try:
            grade=int(input("請輸入你的成績(-1時結束):"))
            if 0<=grade<=100:
                people+=1
                total+=grade
                if 60<=grade<=69:
                    print("你的成績為%d,D"%(grade))
                    nD+=1
                elif 70<=grade<=79:
                    print("你的成績為%d,C"%(grade))
                    nC+=1
                elif 80<=grade<=89:
                    print("你的成績為%d,B"%(grade))
                    nB+=1
                elif 90<=grade:
                    print("你的成績為%d,A"%(grade))
                    nA+=1
                elif grade<=59:
                    print("你的成績為%d,F"%(grade))
                    nF+=1
            elif grade==-1:
                print("結束輸入成績")
            else:
                print("成績必須介於0~100之間")
        except:
            print("輸入資料型態錯誤")
        average=float(total/people)
        print("A的人數為%d個,B的人數為%d個,C的人數為%d個,D的人數為%d個,F的人數為%d個,總分為%d,共%d人,平均為%.2f"%(nA,nB,nC,nD,nF,total,people,average))

def order():
    bm=fm=dm=0
    burger=input("請問你要點漢堡嗎?(NT$40)(y/n)")
    if burger=="y":
        bm=int(input("請書輸入您要購買的數量:"))
    fries=input("請問你要點薯條嗎?(NT$30)(y/n)")
    if fries=="y":
        fm=int(input("請書輸入您要購買的數量:"))
    drink=input("請問你要點飲料嗎?(NT$25)(y/n)")
    if drink=="y":
        dm=int(input("請書輸入您要購買的數量:"))
    total=bm*40+fm*30+dm*25
    print("您點了漢堡%d份,薯條%d份,飲料%d杯,共需%d元"%(bm,fm,dm,total))


def taxi():
    fee=tt=gt=jt=0 
    distance=float(input("請輸入搭乘的里程(公里):"))
    if distance<=1.25:
        fee=70
    else:
        tt=int((distance-1.25)/0.2)
        fee+=70+tt*5
    jt=int(input("請輸入塞車時間(秒):"))
    if jt>=80:
        fee+=jt/80*5
    gt=int(input("請輸入上車時間:"))
    if gt>=23 or gt<=6:
        fee+=20
    ny=input("是否為春節期間?(y/n)")
    if ny=="y":
        fee+=20
    print("您的搭乘里程為%.2f公里,您的上車時間為%d,塞車時間為%d秒,共%d元"%(distance,gt,jt,fee))    

def bmi():
    name=input("請輸入名稱:")
    weight=int(input("請輸入體重:"))
    height=int(input("請輸入身高:"))
    Height=height/100
    BMI=weight/Height**2
    print("name:%s,weight:%d,height:%d,BMI:%6.2f"%(name,weight,height,BMI))


def iloop():
    keep="y"
    while keep=="y":
        n=int(input("請輸入一個正整數:"))
        total=0

        for i in range(n,1,-1):
            if i<n:
                print(str(i)+"+",end="")
            else:
                print(str(i),end="")
            total+=i
            i+=1

        if n>0:
            print("="+str(total))
        else:
            print("請輸入正整數!")
        keep=input("是否繼續(y/n)?")


def draw():
    import turtle

    def menu():
        print("==================")
        print("1.畫圓")
        print("2.畫線")
        print("3.結束")
        ch=input("請輸入你的選項:")
        turtle.clear()
        return ch

    def drawcircles():
        try:
            turtle.hideturtle()
            speed=int(input("請輸入速度:"))
            color=input("請輸入顏色(English):")
            size=int(input("請輸入線粗細大小:"))
            num_cir=int(input("請輸入圓的個數(>0):"))
            if num_cir>0:
                radius=int(input("請輸入圓半徑(>0):"))
                ani_speed=0
                angle=360/num_cir
                turtle.pencolor(color)
                turtle.penup()
                turtle.goto(0,0)
                turtle.pendown()
                turtle.speed(ani_speed)
                turtle.pensize(size)

                for x in range(num_cir):
                    turtle.circle(radius)
                    turtle.left(angle)
            else:
                print("圓的個數不正確")
        except:
            print("資料型態錯誤")

    def drawlines():
        try:
            start_x = -200
            start_y = 0

            speed=int(input("請輸入速度:"))
            color=input("請輸入顏色(English):")
            size=int(input("請輸入線粗細大小:"))
            num_lines=int(input("(請輸入線的個數必須是4的倍數):"))
            if num_lines>0 and num_lines%4==0:
                line_len=int(input("請輸入線的長度(>0):"))
                angle=180-360/num_lines

                turtle.hideturtle()
                turtle.penup()
                turtle.goto(start_x,start_y)
                turtle.pendown()
                turtle.speed(speed)
                turtle.pencolor(color)
                turtle.pensize(size)

                for x in range(num_lines):
                    turtle.forward(line_len)
                    turtle.left(angle)

            else:
                print("線的個數不正確")
        except:
            print("資料型態錯誤")


    while True:
        choice=menu()
        if choice=="1":
            drawcircles()
        elif choice=="2":
            drawlines()
        elif choice=="3":
            print("謝謝使用")
            break
        else:
            print("無此選項")

def nine():
    for i in range(1,10):
        for j in range(1,10):
            print("%dx%d=%d"%(j,i,i*j),end="\t")
        print()

def area():
    def showmenu():
        print("==================")
        print("面積計算")
        print("1.圓面積/周長")
        print("2.長方形面積")
        print("3.三角形面積")
        print("4.離開")
        ch=input("請輸入你的選項:")
        return ch


    def Tarea(c,d):
        if c>0 and d>0:
            Tarea=c*d/2
            print("底:%d,高:%d,面積:%.2f"%(c,d,Tarea))
        else:
            print("資料錯誤")

    def triangle():
        try:
            a=int(input("請輸入底:"))
            b=int(input("請輸入高:"))
            Tarea(a,b)
        except:
            print("資料型態錯誤")
        
    def Rarea(length,width):
        if length>0 and width>0:
            Rarea=length*width
            print("長:%d,寬:%d,面積:%d"%(length,width,Rarea))
        else:
            print("資料錯誤")

    def rectangle():
        try:
            length=int(input("請輸入長:"))
            width=int(input("請輸入寬:"))
            Rarea(length,width)
        except:
            print("資料型態錯誤")

    def Carea(r):
        if r>0:
            area=r*r*3.1416
            circum=2*r*3.1416
            print("半徑:%d,圓面積:%.2f,圓周長:%.2f"%(r,area,circum))
        else:
            print("資料錯誤")

    def circle():
        try:
            radius=int(input("請輸入半徑:"))
            Carea(radius)
        except:
            print("資料型態錯誤")



    def main():
        while True:
            choice=showmenu()
            if choice=="1":
                circle()
            elif choice=="2":
                rectangle()
            elif choice=="3":
                triangle()
            elif choice=="4":
                print("謝謝使用")
                break
            else:
                print("無此選項")
    main()

while True:
    num=menu()
    if num=="1":
        grade()
    elif num=="2":
        order()
    elif num=="3":
        taxi()
    elif num=="4":
        bmi()
    elif num=="5":
        iloop()
    elif num=="6":
        draw()
    elif num=="7":
        nine()
    elif num=="8":
        area()
    elif num=="9":
        print("結束")
        break
    else:
        print("無此選項")