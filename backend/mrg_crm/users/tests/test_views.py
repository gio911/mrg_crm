from .test_setup import TestSetUp
import pdb

class TestViews(TestSetUp):

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_correctly(self):
        res = self.client.post(self.register_url, self.user_data, format='json')
        # pdb.set_trace()
        self.assertEqual(res.status_code, 201)
