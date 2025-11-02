from classes import Orchestra, Musician, MusiciansOrchestras

orchestras = [
    #id оркестра, название оркестра
    Orchestra(1, 'симфонический оркестр'),
    Orchestra(2, 'джазовый оркестр'),
    Orchestra(3, 'камерный оркестр'),
    Orchestra(4, 'народных инструментов'),
    Orchestra(5, 'духовой оркестр'),]

musicians = [
    #id музыканта, имя, зарплата, id оркестра
    Musician(1, 'Алексей', 30000, 1),
    Musician(2, 'Николай', 35000, 2),
    Musician(3, 'Иван', 40000, 3),
    Musician(4, 'Анастасия', 27000, 1),
    Musician(5, 'Мария', 25000, 4),]
#список объектов класса MusiciansOrchestras со связью м:м
#один музыкант может играть в нескольких оркестрах, в одном оркестре могут играть разные музыканты
musicians_orchestras = [
    #(оркестр-музыкант)
    MusiciansOrchestras(1, 1),
    MusiciansOrchestras(1, 4),
    MusiciansOrchestras(2, 2),
    MusiciansOrchestras(2, 4),
    MusiciansOrchestras(3, 3),
    MusiciansOrchestras(4, 5),
    MusiciansOrchestras(5, 5),]