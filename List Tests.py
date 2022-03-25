nasdtec_list_raw = '''
Alabama 26. Minnesota
2. Alaska 27. Mississippi
3. Arizona 28. Missouri
4. Arkansas 29. Montana
5. California 30. Nebraska
6. Colorado 31. Nevada
7. Connecticut 32. New Hampshire
8. Delaware 33. New Jersey
9. District of Columbia 34. New York
10. DODEA 35. North Carolina
11. Florida 36. North Dakota
12. Georgia 37. Ohio
13. Guam 38. Oklahoma
14. Hawaii 39. Oregon
15. Idaho 40. Pennsylvania
16. Illinois 41. Rhode Island
17. Indiana 42. South Carolina
18. Iowa 43. Tennessee
19. Kansas 44. Texas
20. Kentucky 45. Utah
21. Louisiana 46. Vermont
22. Maine 47. Virginia
23. Maryland 48. Washington
24. Massachusetts 49. West Virginia
25. Michigan 50. Wisconsin
51. Wyoming'''.lower()

state_list = '''
Alabama
.Alaska
.Arizona
.Arkansas
.California
.Colorado
.Connecticut
.Delaware
.Florida
.Georgia
.Hawaii
.Idaho
.Illinois
.Indiana
.Iowa
.Kansas
.Kentucky
.Louisiana
.Maine
.Maryland
.Massachusetts
.Michigan
.Minnesota
.Mississippi
.Missouri
.Montana
.Nebraska
.Nevada
.New Hampshire
.New Jersey
.New Mexico
.New York
.North Carolina
.North Dakota
.Ohio
.Oklahoma
.Oregon
.Pennsylvania
.Rhode Island
.South Carolina
.South Dakota
.Tennessee
.Texas
.Utah
.Vermont
.Virginia
.Washington
.West Virginia
.Wisconsin
.Wyoming
'''.lower().split('.')

nasdtec_list_clean = ''.join([i for i in nasdtec_list_raw if not i.isdigit()]).split('.')

for i in nasdtec_list_clean:
    ap = i.strip()
    nasdtec_list_clean[nasdtec_list_clean.index(i)] = ap

for i in state_list:
    sa = i.strip()
    state_list[state_list.index(i)] = sa

for i in state_list:
    if i not in nasdtec_list_clean:
        print(f'{i.title()} is not in the NASDTEC agreement and you would have to get recertified there.')








