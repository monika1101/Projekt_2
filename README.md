# Projekt_2

#CZYM ZAJMUJE SIĘ WTYCZKA?
+ Zaprojektowana wtyczka jest wtyczką eksperymetalną, która ma za zadanie obliczyć:
    - rożnicę wysokości pomiędzy dwoma wskazanymi punktami;
    - pole powierzchni (metodą Gaussa) pomiędzy wskazanymi punktami;
+ Program przelicza różnicę wysokości w układzie PL-EVRF2007-NH.
+ Współrzędne do obliczenia pola powierzchni powinny być w układzie PL-2000.
+ Pole powierzchni podane jest w metrach kwadratowych, a przewyższenie w metrach.

#CO JEST POTRZEBNE, ABY WTYCZKA ZADZIAŁAŁA?
+ Do poprawnego działania wtyczki potrzebny jest program QGIS w wersji przynajmnniej 3.0.
+ Aby skorzystać z programu potrzebny jest plik z danymi np. osnowy wysokościowej.
+ Cały projekt był testowany w systemie Windows.

#JAK URUCHOMIĆ WTYCZKĘ?
  +  ... Co po kolei klikać?
  +  W celu obliczenia przewyższenia należy wybrać tylko 2 punkty, natomiast do pola powierzchni minimum 3.
  +  Jako przykładowy plik mogą posłużyć dane osnowy wyskościowej z powiatu Ciechanowskiego: https://ciechanow.geoportal2.pl/map/geoportal/wfs.php, które trzeba zaimportować przez WFS.
 
#JAKIE WYNIKI WYGENERUJE NAM WTYCZKA?
 + Poprawnie działająca wtyczka wyświetli wynik jako napis "Pole figury pomiędzy wybranymi punktami wynosi (...) m2" lub "Przewyższenie pomiędzy punktami wynosi (...) m".
+ W przypadku wskazania niewłaściwej liczby punktów wyświetli się napis:
    - pole powierzchni: "Liczba punktów powinna być większa od 2";
    - przewyższenie: "Liczba punktów powinna wynosić 2".

  #POZOSTAŁE WAŻNE INFORMACJE
  1) ...
  2) ...
  
  #ZNANE BŁĘDY
  1) ...
  
