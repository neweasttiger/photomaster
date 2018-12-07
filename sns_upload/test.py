

import subprocess

result = subprocess.check_output ('./program' , shell=True)
if result == 'AAA' :
    print "123"
elif result == 'BBB' :
    print "456"
else
    print "faild"
