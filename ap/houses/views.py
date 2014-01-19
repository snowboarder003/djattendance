from django.shortcuts import render
from houses.models import House, Room, BedFrameType, MattressType, Bunk
from accounts.models import Trainee
import django_tables2 as tables
from django import forms

from django.db import models

#import_bunks dependencies
import os
import csv

class HouseTable(tables.Table):
    house=tables.Column()
    gender=tables.Column()
    bottom=tables.Column()
    top=tables.Column()
    couple=tables.Column()
    link=tables.LinkColumn('houses.views.bunk_selector', args=(tables.utils.A('pk'),))

def CompareBunk(bunk1,bunk2):
    num1=min(bunk1.number,bunk1.link.number)
    num2=min(bunk2.number,bunk2.link.number)
    if num1!=num2:
        return num1-num2
    else:
        return bunk1.number-bunk2.number

class BunkTraineeForm(forms.Form):
    bunk=forms.ModelChoiceField(queryset=Bunk.objects.filter(for_trainees=True),widget=forms.HiddenInput())
    trainee=forms.ModelChoiceField(queryset=Trainee.objects.filter(active=True).order_by('account__lastname','account__firstname'),required=False, 
        widget=forms.Select(attrs={"onChange":'submit()'}))

def bunk_selector(request,house__pk):
    log = []
    if request.method == 'POST': # If the form has been submitted...
        #log.append(str(request.POST));
        form = BunkTraineeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            try:
                bunk = form.cleaned_data['bunk']
                for trainee in Trainee.objects.filter(active=True,bunk=bunk):
                    trainee.bunk=None;
                    trainee.save();
                trainee = form.cleaned_data['trainee']
                if not trainee is None:
                    trainee.bunk = bunk;
                    trainee.save()
            except Trainee.DoesNotExist:
                log.append("Invalid Trainee ID");
            #log.append("Valid form post");
    
    if house__pk is None or house__pk=='':
        list = (Trainee.objects.filter(account__gender='B',bunk__isnull=True,spouse__isnull=True),
                Trainee.objects.filter(account__gender='S',bunk__isnull=True,spouse__isnull=True),
                Trainee.objects.filter(bunk__isnull=True,spouse__isnull=False))
        log.append(str(list))
        house_data=[]
        for house in House.objects.filter(used=True):
            house_data.append({'house':house.name,
                'gender':house.get_gender_display(),
                'bottom':str(house.empty_bunk_count(['B'])),
                'top':str(house.empty_bunk_count(['T'])),
                'couple':str(house.empty_bunk_count(['q','Q'])),
                'link':'edit',
                'pk':house.pk})
        house_table=HouseTable(house_data)
        tables.RequestConfig(request,paginate=None).configure(house_table)
        data = {'import_results': "\n".join(log),
                'houses':house_table}
        return render(request, 'houses/index.html', dictionary=data)
    else:
        try:
            house=House.objects.get(pk=house__pk)
            rooms_with_bunks = []
            for room in Room.objects.filter(house=house).annotate(min_bunk=models.Min('bunk__number')).order_by('min_bunk'):
                bunks = sorted(Bunk.objects.filter(room=room,for_trainees=True).prefetch_related('link'), cmp=CompareBunk)
                bunk_list=[]
                for bunk in bunks:
                    try:
                        trainee=Trainee.objects.get(bunk=bunk)
                        bunk_list.append((bunk,BunkTraineeForm(initial={'bunk':bunk.id,'trainee':trainee.id})))
                    except Trainee.DoesNotExist:
                        bunk_list.append((bunk,BunkTraineeForm(initial={'bunk':bunk.id})))
                rooms_with_bunks.append((room,bunk_list))
        except House.DoesNotExist:
            None
        data = {'house':house,
            'room_list':rooms_with_bunks,
            'import_results': "\n".join(log)}
        return render(request, 'houses/bunk_table.html', dictionary=data)


def import_bunks(request):
    file_path = os.path.join(os.path.dirname(__file__), 'Bunks.csv')
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