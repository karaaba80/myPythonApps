import sys
import numpy as np
import cv2

sys.path.append('common')
import command_parser_v2 as cp


def main():
    p = cp.parser(sys.argv, registeredInfo=[
        ['-c', 'capital', '169000'],
        ['-r', 'rente', '1.16'],
        ['-y', 'how many years', '30'],
    ])

    capital = int(p.get_all('-c'))
    rente = float(p.get_all('-r'))
    years = int(p.get_all('-y'))
    total_cost = (years*capital*rente*0.01)
    div = (1-(1+rente*0.01)**(-years))
    total_cost = total_cost/div

    gws = 130
    internet = 40
    water_tax = 40

    currency = 'avro'

    print ('alinan kredi', capital, currency)
    print ('sabit', years, 'yillik faiz')
    print('kredi faiz orani %', rente)
    print('toplam odeme:', round(total_cost), currency)
    print('yillik odeme:', round((total_cost) / years), currency)
    print('aylik odeme (ev):', round((total_cost) / (years * 12)), currency)
    print('aylik tahmini odeme (ev ve diger ucretler):', round((total_cost) / (years * 12))+gws+internet+water_tax, currency)
    # print ('div', div)
    print()
    print ('toplam ortalama faiz odemesi:', round(total_cost-capital), currency)
    print('yillik ortalama faiz odemesi:', round((total_cost - capital)/years), currency)
    print('aylik ortalama faiz odemesi:', round((total_cost - capital)/(years*12)), currency)




if __name__ == '__main__':
    main()    