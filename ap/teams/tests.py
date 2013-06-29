from django.test import TestCase
from teams.models import Team


class TeamTest(TestCase):
    def setUp(self):
        Team.objects.create(name="ucla", code="UCLA-CAMP", type="CAMPUS")
        Team.objects.create(name="Anaheim", code="ANA-CHILD", type="CHILD")
        Team.objects.create(name="Irvine", code="I-COM", type="COM")
        Team.objects.create(name="LB", code="LB-YP", type="YP")
        Team.objects.create(name="BFA", code="I-BFA", type="I")

    def test_team_can_speak(self):
        """ Team objects that can speak are correctly identified """
        t = Team.objects.get(name="ucla")
        u = Team.objects.get(name="Anaheim")
        v = Team.objects.get(name="Irvine")
        w = Team.objects.get(name="LB")
        x = Team.objects.get(name="BFA")
        self.assertEqual("CAMPUS", t.type)
        self.assertEqual("CHILD", u.type)
        self.assertEqual("COM", v.type)
        self.assertEqual("YP", w.type)
        self.assertEqual("I", x.type)
