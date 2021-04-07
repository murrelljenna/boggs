from apps.tenant_db import models, serializers
from rest_framework import viewsets, status
from rest_framework.routers import DefaultRouter
from django.http import JsonResponse

class CallEffortAPIView(viewsets.ViewSet):
    def create(self, request):
        serializer = serializers.CallEffortSerializer(data=request.data)
        if serializer.is_valid():
            activities = []

            contacts = models.Contact.objects.all()

            if 'address' in self.request.query_params:
                contacts = contacts.filter(
                    address__id=self.request.query_params['address']
                )

            for contact in contacts:
                activity = models.Activity.objects.create(
                    contact=contact,
                    code="CALL",
                    status="TODO",
                )

                models.CallEffortActivity.objects.create(
                    call_effort=serializer.save(),
                    activity=activity
                )
                activities.append(serializers.ActivitySerializer(activity).data)

            return JsonResponse(activities, safe=False, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        queryset = Activities.objects.filter(calleffortactivity__call_effort__id=pk)


router = DefaultRouter()
router.register(r'efforts/calls', CallEffortAPIView, basename='CallEffort')

urlpatterns = router.urls
