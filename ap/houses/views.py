from django.shortcuts import render
from houses.models import House, Room, BedFrameType, MattressType, Bunk 

import os
import csv
import re

def import_bunks(request):
    file_path = os.path.join(os.path.dirname(__file__), 'Bunks.csv')
    header = []
    log = []
    count = 0
#     with open(file_path, 'rb') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#         last_residence=''
#         last_room_type=None
#         room=None
#         house=None
#         room_cap=0
#         for row in reader:
#             if count==0:
#                 header=row
#             else:
#                 if len(row)>9:
#                     residence=row[1]
#                     if residence!=last_residence:
#                         last_residence=residence
#                         house=None
#                         room_cap=0
#                         try:
#                             house=House.objects.get(name=residence);
#                         except House.DoesNotExist:
#                             try:
#                                 house=House.objects.get(name=re.sub(r"\d+\s*","",residence));
#                             except House.DoesNotExist:
#                                 log.append("Cannot find House for "+residence+"!");
#                                 continue;
#                     if house is None:
#                         continue
#                      
#                     room_type=row[9]
#                     if room_type!=last_room_type:
#                         last_room_type=room_type
#                         room_cap=0
#                     if room_type=='Double room' or room_type=='Couple':
#                         if room_cap % 2 == 0:
#                             room=Room(type='BED',capacity=2,house=house)
#                             room.save()
#                             room_cap=0
#                         room_cap+=1
#                     elif room_type=='Triple room':
#                         if room_cap % 3 == 0:
#                             room=Room(type='BED',capacity=3,house=house)
#                             room.save()
#                             room_cap=0
#                         room_cap+=1
#                     elif room_type=='Single room':
#                         room=Room(type='BED',capacity=1,house=house)
#                         room.save()
#                         room_cap=0
#                     for_trainees=True if row[6]=='Yes' else False
#                     has_protector=True if row[13]=='1' else False
#                      
#                     try:
#                         bed_frame_type = BedFrameType.objects.get(name=row[11])
#                     except BedFrameType.DoesNotExist:
#                         if row[11]!='':
#                             log.append("Row #"+str(count+1)+" has invalid bed frame type: "+row[11])
#                         bed_frame_type = None
#                     try:
#                         mattress_type = MattressType.objects.get(name=row[12])
#                     except MattressType.DoesNotExist:
#                         mattress_type = None
#                     length='L' if row[5]=='Long' else 'R'
#                     bunk_no=int(row[2])
#                     if row[7]=='1':
#                         position='S'
#                     elif row[3]=='Bottom':
#                         position='B'
#                     elif row[3]=='Queen-A':
#                         position='Q'
#                     elif row[3]=='Queen-B':
#                         position='q'
#                     else:
#                         position='T'
#                     notes = row[10]
#                      
#                     other_no=int(row[4])
#                      
#                     if position=='T' or position=='q':
#                         other_bunk=Bunk.objects.get(room__house=house,number=other_no)
#                         room=other_bunk.room;
#                     else:
#                         other_bunk=None
# #                     try:
# #                         other_bunk=Bunk.objects.get(room=room,number=other_no);
# #                     except Bunk.DoesNotExist:
# #                         other_bunk=None
# #                     except Bunk.MultipleObjectsReturned:
# #                         other_bunk=None
# #                         log.append("MULT: "+str(row))
# #                         continue;
#                     bunk = Bunk(for_trainees=for_trainees,
#                                 has_protector=has_protector,
#                                 bed_frame_type=bed_frame_type,
#                                 mattress_type=mattress_type,
#                                 length=length,
#                                 number=bunk_no,
#                                 position=position,
#                                 link=other_bunk,
#                                 room=room,
#                                 notes=notes)
#                     bunk.save()
#                     if not other_bunk is None:
#                         other_bunk.link=bunk
#                         other_bunk.save()
#             count=count+1
            
            
    data = {'import_results': str(header)+"\n"+"\n".join(log)}
    return render(request, 'houses/import.html', dictionary=data)