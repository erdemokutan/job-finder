from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes  
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg,Min,Max,Count
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated

from .serializers import CandidatesAppliedSerializer, JobSerializer
from .models import CandidatesApplied, Job

from django.shortcuts import get_object_or_404
from .filters import JobsFilter

from django.utils import timezone
# Create your views here.

@api_view(['GET'])
def getAllJobs(request):

    filterset=JobsFilter(request.GET,queryset=Job.objects.all().order_by('id'))

    count=filterset.qs.count()

    #Pagination
    resPerPage=5
    paginator=PageNumberPagination()
    paginator.page_size=resPerPage

    queryset=paginator.paginate_queryset(filterset.qs,request)

    serializer=JobSerializer(queryset,many=True) #qs=queryset
    return Response({
        'count':count,
        'resPerPage':resPerPage,
        'jobs':serializer.data})


@api_view(['GET'])
def getJob(request,pk):
    job=get_object_or_404(Job,id=pk)

    serializer=JobSerializer(job,many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def newJob(request):
    request.data['user']=request.user
    data=request.data

    job=Job.objects.create(**data)

    serializer=JobSerializer(job,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateJob(request,pk):
    job=get_object_or_404(Job,id=pk)

    if job.user != request.user:
        return Response({'message':'You Can Not Update This Job!'},status=status.HTTP_403_FORBIDDEN)

    job.title=request.data['title']
    job.description=request.data['description']
    job.email=request.data['email']
    job.address=request.data['address']
    job.jobType=request.data['jobType']
    job.education=request.data['education']
    job.industry=request.data['industry']
    job.experience=request.data['experience']
    job.salary=request.data['salary']
    job.positions=request.data['positions']
    job.company=request.data['company']

    job.save()

    serializer=JobSerializer(job,many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteJob(request,pk):
    job=get_object_or_404(Job,id=pk)

    if job.user != request.user:
        return Response({'message':'You Can Not Delete This Job!'},status=status.HTTP_403_FORBIDDEN)

    job.delete()

    return Response({'message':'Job is Deleted Successfully!'},status=status.http_200_OK)


@api_view(['GET'])
def getTopicStats(request,topic):
    args={'title__icontains': topic}
    jobs=Job.objects.filter(**args)


    if len(jobs)== 0:
        return Response({'message':'Not stats found for {topic}'.format(topic=topic)})
    
    stats=jobs.aggregate(
        total_jobs=Count('title'),
        avg_positions=Avg('positions'),
        avg_salary=Avg('salary'),
        min_salary=Min('salary'),
        max_salary=Max('salary')

    )

    return Response(stats)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def applyToJob(request,pk):

    user=request.user
    job=get_object_or_404(Job,id=pk)

    if user.userprofile.resume=='':
        return Response({'error':'You Must Upload Your Resume First!'},status=status.HTTP_400_BAD_REQUEST)
    
    if job.deadline < timezone.now():
        return Response({'error':'You Can Not Apply This Job Because Deadline is Over!'},status=status.HTTP_400_BAD_REQUEST)
    
    alreadyApplied=job.candidatesapplied_set.filter(user=user).exists()

    if alreadyApplied:
        return Response({'error':'You Have Already Applied This Job!'},status=status.HTTP_400_BAD_REQUEST)
    
    jobApplied=CandidatesApplied.objects.create(
        job=job,
        user=user,
        resume=user.userprofile.resume

    )
    return Response({
        'applied':True,
        'job_id':jobApplied.id
    },status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCurrentUserAppliedJobs(request):

    args={'user_id':request.user.id}
    jobs=CandidatesApplied.objects.filter(**args)

    serializer=CandidatesAppliedSerializer(jobs,many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def isApplied(request,pk):

    user=request.user
    job=get_object_or_404(Job,id=pk)

    applied=job.candidatesapplied_set.filter(user=user).exists()
    
    return Response(applied)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCurrentUserJobs(request):

    args={'user':request.user.id}
    jobs=Job.objects.filter(**args)
    serializer=JobSerializer(jobs,many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCandidatesApplied(request,pk):

    user=request.user
    job=get_object_or_404(Job,id=pk)

    if job.user !=user:
        return Response({'error':'You Can Not Access This Job!'},status=status.HTTP_403_FORBIDDEN)
    
    candidates=job.candidatesapplied_set.all()

    serializer=CandidatesAppliedSerializer(candidates,many=True)

    return Response(serializer.data)