from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer
from reviews.serializers import ReviewSerializer

class FeedSerializer(ModelSerializer):
    user = FeedUserSerializer(read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta: ## 모델이나 폼에 대한 부가적인 정보를 제공한다. (테이블 이름, 정렬, 권한 설정 등에 영향을 미친다.)
        model = Feed
        fields = "__all__"
        # depth = 1 ## user 정보의 상세 조회
