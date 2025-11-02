from operator import itemgetter
import data

def task_A1():
    # 1:м; список всех связанных музыкантов и оркестров, отсортированный по оркестрам, сортировка по музыкантам произвольная
    one_to_many = [(m.name, m.salary, o.name)
                   for o in data.orchestras
                   for m in data.musicians
                   if m.orchestra_id == o.id]
    sorted_result = sorted(one_to_many, key = itemgetter(2))
    print('Задание А1:')
    print(sorted_result)
    #альтернативный вывод:
    # for r in sorted_result:
        #print(r)
def task_A2():
    # 1:м; оркестры с суммарной зп музыкантов; список отсортирован по суммарной зарплате
    one_to_many = [(m.name, m.salary, o.name)
                   for o in data.orchestras
                   for m in data.musicians
                   if m.orchestra_id == o.id]
    res = []
    for o in data.orchestras:
        orch_musicians = list(filter(lambda i: i[2] == o.name, one_to_many))
        if len(orch_musicians)>0:
            total_salary = sum(m[1] for m in orch_musicians)
            res.append((o.name, total_salary))
    sorted_res = sorted(res, key = itemgetter(1), reverse = True)
    print('Задание А2:')
    print(sorted_res)
    # альтернативный вывод:
    # for r in sorted_res:
        #print(r)
def task_A3():
    print('Задание А3:')

    many_to_many_temp = [  #временный список. связывает оркестры и музыкантов
        (o.name, mo.orchestra_id, mo.musician_id)
        for o in data.orchestras
        for mo in data.musicians_orchestras
        if o.id == mo.orchestra_id]

    many_to_many = [ #полный список, состоящий из имени музыканта, зарплаты, названия оркестра
        (m.name, m.salary, o_name)
        for o_name, o_id, m_id in many_to_many_temp
        for m in data.musicians if m.id == m_id]

    filtered_orchestras = [name for name in set(d.name for d in data.orchestras) if 'оркестр' in name] #фильтруем
    res = {}
    for orchestra_name in filtered_orchestras:
        musicians_in_orchestra = list(filter(lambda i: i[2] == orchestra_name, many_to_many))
        musician_names = [m[0] for m in musicians_in_orchestra]
        res[orchestra_name] = musician_names
    print(res)
    # альтернативный вывод:
    # for org_name, musicians_list in res.items():
    #     print(f"{org_name}: {musicians_list}")