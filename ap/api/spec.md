# API endpoint spec

root url: `/api`

request semantics (from http://codeplanet.io/principles-good-restful-api-design/):
`GET` (`SELECT`): Retrieve a specific Resource from the Server, or a listing of Resources.
`POST` (`CREATE`): Create a new Resource on the Server.
`PUT` (`UPDATE`): Update a Resource on the Server, providing the entire Resource.
`PATCH` (`UPDATE`): Update a Resource on the Server, providing only changed attributes.
`DELETE` (`DELETE`): Remove a Resource from the Server.

return full resource for every request

## trainees
(for trainee autocomplete)

`GET` one trainee:
`/trainees/[pk]`

`GET` all trainees:
`/trainees`

`GET` all active trainees:
`/trainees/active`

`GET` trainees by gender:
`/trainees/gender/[m/f]` or `[b/s]`

`GET` trainees by term:
`/trainees/term/[1-4]`

`GET` trainees by house:
`/trainees/house/[pk]`

`GET` trainees by team:
`/trainees/team/[pk]` or `[team-code]` (e.g. 'ANA-COM' or 'I-YP')

`GET` trainess by team type:
`/trainees/teamtype/[type]` (e.g. 'CAMPUS' or 'YP')

`GET` house coordinators:
`/trainees/HC`

## schedules, attendance, leaveslips
(for attendance views)

`GET` `PUT` `PATCH` one schedule, with all its events:
`/schedules/[pk]`

`GET` one trainee's schedules:
`/schedules/trainee/[pk]`

`GET` `PUT` `PATCH` one event:
`/events/[pk]`

`GET` one event's rolls:
`/events/[pk]/rolls`

`GET` `POST` `PUT` `PATCH` one roll:
`/rolls/[pk]`

`GET` `PUT` `PATCH` one trainee's rolls:
`/rolls/trainee/[pk]`

## services, workers, etc.
(for service scheduler)
