from django.test import TestCase, Client
from .models import Student

# Create your tests here.
class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='lqk111',
            sex=1,
            email='dfsaf@qq.com',
            profession='IT',
            qq='32434234234',
            phone='3432423432',
        )

    def  test_create_and_sex_show(self):
        student = Student.objects.create(
            name = 'huyang',
            sex =1,
            email='23432423@qq.com',
            profession='IT',
            qq='3432432432',
            phone='2143242',
        )
        self.assertEqual(student.sex_show,'男','性别字段内容跟展示不一致！')

    def test_filter(self):
        Student.objects.create(
            name='huyang',
            sex=1,
            email='23432423@qq.com',
            profession='IT',
            qq='3432432432',
            phone='2143242',
        )
        name = 'lqk222',
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(),1,'应该只存在一个名称为{}的记录'.format(name))

    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code,200, 'status code must bu 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name = 'test_for_post',
            sex =1,
            email='32432423@qq.com',
            profession='文员',
            qq='23432432',
            phone='23432432423',
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code,302,'status code must be 302!')

        response = client.get('/')
        self.assertTrue(b'test_for_post' in response.content,'response content must contain `test_for_post`')

