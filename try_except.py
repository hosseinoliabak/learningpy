'''
Here the conversion drops into the except: clause and the program continues
'''
sStr = 'Hello Bob'
try:
    iStr = int(sStr)
except:
    iStr = -1

print('First',iStr)

'''
Here the conversion succeeds; it just skips the except: caluse
and the program continues
'''
sStr = '123'
try:
    iStr = int(sStr)
except:
    iStr = -1

print('Second',iStr)
