from django.shortcuts import render
from tasks.models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        task = self.get_object()
        status = request.data.get('status')
        if status:
            task.status = status
            task.save()
            return Response({'status': 'status updated'})
        else:
            return Response({'status': 'no status provided'}, status=400)

    @action(detail=True, methods=['post'])
    def toggle_planned(self, request, pk=None):
        task = self.get_object()
        task.planned = not task.planned
        task.save()
        return Response({'planned': task.planned})

    @action(detail=True, methods=['post'])
    def set_plan_order(self, request, pk=None):
        task = self.get_object()
        plan_order = request.data.get('plan_order')
        if plan_order is not None:
            task.plan_order = plan_order
            task.save()
            return Response({'plan_order': task.plan_order})
        else:
            return Response({'status': 'no plan order provided'}, status=400)

    @action(detail=False, methods=['get'])
    def get_planned_tasks(self, request):
        planned_tasks = Task.objects.filter(planned=True).order_by('plan_order')
        serializer = self.get_serializer(planned_tasks, many=True)
        return Response(serializer.data)