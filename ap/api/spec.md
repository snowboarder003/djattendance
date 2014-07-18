# API endpoint spec

root url: `/api`

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
`/trainees/team/[type]` (e.g. 'CAMPUS' or 'YP')

`GET` house coordinators:
`/trainees/HC`

## schedules, attendance, leaveslips
(for attendance views)



## services, workers, etc.
(for service scheduler)
