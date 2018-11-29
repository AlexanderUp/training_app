# encoding:utf-8
# эквивалентно-эффективная температура (зависимость от температуры, влажности воздуха и скорости ветра)

# ver. 1.0

'''
Эквивалентно-эффективная температура (ЭЭТ) учитывает комплексное влияние на человека температуры,
влажности воздуха и скорости ветра. ЭЭТ представляет собой сочетание метеовеличин,
производящее тот же тепловой эффект, что и неподвижный воздух при 100%-ной относительной влажности и
определенной температуре, и оценивает теплоощущение обнаженного по пояс человека.

================================================================================
ЕТ °C        |    Уровень комфорта
--------------------------------------------------------------------------------
>30	         |    Тепловая нагрузка сильная
24....30	 |    Тепловая нагрузка умеренная
18…24	     |    Комфортно – тепло
12...18	     |    Комфорт (умеренно тепло)
6…12	     |    Прохладно
0…6	         |    Умеренно прохладно
–6…0	     |    Очень прохладно
–6…–12	     |    Умеренно холодно
–12…–18	     |    Холодно
–18…–24	     |    Очень холодно
< –24	     |    Начинается угроза обморожения
================================================================================

Категории теплоощущения в градусах ЭЭТ в условиях умеренных широт
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Категория теплоощущения	ЭЭТ для человека
--------------------------------------------------------------------------------
	                   |       раздетого	          |    одетого
--------------------------------------------------------------------------------
Комфортно	           |       17.3–21.7	          |    16.7–20.6
Зона охлаждения	       |       ниже 17.3	          |    ниже 16.7
Зона перегрева	       |       выше 21.7	          |    выше 20.6
================================================================================
'''


def eet(t, v, f):
     '''
     by A.Missenard
     t - air temperature, degrees of Celsius
     v - wind speed, meters per second
     f - relative humidity, %
     '''
     return (37 - (37 - t) / (0.68 - 0.0014 * f + (1 / (1.76 + 1.4 * v ** .75))) - 0.29 * t * (1 - f / 100))


def eet2(t, v, f):
     '''
     by B.A.Aisenshtat
     t - air temperature, degrees of Celsius
     v - wind speed, meters per second
     f - relative humidity, %
     '''
     return (t * (1 - 0.003 * (100 - f)) - 0.385 * v ** 0.59 * ((36.6 - t) + 0.622 * (v - 1)) + ((0.0015 * v + 0.008) * (36.6 - t) - 0.0167) * (100 - f))


if __name__ == '__main__':
    print('=' * 75)
    t = 20
    v = 10
    f = 75
    print('t = {}, v = {}, f = {} ==> eet = {}'.format(t, v, f, eet(t, v, f)))
    print('t = {}, v = {}, f = {} ==> eet2 = {}'.format(t, v, f, eet2(t, v, f)))
