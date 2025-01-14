from lms_app.apps import LmsAppConfig
from rest_framework.routers import DefaultRouter
from django.urls import path

from lms_app.services import (
    CreateProductAPIView,
    CreatePriceAPIView,
    CreateCheckoutSessionAPIView,
)
from lms_app.views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView,
    PaymentListAPIView,
    ManageSubscription,
)

app_name = LmsAppConfig.name

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="courses")
urlpatterns = [
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lesson/", LessonListAPIView.as_view(), name="lesson-list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson-view"),
    path(
        "lesson/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson-update"
    ),
    path(
        "lesson/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson-delete"
    ),
    path("payments/", PaymentListAPIView.as_view(), name="payment-list"),
    path(
        "manage-subscription/", ManageSubscription.as_view(), name="manage-subscription"
    ),
    path("create-product/", CreateProductAPIView.as_view(), name="create-product"),
    path("create-price/", CreatePriceAPIView.as_view(), name="create-price"),
    path(
        "create-checkout-session/",
        CreateCheckoutSessionAPIView.as_view(),
        name="create-checkout-session",
    ),
] + router.urls