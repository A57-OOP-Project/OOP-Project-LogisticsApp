<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# OOP Logistics App 
*Prepared by Olesya, Mihail and Svetoslav*<br /> 
*Version: v1.00*<br /> 

The logistics application is a console based application where employees can access it through writing commands on the console once it is started. It is the digital database and footprint for a parcel based freight business. It operates using 12 commands. 

It supports packages, routes, trucks and customer information. Embedded in the application are:
1. Distances between the major Australian freight hubs requested (further details below). 
2. Truck details for three truck brands with their capacity and maximum ranges(further details below)

#### Please note that all commands should include the command name and the required parameters e.g. `CreatePackage BRI MEL 1500 Pesho,phone:0888777555`

## Commands
### 1. Packages
&ensp;&ensp;&ensp;By using commands you can manage the package by creating it in the system, adding it to a route, view the status of a package using its ID.

#### &ensp;&ensp;1.1 Create a package
- Command is `CreatePackage` and you need to include parameters in the following order:
    - **Start location** - should be text (string) using the location hub abbreviaton available further below
    - **End location** - should be text (string) using the location hub abbreviaton available further below
    - **Weight of the package** - should be a number up to the maximum capacity of the truck
    - **Customer contact info** - please add a string with no spaces

&ensp;&ensp;&ensp;It automatically creates an ID of the package. <br/>
&ensp;&ensp;&ensp;Example: `CreatePackage BRI MEL 1500 Pesho,phone:0888777555`

#### &ensp;&ensp;1.2 Add a package to a route
&ensp;&ensp;&ensp;***Prerequisites:** Need to create the **route** prior to assigning any packages to it. The **package** should have been created prior to assigning it to a route as well <br/>
&ensp;&ensp;&ensp;**Additional checks included:** whether all locations have capacity to receive the package.*
- Command is `AddPackage` and you need to include parameters in the following order:
    - **Route ID** - the route to which we are adding the package
    - **Package ID** - the package tp be added to this specific route

&ensp;&ensp;&ensp;Example: `AddPackage 1 1` 

#### &ensp;&ensp;1.3 View created but unassgined packages
- Command is `ViewNotAssigned` and *no parameters are required* 

&ensp;&ensp;&ensp;Example: `ViewNotAssigned` 
 
#### &ensp;&ensp;1.4 View the status of a package using its ID 
- Command is `ViewPackage ` and you need to include:
    - **Package ID** is the only parameter

&ensp;&ensp;&ensp;Example: `ViewPackage 1` 

#### &ensp;&ensp;1.5 Remove package from a route 
- Command is `RemovePackageFromRoute` and you need to include parameters in the following order:
    - **Route ID** - the route from which the package is being removed
    - **Package ID** - the package to be removed from this specific route

&ensp;&ensp;&ensp;Example: `RemovePackageFromRoute 2 5` 

### 2. Routes
&ensp;&ensp;&ensp;By using commands you can manage the routes by creating it in the system, assigning packages and trucks to it, check detailed information for a route.

#### &ensp;&ensp;2.1 Create a desired route 
- Command is `CreateRoute` and you need to include:
    - **Stops** - use the location hub abbreviation further below. Please separate them by **'->'** no spaces around them e.g. **MEL->BRI->ASP**

&ensp;&ensp;&ensp;Example: `CreateRoute BRI->SYD->MEL 2024-02-15 23:00` <br/>
&ensp;&ensp;&ensp;It automatically creates an ID of the route. 

#### &ensp;&ensp;2.2 Find existing routes present in the system 
- Command is `FindRoute` and you need to include parameters in the following order:
    - **Start location** - use the corresponding abbreviation below for the location
    - **End location** - use the corresponding abbreviation below for the location

&ensp;&ensp;&ensp;Example: `FindRoute BRI MEL` <br/>

#### &ensp;&ensp;2.3 Request detailed information on a specific route
- Command is `ViewRoute` and include:
    - **Route ID** is the only parameter

&ensp;&ensp;&ensp;Example: `ViewRoute 1` <br/>

#### &ensp;&ensp;2.4 Check route's capacity using the required weight capacity and locations
- Command is `CheckRouteCapacity` and include the following parameters in this order:
    - **Route ID** - the route ID to which to add the Truck. It should be a number (integer)
    - **Start location** - it should be text (string)
    - **End location** - it should be text (string)
    - **Weight** - the required weight capacity for the route. It should be a number (integer)

&ensp;&ensp;&ensp;Example: `CheckRouteCapacity 2 ADL BRI 11000` <br/>

### 3. Trucks
&ensp;&ensp;&ensp;By using commands you can manage the trucks by finding a suitable truck for a route, adding it directly to a route.

&ensp;&ensp;&ensp;**Important assumption: Only one truck can be added to any one route.**

#### &ensp;&ensp;3.1 Add truck to a route
- Command is `AddTruck` and include the following parameters in this order:
    - **Brand** - Brand as per table further below
    - **Truck ID** - truck ID to which we want to assign the package. ??????? Q below
    - **Route ID** - which route to be added

&ensp;&ensp;&ensp;Example: `AddTruck scania 1002 2` <br/>

#### &ensp;&ensp;3.2 Find a suitable truck for the required route (with associated stops) and required weight capacity.
- Command is `FindTruck` and include the following parameters in this order:
    - **Weight** - what the weight capacity required. It should be a number (integer)
    - **Locations** - please include all location hubs which the truck is required to make a stop. Use the abbreviations below.

&ensp;&ensp;&ensp;Example: `FindTruck 13000 BRI SYD MEL` <br/>

### 4. View status of the system 
&ensp;&ensp;&ensp;Overall status of items in progress:
- Command is `ViewSystem` and *no parameters are required* 

