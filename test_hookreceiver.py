import unittest
import hookreceiver
from os import environ

class HookreceiverTestCase(unittest.TestCase):

    def setUp(self):
        self.app = hookreceiver.app.test_client()

    def test_bb_example_post(self):
        data = """
{
    "canon_url": "https://bitbucket.org",
    "commits": [
        {
            "author": "marcus",
            "branch": "master",
            "files": [
                {
                    "file": "somefile.py",
                    "type": "modified"
                }
            ],
            "message": "Added some more things to somefile.py",
            "node": "620ade18607a",
            "parents": [
                "702c70160afc"
            ],
            "raw_author": "Marcus Bertrand <marcus@somedomain.com>",
            "raw_node": "620ade18607ac42d872b568bb92acaa9a28620e9",
            "revision": null,
            "size": -1,
            "timestamp": "2012-05-30 05:58:56",
            "utctimestamp": "2012-05-30 03:58:56+00:00"
        }
    ],
    "repository": {
        "absolute_url": "/marcus/project-x/",
        "fork": false,
        "is_private": true,
        "name": "Project X",
        "owner": "marcus",
        "scm": "git",
        "slug": "project-x",
        "website": "https://atlassian.com/"
    },
    "user": "marcus"
}"""
        rv = self.app.post('/repo/demo_repo/123', 
                data=data, 
                content_type='application/json', 
        )
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.data, 'processed 1 commits')

if __name__ == '__main__':
    unittest.main()
