import sys,os
sys.path.append("../src/")
import env,requests

userpoint = "http://" + env.getenv('USER_IP') + ":" + str(env.getenv('USER_PORT'))
G_userip = env.getenv("USER_IP")
auth_key = env.getenv('AUTH_KEY')

def post_to_user(url = '/', data={}):
    return requests.post(userpoint+url,data=data).json()

cons = os.listdir('/var/lib/lxc')
for con in cons:
    print("Update %s..."%(con))
    namesplit = con.split('-')
    user = namesplit[0]
    res = post_to_user('/user/uid/',{'username':user,'auth_key':auth_key})
    configfile = open('/var/lib/lxc/'+con+'/config','r')
    context = configfile.read()
    configfile.close()
    #print(context)
    #print(res['uid'])
    context = context.replace("docklet-br","docklet-br-"+str(res['uid']))
    newfile = open('/var/lib/lxc/'+con+'/config','w')
    newfile.write(context)
    newfile.close()
