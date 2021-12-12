from operator import itemgetter
 
class  HDD:
    """Жесткий диск"""
    def __init__(self, id, name_hdd, cap, pc_id):
        self.id = id
        self.name_hdd = name_hdd # имя
        self.cap = cap # вместимость диска (Гигабайт)
        self.pc_id = pc_id # в каком компьютере
 
class PC:
    """Компьютер"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class HddPc:
    """
    связь многие ко многим
    """
    def __init__(self, pc_id, hdd_id):
        self.pc_id = pc_id
        self.hdd_id = hdd_id
 
# Компьютеры
Pcs = [
    PC(1, 'компьютер HP'),
    PC(2, 'компьютер MSI'),
    PC(3, 'MacBook Pro'),
    PC(4, 'компьютер Alienware'),
    PC(5, 'компьютер Asus'),
    PC(6, 'MacBook Air'),
]
 
# Жесткие диски
hdds = [
    HDD(1, 'Seagate', 5120, 2),
    HDD(2, 'Samsung', 2048, 1),
    HDD(3, 'Macintosh', 1024, 3),
    HDD(4, 'Toshiba', 3072, 4),
    HDD(5, 'WD blue', 4096, 5),
    HDD(6, 'WD gold', 2048, 1),
    HDD(7, 'Macintosh', 512, 6),
    HDD(8, 'Seagate Baracuda', 4096, 4),
    HDD(9, 'Toshiba', 4096, 5)
]
 
hdds_pcs = [
    HddPc(1,1),
    HddPc(1,2),
    HddPc(1,4),
    HddPc(1,8),
    HddPc(2,4),
    HddPc(2,5),
    HddPc(2,6),
    HddPc(2,1),
    HddPc(3,3),
    HddPc(4,1),
    HddPc(4,5),
    HddPc(5,4),
    HddPc(5,2),
    HddPc(6,7),

]
 
    # Соединение данных один-ко-многим 
one_to_many = [(h.name_hdd, h.cap, p.name) 
        for p in Pcs 
        for h in hdds 
        if h.pc_id==p.id]
    
    # Соединение данных многие-ко-многим
many_to_many_temp = [(p.name, ph.pc_id, ph.hdd_id) 
        for p in Pcs 
        for ph in hdds_pcs 
        if p.id==ph.pc_id]
    
many_to_many = [(h.name_hdd, h.cap, pc_name) 
        for pc_name, pc_id, hdd_id in many_to_many_temp
        for h in hdds if h.id==hdd_id]

def E1():
    print('Задание E1')
    res_E1 = []
    for name_hdd, cap, name in one_to_many:
        if 'компьютер' in name: # Ищем компьютеры с ключевым словом "компьютер"
            res_E1.append((name, name_hdd))
    return res_E1        
    
def E2():
    print('\nЗадание E2')
    # находим среднюю вместимость жестких дисков 
    res_E2_unsorted = []
    # Перебираем все компьютеры
    for p in Pcs:
        # Список жестких дисков компьютера
        list_hdd = list(filter(lambda i: i[2]==p.name, one_to_many))
        # Если в компьютере есть жесткий диск        
        if len(list_hdd) > 0:
            # вместимомть HDD
            list_cap = [cap for _,cap,_ in list_hdd]
            # средняя вместимость
            avg_sum = sum(list_cap)/len(list_cap)
            res_E2_unsorted.append((p.name, avg_sum))
    res_E2 = sorted(res_E2_unsorted, key=itemgetter(1))
    return res_E2
        
def E3():
    print('\nЗадание E3')
    # находим жесткие диски, начинающиеся с "S" и выводим их компьютеры
    res_E3 = []
    for name_hdd, cap, name in many_to_many:
        if name_hdd.find("S") == 0:
            res_E3.append((name_hdd, name))
    return res_E3        

