try:
    try:
        import sys
        import os
        import amino
        import getpass
        from banner import BANNER

    except ImportError as e:
        print(f"\033[1;31m[ERROR] \033[0m\xBB {e}")
        sys.exit()

    def Tass2(data):
        listusers = []
        for userId ,status in zip(data.userId,data.status):
            if status != 9 and status != 10:
                listusers.append(userId)
        return listusers

    def Tass(data):
        listusers = []
        for userId ,status in zip(data.profile.userId,data.profile.status):
            if status != 9 and status != 10:
                listusers.append(userId)
        return listusers

    os.system('cls' if os.name == 'nt' else 'clear')
    BANNER()

    client = amino.Client()
    ss = 0
    sz = 25
    nuum = 0
    tst = False

    while tst == False:
        try:
            email = input("\033[1;92mDigite seu email >>>\033[1;97m ")
            password = getpass.getpass("\033[1;92mDigite sua senha >>>\033[1;97m ")
            client.login(email = email,password = password)
            tst = True

        except:
            tst = False
            print("\n\033[1;91mVerificar e-mail ou senha")
            exx = input("\033[1;91mContinuar ? (s/n) >>>\033[1;97m ")
            if exx == 'n' or exx == 'N':
                os._exit(1)

    tst = False
    while tst == False:
        try:
            infoos = input("\n\033[1;92mURL do chat >>>\033[1;97m ")
            infoo = client.get_from_code(infoos)
            tst = True
            if infoo.objectType != 12:
                print("\033[1;91mURL invalida !!!")
                tst = False

        except:
            tst = False
            print("\n\033[1;91mVerificar URL")

        if tst == False:
            exx = input("\033[1;91mContinuar ? (s/n) >>>\033[1;97m ")
            if exx == 'n' or exx == 'N':
                os._exit(1)

    chatId = infoo.objectId
    comId = infoo.path[1:infoo.path.index("/")]
    sub_client = amino.SubClient(comId = comId,profile = client.profile)
    swich = 0
    tst = False

    while tst == False:
        try:
            tst = True
            swich = int(input("\n\033[1;96mEscolher: \n1 - Membros online \n2 - Seus seguidores \n3 - Novos membros \n\n>>>\033[1;97m "))
            if swich < 0 or swich > 3:
                print("\033[1;91mOps !!!, opção invalida")
                tst = False

        except :
            print("\n\033[1;91mEscolha um numero")
            tst = False

    tst = False
    while tst == False:
        try:
            tst = True
            maxo = int(input("\n\033[1;92mQual o maximo de convites por membros  >>>\033[1;97m "))

        except:
            tst = False
            print("\n\033[1;91mOps !!!, ocorreu um erro")

        if tst == False:
            tobb=input("\033[1;91mContinuar ? (s/n) >>> ")
            if tobb == "n" or tobb == "N":
                os._exit(1)
    cpt = 0
    if swich == 1:
        nemmm = 0
        cpt = 0
        while maxo > nemmm and len(sub_client.get_online_users(start = nemmm,size=25).profile.userId) != 0:
            lista = sub_client.get_online_users(start= nemmm,size = 25)

            for userId in Tass(lista):
                try:
                    sub_client.invite_to_chat(userId = userId,chatId = chatId)
                    cpt = cpt + 1
                    print(cpt , "\033[1;93m ) \033[1;92m- \033[1;93muser id\033[1;92m =\033[0m ",userId)

                except:
                    ffffff = True

            nemmm = nemmm + 25

    elif swich == 2:
        tst = False
        while tst == False:
            try:
                link = input("\n\033[1;92mLink do perfil >>>\033[1;97m ")
                linko = client.get_from_code(link)
                tst = True
                if linko.objectType != 0:
                    print ("\033[1;91mOps !!!, link invalido")
                    tst = False

                fchg = linko.path[1:infoo.path.index("/")]
                if fchg != comId:
                    tst = False
                    print ("\033[1;91mOps !!!, link invalido")

            except:
                tst = False
                print("\n\033[1;91mVerificar URL")

                if tst == False:
                    exx = input("\033[1;91mContinuar ? (s/n) >>> ")
                if exx == 'n' or exx == 'N':
                    os._exit(1)

        userIdf = linko.objectId
        nemmm = 0
        cpt = 0

        while maxo > nemmm and len(sub_client.get_user_followers(userId = userIdf,start = nemmm,size = 25).userId) != 0:
            listf = sub_client.get_user_followers(userId=userIdf,start= nemmm,size= 25)

            for userId in Tass2(listf):
                try:
                    sub_client.invite_to_chat(userId=userId, chatId = chatId)
                    cpt = cpt + 1
                    print("\n", cpt , "\n\033[1;93m ) \033[1;92m- \033[1;93muser id \033[1;92m= \033[0m",userId)

                except:
                    ffffff = True

            nemmm = nemmm + 25
    elif swich == 3:
        nemmm = 0
        cpt = 0
        while maxo > nemmm and len(sub_client.get_all_users(start = nemmm,size=25).profile.userId) != 0:
            listn=sub_client.get_all_users(start = 0,size = 25)

            for userId in Tass(listn):
                try:
                    sub_client.invite_to_chat(userId = userId,chatId = chatId)
                    cpt = cpt + 1
                    print("\n", cpt , "\n\033[1;93m ) \033[1;92m-\033[1;93m user id \033[1;92m= \033[0m",userId)

                except:
                    ffffff = True

            nemmm = nemmm + 25

    print("\n\033[1;96mProntinho !!!\n\nNão use esse ferramenta toda hora pois isso pode encomodar, ah quase me esqueci, se inscreva no meu canal no Youtube, link abaixo\n\n[+] Link - https://youtube.com/channel/UCvfhcJHqcDfnl5ukzKCFpog\n\nOutros links meus abaixo\n\n[+] Meu perfil na Otanix - http://aminoapps.com/p/3va242\n\n[+] Github - https://github.com/JoPowerTech\n")
    os._exit(1)

except KeyboardInterrupt:
    os._exit(1)
