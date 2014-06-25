from tastypie import fields, utils
from tastypie.resources import ModelResource
from tastypie.validation import Validation, CleanedDataFormValidation
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization


from leaveslips.models import LeaveSlip, IndividualSlip, GroupSlip, MealOutSlip, NightOutSlip, IndividualSlipForm
from schedules.models import Event
from accounts.models import Profile, User, Trainee, TrainingAssistant


''' leaveslip_api resources.py

All the API resources for leaveslips. For each model, GET, POST, and PUT are supported.

See schemas.txt for sample formats.

'''

# Custom validation of POST and PUT requests
class LeaveSlipValidation(Validation):
	def is_valid(self, bundle, request=None):
		if not bundle.data:
			return {'__all__': 'Missing leaveslip data.'}

		# bundle.data['TA']
		# print bundle.data
		# print bundle.request.user

		trainee = Profile.get_trainee(User.objects.get(email=bundle.request.user).id)
		bundle.data['TA'] = trainee.TA
		bundle.data['status'] = 'P'
		print bundle.data
		return super(LeaveSlipValidation, self).is_valid(bundle, request)

class TraineeResource(ModelResource):
	class Meta:
		authorization = Authorization()
		queryset = Trainee.objects.all()
        resource_name = 'trainee'


class TrainingAssistantResource(ModelResource):
	class Meta:
		authorization = Authorization()
		queryset = TrainingAssistant.objects.all()
		resource_name = 'TA'
		

class IndividualSlipResource(ModelResource):
	trainee = fields.ForeignKey(TraineeResource, 'trainee')
	TA = fields.ForeignKey(TrainingAssistantResource, 'TA')

	class Meta:
		queryset = IndividualSlip.objects.all()
		allowed_methods = ['get', 'post', 'put']
		authentication = BasicAuthentication()
		authorization = Authorization()
		form = CleanedDataFormValidation(form_class=IndividualSlipForm)

	# Adding the event information to the returned data without creating an event resource
	# data returned can be customized here
	def dehydrate(self, bundle):
		bundle.data['events'] = IndividualSlip.objects.get(pk=bundle.data['id']).events.all()
		print bundle.data['events']
		return bundle



class MealOutSlipResource(ModelResource):
	leaveslip = fields.OneToOneField(IndividualSlipResource, 'leaveslip', null=False, full=True)

	class Meta:
		queryset = MealOutSlip.objects.all()
		allowed_methods = ['get', 'post', 'put']

class NightOutSlipResource(ModelResource):
	leaveslip = fields.OneToOneField(IndividualSlipResource, 'leaveslip', null=False, full=True)

	class Meta:
		queryset = NightOutSlip.objects.all()
		allowed_methods = ['get', 'post', 'put']

class GroupSlipResource(ModelResource):
	class Meta:
		queryset = GroupSlip.objects.all()
		allowed_methods = ['get', 'post', 'put']
