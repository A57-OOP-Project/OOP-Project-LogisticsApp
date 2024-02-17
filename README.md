
Examples

CreatePackage BRI MEL 1500 Pesho,phone:0888777555
CreatePackage BRI SYD 11000 Olesya,phone:0888999777
FindRoute BRI MEL
CreateRoute BRI->SYD->MEL 2024-02-17 14:00
FindTruck 13000 BRI SYD MEL
AddTruck scania 1001 1
ViewRoute 1
AddPackage 1 1 
AddPackage 1 2 
ViewSystem 0
ViewPackage 1
CreatePackage ASP BRI 2000 Zoya,phone:0888555888
CreatePackage ASP BRI 7000 Zoya,phone:0888555888
CreatePackage ASP BRI 10000 Zoya,phone:0888555888
CreatePackage ASP BRI 5000 Zoya,phone:0888555888
CreatePackage ASP ADL 800 KuKu,phone:0888678678
CreatePackage MEL BRI 1000 CarnivalKids,phone:0888567567
CreatePackage ADL SYD 2000 Bravo,phone:0888123456
CreateRoute ASP->ADL->MEL->SYD->BRI 2024-02-17 23:00
FindTruck 28000 ASP ADL MEL SYD BRI
AddTruck scania 1002 2
AddPackage 2 3 
AddPackage 2 4 
AddPackage 2 5 
AddPackage 2 7 
FindRoute MEL BRI
AddPackage 2 8
ViewNotAssigned
AddPackage 2 6 
AddPackage 2 9
ViewPackage 9
RemovePackageFromRoute 2 5
ViewRoute 2
CreatePackage ADL BRI 11000 DonaldTrump,phone:0888123123
CheckRouteCapacity 2 ADL BRI 11000
end









