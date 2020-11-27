import os

from nodes import BranchNode, LeafNode

belarus = BranchNode('Belarus')

hrodna_reg = BranchNode('Hrodna region')
minsk_reg = BranchNode('Minsk region')

hrodna_city = BranchNode('Hrodna')
shchuchin_city = BranchNode('Schuchin')

lenin_district = BranchNode('Lenin District')

b_troickaya_st = BranchNode('Bolshaya Troitskaya st.')
sovetskaya_st = BranchNode('Sovetskaya st.')

b_troickaya_st_4 = BranchNode('4')
sovetskaya_st_4 = BranchNode('4')

b_troickaya_st_4_1st_floor = BranchNode('1st floor')
b_troickaya_st_4_2nd_floor = BranchNode('2nd floor')
sovetskaya_st_4_1st_floor = BranchNode('1st floor')

b_troickaya_st_4_1st_floor_4th_office = BranchNode('Office 4')
b_troickaya_st_4_1st_floor_6th_office = BranchNode('Office 6')
sovetskaya_st_4_1st_floor_2nd_office = BranchNode('Office 2')

b_troickaya_st_4_1st_floor_4th_office_4th_sensor = LeafNode('Sensor 4')
b_troickaya_st_4_1st_floor_4th_office_5th_sensor = LeafNode('Sensor 5')
b_troickaya_st_4_1st_floor_6th_office_1st_sensor = LeafNode('Sensor 1')
sovetskaya_st_4_1st_floor_2nd_office_1st_sensor = LeafNode('Sensor 1')

b_troickaya_st_4_1st_floor_4th_office.add(b_troickaya_st_4_1st_floor_4th_office_4th_sensor)
b_troickaya_st_4_1st_floor_4th_office.add(b_troickaya_st_4_1st_floor_4th_office_5th_sensor)
b_troickaya_st_4_1st_floor_6th_office.add(b_troickaya_st_4_1st_floor_6th_office_1st_sensor)
sovetskaya_st_4_1st_floor_2nd_office.add(sovetskaya_st_4_1st_floor_2nd_office_1st_sensor)

b_troickaya_st_4_1st_floor.add(b_troickaya_st_4_1st_floor_4th_office)
b_troickaya_st_4_1st_floor.add(b_troickaya_st_4_1st_floor_6th_office)
sovetskaya_st_4_1st_floor.add(sovetskaya_st_4_1st_floor_2nd_office)

b_troickaya_st_4.add(b_troickaya_st_4_1st_floor)
b_troickaya_st_4.add(b_troickaya_st_4_2nd_floor)
sovetskaya_st_4.add(sovetskaya_st_4_1st_floor)

b_troickaya_st.add(b_troickaya_st_4)
sovetskaya_st.add(sovetskaya_st_4)

lenin_district.add(b_troickaya_st)
lenin_district.add(sovetskaya_st)

hrodna_city.add(lenin_district)

hrodna_reg.add(hrodna_city)
hrodna_reg.add(shchuchin_city)

belarus.add(hrodna_reg)
belarus.add(minsk_reg)

search_hrodna = belarus.search('Hrodna')
search_4 = belarus.search('4')
search_sensor_1 = belarus.search('Sensor 1')
search_sensor_3 = belarus.search('Sensor 3')

belarus_show = belarus.show()
hrodna_show = hrodna_city.show()

print(search_hrodna)
print(search_4)
print(search_sensor_1)
print(search_sensor_3)
print(os.path.basename(str(search_sensor_1[0])))

print('\n\n\n')
print(belarus_show)
print('\n\n\n')
print(hrodna_show)

