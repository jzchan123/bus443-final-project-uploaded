from django.shortcuts import render
from django.http import HttpResponse
from faculty.models import Facultydetails
from django.db import connection
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
	context = {'name':'Jeffrey'}
	return render(request, 'faculty/home.html', context)

def savedata(request):
	if('fname' and 'lname' and 'cid' and 'cdesc' in request.GET):
		fname = request.GET.get('fname')
		lname = request.GET.get('lname')
		cid = int(request.GET.get('cid'))
		cdesc = request.GET.get('cdesc')
		adddata = Facultydetails(firstname = fname, lastname = lname, courseid = cid, coursedescription = cdesc)
		adddata.save()
		return HttpResponse('Success')

@login_required
def about(request):
	return HttpResponse('<h2>about us page</h2>')


def dictfetchall(cursor):
	#"returns all rows from a cursor as a dict"
	columns = [col[0] for col in cursor.description]
	return [
		dict(zip(columns,row))
		for row in cursor.fetchall()]


@login_required
def facultyinfo(request):
	facultydata = Facultydetails.objects.all()
	paginator = Paginator(facultydata, 10 ) 
	page = request.GET.get('page')
	facultyminiset = paginator.get_page(page)



	#facultydata = Facultydetails.objects.filter(firstname = "enternamehere")
#	print(facultydata[0].__dict__)
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM FACULTY_FACULTYDETAILS")
#	facultydata = dictfetchall(cursor)
#	print(facultydata)
	return render(request, 'faculty/details.html', {'data':facultyminiset})
	