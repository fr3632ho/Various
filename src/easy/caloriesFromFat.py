import sys
import math

fat,pss,alcohol = 9,4,7

def parse_data():
    data = [[i for i in j.strip('\n').split('\n')] for j in sys.stdin.read().rstrip('\n').split('-')]
    data = data[:len(data)-2]
    return data

def main():
    data = parse_data()
    #print(data)
    for value in data:
        #print(value)
        converter(value)

def converter(value):
    total_calories = fats_total = 0
    for meal in value:
        # Meal calories and fat calories per meal
        m_c = m_p = 0
        f_c = f_p = 0
        for i, num in enumerate(meal.split(' ')):
            current = 0
            # Parse the values
            if 'g' in num:
                current = stripToInt(num,'g')
                if i == 0:
                    f_c += current * fat
                    m_c += current * fat
                elif i == 4:
                    m_c += current * alcohol
                else:
                    m_c += current * pss
            elif '%' in num:
                current = stripToInt(num,'%')
                if i == 0:
                    f_p += current
                m_p += current
            else:
                current = stripToInt(num,'C')
                if i == 0:
                    f_c += current
                m_c += current
        # Calculate how many calories one percent is
        remainder_p = 100 - m_p
        one_percent = m_c/remainder_p
        m_c += one_percent * m_p
        if f_p != 0:
            f_c += f_p * one_percent
        fats_total += f_c
        total_calories += m_c
    print(f'{round(100*(fats_total/total_calories))}%')


def stripToInt(str,char):
    return int(str.strip(char))

if __name__=="__main__":
    main()
