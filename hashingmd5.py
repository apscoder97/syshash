import hashlib

def hashing(val):
    encdata=hashlib.md5(val.encode())
    result=encdata.hexdigest()
    return result

if __name__ == "__main__":
    print("Enter Hash Value")
    value=input()
    flag=0
    val=value.lower()
    for i in range(1000,10000):
        send=str(i)
        newhash=hashing(send)
        if value==newhash:
            flag=1
            vak=i
            break
    if flag==1:
        print("Orginal Value is=",vak)