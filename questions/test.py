# -*- coding: utf-8 -*-

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
q_num = [1, 2, 0, 3, 4, 2, 5, 4]  # 全部题号对应的列表元素编号
for i in q_num:  # for 循环用来找到对应的每个数字对应的位置序号
    if i == 0:
        seq_num = '1st'
    elif i == 1:
        seq_num = '2nd'
    elif i == 2:
        seq_num = '3rd'
    else:
        seq_num = str(i + 1) + 'th'
    print 'The animal %s is at %d and is a %s.' %  (seq_num, i, animals[i])
    print 'The animal at %d is the %s animal and is a %s.' % (i, seq_num, animals[i])

