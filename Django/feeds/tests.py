from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Feed
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class FeedAPITestCase(APITestCase):
		# setUp 메서드는 각 테스트 메서드가 실행되기 전에 호출
    def setUp(self):
				# 테스트용 사용자에 대한 JWT 토큰 생성
        self.user = User.objects.create_user(username='testuser', password='password')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.feed1 = Feed.objects.create(user=self.user, content='Test Feed 1')
        self.feed2 = Feed.objects.create(user=self.user, content='Test Feed 2')

    def test_get_all_feeds(self):
        url = reverse('all_feeds')  # 'all_feeds'는 url 패턴 이름입니다.
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)  # 2개의 피드가 반환되어야 합니다.

    def test_get_feed_detail(self):
        url = reverse('feed_detail', kwargs={'feed_id': 1})  # 'user_feeds'는 url 패턴 이름입니다.
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['title'], self.feed1.content)
        # self.assertEqual(len(response.data), 2)  # 해당 유저의 2개 피드가 반환되어야 합니다.
    
    def test_create_feed(self):
        self.client.login(username='testuser', password='password')
        url = reverse('all_feeds')  # 'feeds'는 URL 패턴 이름입니다.
        data = {'content': 'New Feed','title':'New Title'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Feed.objects.count(), 3)  # 게시글 수가 3개여야 합니다.
        self.assertEqual(Feed.objects.latest('id').content, 'New Feed')