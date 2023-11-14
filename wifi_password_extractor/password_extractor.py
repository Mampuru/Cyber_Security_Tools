import subprocess

#getting meta data
meta_data = subprocess.check_output(['netsh','wlan','show','profiles'])

#decoding meta data
data = meta_data.decode('utf-8',errors = "backslashreplace")

#splitting data by line by line
data = data.split('\n')

#creating a list of profiles
profile = []

for i in data:
    #find all user profile in each line item
    if "All User Profile" in i:
        i = i.split(":") #split the item by :
        i = i[1] #item at index 1 is the wifi name
        i = i[1:-1] #fomatting the name
        profile.append(i) #addin wifi name to the list

print("{:<30} | {:<}".format("Wi-Fi name","Password"))
print("------------------------------------")

for i in profile:
    try:
        result = subprocess.check_output(['netsh','wlan','show','profiles',i,'key = clear'])

        result = result.decode('utf-8',errors = "backslashreplace")
        result = result.split('\n')

        result = [b.split(":")[1][1:-1] for b in result if "Key Content" in b]

        try:
            print("{:<30} | {:<}".format(i,result[0]))
        except IndexError:
            print("{:<30} | {:<}".format(i,""))
    
    except subprocess.CalledProcessError:
        print("Encodeing Error occured")