&ensp;&ensp;&ensp;Example: `ViewSystem` <br/>


## Databases
&ensp;&ensp;&ensp;The following databases are embedded in the application:<br/>
&ensp;&ensp;&ensp;**Distances** in kilometers between locations hubs in Australia:
| 		 | 	SYD 	 | 	MEL	 | 	ADL	 | 	ASP	 | 	BRI | 	DAR	 | 	PER	 |
| 	:-----:	 | 	:-----:	 | 	:-----:	 | 	:-----:	 | 	:-----:	 | 	:-----:	 | 	:-----:	 | 	:-----:	 |
| 	**SYD**	| 		| 	877	 | 	1376	| 	2762	| 	909	 | 	3935	| 	4016	 |
| 	**MEL**	| 	877	| 		 | 	725	 | 	2255	| 	1765	| 	3752	 | 	3509	|
| 	**ADL**	| 	1376	| 	725	 | 		| 	1530	| 	1927	 | 	3027	| 	2785	 |
| 	**ASP**	| 	2762	| 	2255	 | 	1530	| 		| 	2993	 | 	1497	| 	2481	 |
| 	**BRI**	| 	909	| 	1765	 | 	1927	| 	2993	| 		 | 	3426	| 	4311	 |
| 	**DAR**	| 	3935	| 	3752	 | 	3027	| 	1497	| 	3426	 | 		| 	4025	 |
| 	**PER**	| 	4016	| 	3509	 | 	2785	| 	2481	| 	4311	 | 	4025	| 		 |

The following **truck types** are available to be added as Truck with packages operating on a certain route:
| 		 | 	Scania 	 | 	Man	 | 	Actros |
| 	:-----:	 | 	:------:	 | 	:-----:	 | 	:-----:	 |
| 	Capacity	| 	42000 kg	| 	37000 kg	 | 	26000 kg	|
| 	Max Range (km)	| 	8000 km	| 	10000 km	 | 	13000 km	 |
| 	IDs	| 	1001-1010	| 	1011-1025	 | 	1026-1040	|


## Abbreviations:
&ensp;&ensp;&ensp;The following abbreviations are used for the location hubs:<br/>

    SYD = SYDNEY
    MEL = MELBOURNE
    ADL = ADELAIDE
    ASP = ALICE SPRINGS
    BRI = BRISBANE
    DAR = DARWIN 
    PER = PERTH 


## Example code with all functionality
```
CreatePackage BRI MEL 1500 Pesho,phone:0888777555
CreatePackage BRI SYD 11000 Olesya,phone:0888999777
FindRoute BRI MEL
CreateRoute BRI->SYD->MEL 2024-02-20 13:00
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
CreateRoute ASP->ADL->MEL->SYD->BRI 2024-02-20 12:00
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
```

# Use Cases

### Use Case #1

A customer visits the company office in Sydney on Oct 8th.
They bring a package that needs to be delivered to Melbourne. An employee of the company records the customer’s contact info, weighs the package at 45kg and then checks for a suitable delivery route.
The system reports that there are two routes:

- Brisbane (Oct 10th 06:00h) → Sydney (Oct 10th 20:00h) → Melbourne (Oct 11th 18:00h)

- Sydney (Oct 12th 06:00h) → Melbourne (Oct 12th 20:00h) → Adelaide (Oct 13th 15:00h)

Both routes' trucks have free capacity, and the employee suggests the first one, as the package will arrive one day earlier.
The customer agrees and the employee uses the system to add the delivery package to the first route and to update the package’s expected arrival time to Oct 11th 18:00h.
```
CreatePackage SYD MEL 45 AustralianCustomer1
FindRoute SYD MEL
CreateRoute SYD->MEL 2024-02-20 06:00
FindTruck 10000 SYD MEL
AddTruck Scania 1001 1
AddPackage 1 1
ViewSystem 0
```
### Use Case #2

Many packages with total weight of 23000kg have gathered in the hub in Alice Springs and an employee of the company uses the system to create a route that leaves on Sep 12th 06:00h with the following stops:

- Alice Springs → Adelaide → Melbourne → Sydney → Brisbane

The system determines the route distance to 4041km and calculates estimated arrival times for each of the locations based on a predefined average speed of 87km/h.
The employee then finds a free truck that meets the required range and capacity and proceeds to bulk assign the packages to the newly created route by using the route id and the packages’ ids.
```
CreatePackage ASP BRI 23000
CreateRoute ASP->ADL->MEL->SYD->BRI 2024-02-20 06:00
FindTruck 23000 ASP BRI
AddPackage 1 1
ViewSystem 0
```
### Use Case #3

A manager at the company uses the system to find information about all delivery routes in progress.
The system responds with information that contains each route’s stops, delivery weight, and the expected current stop based on the time of the day.
```
ViewSystem 0
```
### Use Case #4

A supervising employee uses the system to view information about each package that is not yet assigned to a delivery route.
The system responds with a list of packages containing their IDs and locations.
```
ViewNotAssigned
```
### Use Case #5

A customer contacts the office to request information about their package. The customer provides the id that they received when the package was created, and an employee enters the package id in the system. 
It responds with detailed information which is then emailed to the customer.
```
CreatePackage ASP BRI 2000 Zoya,phone:0888555888
CreatePackage ASP BRI 7000 Zoya,phone:0888555888
CreatePackage ASP BRI 10000 Zoya,phone:0888555888
CreatePackage ASP BRI 5000 Zoya,phone:0888555888
CreatePackage ASP ADL 800 KuKu,phone:0888678678
CreatePackage MEL BRI 1000 CarnivalKids,phone:0888567567
CreatePackage ADL SYD 2000 Bravo,phone:0888123456
ViewPackage 2
ViewPackage 4
ViewPackage 5
```

