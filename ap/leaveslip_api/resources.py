from tastypie import fields, utils
from tastypie.resources import ModelResource
from tastypie.validation import Validation
from tastypie.authorization import Authorization


from leaveslips.models import LeaveSlip, IndividualSlip, GroupSlip, MealOutSlip, NightOutSlip
from schedules.models import Event
from accounts.models import Profile


''' leaveslip_api resources.py

All the API resources for leaveslips. For each model, GET, POST, and PUT are supported.

See schemas.txt for sample formats.

'''

# Custom validation of POST and PUT requests
class LeaveSlipValidation(Validation):
	def is_valid(self, bundle, request=None):
		print bundle
		errors = {}
		if not bundle.data:
			return {'__all__': 'Missing leaveslip data.'}

		# bundle.data['TA']	
		return errors
  #       for key, value in bundle.data.items():
  #           if not isinstance(value, basestring):
  #               continue
		# return errors # + super().is_valid(self, bundle, request)


class IndividualSlipResource(ModelResource):
	
	class Meta:
		queryset = IndividualSlip.objects.all()
		allowed_methods = ['get', 'post', 'put']
		authorization = Authorization()
		validation = LeaveSlipValidation()

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
        authorization = Authorization()

class NightOutSlipResource(ModelResource):
	leaveslip = fields.OneToOneField(IndividualSlipResource, 'leaveslip', null=False, full=True)

	class Meta:
		queryset = NightOutSlip.objects.all()
		allowed_methods = ['get', 'post', 'put']
        authorization = Authorization()

class GroupSlipResource(ModelResource):
	class Meta:
		queryset = GroupSlip.objects.all()
		allowed_methods = ['get', 'post', 'put']
		authorization = Authorization()