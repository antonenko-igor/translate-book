def verbose(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }

    if (num < 20):
        return d[num]

    if (num < 10**2):
        if num % 10 == 0:
            return d[num]     
        else: 
            return d[num // 10 * 10] + '-' + d[num % 10]
    if (num < 10**3):
        if num % 100 == 0: 
            return d[num // 100] + ' hundred'
        else: 
            return d[num // 100] + ' hundred  ' + verbose(num % 100)
    if (num < 10**6):
        if num % 10**3 == 0: 
            return verbose(num // 10**3) + ' thousand'
        else: 
            return verbose(num // 10**3) + ' thousand, ' + verbose(num % 10**3)
    if (num < 10**9):
        if (num % 10**6) == 0: 
            return verbose(num // 10**6) + ' million'
        else: 
            return verbose(num // 10**6) + ' million, ' + verbose(num % 10**6)
    if (num < 10**12):
        if (num % 10**9) == 0: 
            return verbose(num // 10**9) + ' billion'
        else: 
            return verbose(num // 10**9) + ' billion, ' + verbose(num % 10**9)
    if (num % 10**12 == 0): 
        return verbose(num // 10**12) + ' trillion'
    else: 
        return verbose(num // 10**12) + ' trillion, ' + verbose(num % 10**12)   
print(verbose(1234569854213))