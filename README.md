# Projekt_2

#CZYM ZAJMUJE SIĘ WTYCZKA?
+ Zaprojektowana wtyczka jest wtyczką eksperymetalną, która ma za zadanie obliczyć:
    - rożnicę wysokości pomiędzy dwoma wskazanymi punktami;
    - pole powierzchni (metodą Gaussa) pomiędzy wskazanymi punktami;
+ Program przelicza różnicę wysokości w układzie PL-EVRF2007-NH.
+ Współrzędne do obliczenia pola powierzchni powinny być pobrane z geometrii punktów.
+ Pole powierzchni podane jest w metrach kwadratowych, a przewyższenie w metrach.

#CO JEST POTRZEBNE, ABY WTYCZKA ZADZIAŁAŁA?
+ Do poprawnego działania wtyczki potrzebny jest program QGIS w wersji przynajmnniej 3.0.
+ Aby skorzystać z programu potrzebny jest dowolny plik z danymi zawierającymi atrybuty H z układu "PL-EVRF2007-NH", np. warstwa osnowy wysokościowej.
+ Współrzędne punktów pobrane z geometrii punktów.
+ Cały projekt był testowany w systemie Windows.

#JAK URUCHOMIĆ WTYCZKĘ?
 +  Należy zainstalować zaprogramowaną wtyczkę oraz pobrać dane do obliczeń.
 +  Po pobraniu wtyczki, czyli folderu o nazwie "wtyczka_projekt_2", należy go umieścić w folderze "plugins". Można go odnaleźć poprzez program QGIS, kolejno: "Ustawienia", "Profile użytkownika", "Otwórz katalog aktywnego profilu", "python". To tylko przykładowa propozycja instalacji wtyczki. 
 +  Jako przykładowy plik mogą posłużyć dane osnowy wyskościowej z powiatu Ciechanowskiego: https://ciechanow.geoportal2.pl/map/geoportal/wfs.php, które trzeba zaimportować przez WFS.
 +  W celu obliczenia przewyższenia należy wybrać tylko 2 punkty, natomiast do pola powierzchni minimum 3.
 +  Należy zaznaczyć potrzebną liczbę punktów oraz wybrać wtyczkę, wyświetli się okno z opcjami obliczeń. Dostępne są przyciski "Policz pole" skutkujący wyświetleniem pola powierzchni pomiędzy wybranymi punktami oraz przycisk "Policz różnicę wysokości" liczący przyrost wysokości pomiędzy wybranymi punktami.  

#JAKIE WYNIKI WYGENERUJE NAM WTYCZKA?
 + Poprawnie działająca wtyczka wyświetli wynik jako napis "Pole figury pomiędzy wybranymi punktami wynosi (...) m2" lub "Przewyższenie pomiędzy punktami wynosi (...) m".
+ W przypadku wskazania niewłaściwej liczby punktów wyświetli się napis:
    - pole powierzchni: "Liczba punktów powinna być większa od 2!";
    - przewyższenie: "Liczba punktów powinna wynosić 2!".
  
  #ZNANE BŁĘDY
1) Z zakresu pola powierzchni: Okazało się, że dla niektórych wybranych punktów wtyczka wyświetla wynik ujemny, co oczywiście jest błędną wartością, dlatego wyniki z zakresu obliczania pól powierzchni nie powinny być brane pod uwagę.
  
