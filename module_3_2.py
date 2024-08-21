def send_email(message, recipient,*,sender="university.help@gmail.com"):
    result = ""
    if ("@" in recipient) and ("@" in sender):
        if (recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net")) and (
                sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(".net")):
            if sender == recipient:
                result = "Нельзя отправить письмо самому себе!"
                print(result)
                return (0)
            else:
                if sender == "university.help@gmail.com":
                    result = "Письмо успешно отправлено с адреса " + sender + " на адрес " + recipient +"."
                    print(result)
                    return(1)
                else:
                    result = "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + sender + " на адрес " + recipient +"."
                    print(result)
                    return (1)

        else:
            result = "Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient + "."
            print(result)
            return (0)

    else:
        # если нет символа @ в адресе
        result = "Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient + "."
        print(result)
        return(0)


    return(1)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
