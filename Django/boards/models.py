from django.db import models
from common.models import CommonModel

# Create your models here.

# 게시글
# - title
# - content
# 하나의 모델을 만들때는 Board 라는 단수 사용!
class Board(CommonModel):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveBigIntegerField(default=0)
    reviews = models.PositiveBigIntegerField(default=0)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)  ## 유저라는 데이터를 보드에서 가져온다.  -> on_delete=models.CASCADE 는 유저데이터 삭제시 게시글(보드) 데이터 삭제 하냐? -> CASCADE 는 삭제해라!

    def __str__(self):
        return self.title