select
	p.DisplayName as [AthleteName],
	c.DisplayName as [Regatta],
	ct.DisplayName as [CompetitionType],
	cc.DisplayName as [CategoryType],
	v.DisplayName as [Venue],
	e.DisplayName as [Event],
	r.DisplayName as [Race],
	rp.DisplayName as [Phase],
	r.[Date] as [RaceDate],
	rb.Lane as [Lane],
	rb.[Rank] as [Rank],
	rb.ResultTime as [ResultTime]
from Competition c
inner join [Event] e on e.competitionId = c.id
inner join [Venue] v on v.id = c.venueId
inner join [Race] r on r.eventId = e.id
inner join [RacePhase] rp on r.racePhaseId = rp.racePhaseId
inner join [RaceBoat] rb on rb.raceId = r.id
inner join [RaceBoatAthlete] rba on rba.raceBoatId = rb.id
inner join [Person] p on p.id = rba.personId
inner join [BoatClass] bc on bc.boatClassId = e.boatClassId

inner join [CompetitionType] ct on ct.id = c.competitionTypeId
inner join [CompetitionTypeCompetitionCategoryAssociation] ctcca on ctcca.CompetitionTypeId = ct.id
inner join [CompetitionCategory] cc on cc.id = ctcca.CompetitionCategoryId
where p.LastName = 'Peszek'
order by c.DisplayName, r.[Date]