from django import template

register = template.Library()


@register.filter(name='lookup')
def lookup(d, key):
    return d[key]

# returns true if the user has responded to this question
# This is probably more sophisticated than we need right now--really if we
# just provided the for loop counter and indexed into responses, we'd probably
# be fine, but it's possible that the responses would be provided in a 
# different order or that not every question will have a response in the future, 
# so it seems safer to be explicit here.  Similarly for response.
@register.filter(name='has_response')
def has_response(responses, question_id):
	# todo(haileyl): this should call response instead of duplicating code.
	for response in responses:
		if response.question_id == question_id and len(response.body) > 0:
			return True
	return False

# returns the text string response
@register.filter(name='response')
def response(responses, question_id):
	for response in responses:
		if response.question_id == question_id:
			return response.body
	return None

# returns id for span given the question
@register.filter(name='spanid')
def spanid(question):
	return "count" + str(question.id)

register.filter('lookup', lookup)
register.filter('has_response', has_response)
register.filter('response', response)
register.filter('spanid', spanid)