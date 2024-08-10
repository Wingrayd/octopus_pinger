# octopus_pinger
Ping based hardware monitoring system in python

My task is to write simple monitoring for my work (system administrator).
Requirements from the security service, network and hardware have a number of features, so it is difficult to use ready-made solutions. I decided to try to do it myself and learn how to work in Python.

At the moment, the following has been done:
1) A server base capable of connecting clients, sending them a list of addresses and receiving the results of their work as a result.
2) A client base that connects to the server, receives a list of processed addresses from it, pings them and returns data on failures to the server.
3) Added constructs to eliminate errors and the ability to reconnect from both sides of the connection.
4) Added multithreading to the server to connect multiple clients.

At this stage: for use in line 20 of the server, specify the list of addresses you need. In line 9 of the client, specify the address on which the server will be launched. The output of "silent" devices occurs in the console.
   
In the nearest plans:
1) Web interface for displaying states.
2) SQL database with lists of addresses.
2.1 SQL request for the server, which will select a list of corresponding addresses for each unique client address.
3) Containerization to simplify the distribution of clients.
4) It may be possible to implement a bot with online alarms for messenger or mail.

I will be glad to receive tips and advice on how to optimize or simplify the program, reduce the load on the network or on the hardware.

__________________________________________________________________________________________________________________________________________________________________________________________________

Моя задача написать простой мониторинг для своей работы (системный администратор).
Требования со стороны службы безопасности, сеть и "железо" имеют ряд особенностей, поэтому использовать готовые решения затруднительно. Я решил попробовать написать самостоятельно и попрактиковаться в Питоне.

На данный момент сделано:
1) Серверная основа, способная подключать клиентов, передавать им список адресов и принимать как результат итог их работы.
2) Клиентская основа, которая подключается к серверу, получает от него список обрабатываемых адресов, пропинговывает их и возвращает на сервер данные о неудачах. 
3) Добавлены конструкции для исключения ошибок и возможности реконнекта с обеих сторон подключений.
4) Добавлена многопоточность на сервер, для подключения нескольких клиентов.

На данном этапе: для использования в 20 строке сервера укажите список нужных вам адресов. В 9 строке клиента укажите адрес на котором будет запущен сервер. Вывод "молчащих" устройств происходит в консоль.

В ближайших планах:
1) Веб-интерфейс для отображения состояний.
2) SQL база данных со списками адресов.
2.1 SQL запрос для сервера, который будет подбирать список соответствующих адресов для каждого уникального адреса клиента.
3) Контейнеризация для упрощения распространения клиентов.
4) Возможно получится реализовать бота с онлайн сигнализациями для мессенджера или почты.

Я буду рад подсказкам и советам, как можно оптимизировать или упростить программу, снизить нагрузку на сеть или на "железо". 
