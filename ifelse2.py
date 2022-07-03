friend = ['Korkai','Khorkai','Khorkwai','Somchai']
friend1 = {'Korkai': 'คุณ ก.ไก่',
           'Khorkai': 'คุณ ข.ไข่',}


visitor = 'somchai'

if visitor  and visitor.title() in friend:
    print('เป็นเพื่อนกุเอง เชิญเข้ามาด้านใน')
    if visitor in friend1 or visitor.title() in friend1:
        print('สวัสดี '+ friend1[visitor.title()])
    else:
        print('สวัสดีคุณลูกค้า')

else :
    print('ควย มึงเป็นใคร ออกไปเลย')