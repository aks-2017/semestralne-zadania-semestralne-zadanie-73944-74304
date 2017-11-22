Nainštalovali sme si starší mininet 2.0.0 pretože Riplpox nebol podporovaný v novších verziách mininetu a následne sme si nainštalovali Riplpox zo stránky: https://github.com/brandonheller/riplpox/blob/master/INSTALL
Potom sme si spustili kontróler riplpox pomocou príkazu:
~/pox/pox.py riplpox.riplpox --topo=ft,4 --routing=random --mode=reactive
A ďalej sme spustili topológiu, s ktorou budeme pracovať:
sudo mn --custom ~/ripl/ripl/mn.py --topo ft,4 --controller=remote –mac
Potom keď sme zistili pomocou ping, že všetky hosty sú zo sebou komunikovať skúšali sme posielanie správ.
Testovali posielať z 1. hosta na 4. hosta správy príkazom: iperf -s -i 1, ktorý spravil z prvého hosta server a z 4. hosta sme spravili klienta pomocou príkazu: iperf -c 10.0.0.2 -b 20m -n 1000 -t 15.
A zisťovali sme ako komunikujú. Následne by sme si mali v pythone spraviť kód na komunikáciu. Kde budeme zisťovať veľkosť paketu a následne príkazom s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM), vytvoríme druhý soket, ktorým pošleme tú istú spravu.
