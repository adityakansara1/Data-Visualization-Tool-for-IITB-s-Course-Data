from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from LoginRegister.models import courseData
import plotly.graph_objects as go
from django.contrib import messages

# Create your views here.
@login_required(login_url='/login/')
def yearWiseComparison(request):
    if(request.method == "POST"):
        course_code = request.POST['course_code']
        semester = request.POST['semester']
        courseData_objects = courseData.objects.filter(course_code=course_code, sem=semester)
        if(courseData_objects.count() == 0):
            messages.info(request, 'No data found for the given course code and semester')
            return redirect('/plots/yearWiseComparison/')
        else:    
            line = go.Figure()
            line.add_trace(go.Scatter(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('total', flat=True)), mode='lines+markers', name=course_code))                    
            line.update_layout(title_text='Total Students vs Year', xaxis_title='Year', yaxis_title='Total Students')
            line = line.to_html(full_html=False, default_height=500, default_width=700)

            bar = go.Figure()
            bar.add_trace(go.Bar(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('grade_AA', flat=True)), name="Grade AA"))
            bar.add_trace(go.Bar(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('grade_AB', flat=True)), name="Grade AB"))
            bar.add_trace(go.Bar(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('grade_BB', flat=True)), name="Grade BB"))
            bar.add_trace(go.Bar(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('grade_BC', flat=True)), name="Grade BC"))
            bar.add_trace(go.Bar(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('grade_CC', flat=True)), name="Grade CC"))
            bar.add_trace(go.Bar(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('grade_CD', flat=True)), name="Grade CD"))
            bar.add_trace(go.Bar(x=list(courseData_objects.values_list('year', flat=True)), y=list(courseData_objects.values_list('grade_DD', flat=True)), name="Grade DD"))
            bar.update_layout(title_text='Grade vs Year', xaxis_title='Year', yaxis_title='Grade')
            bar = bar.to_html(full_html=False, default_height=500, default_width=700)

            return render(request, 'yearWiseComparison.html', context={'line': line, 'bar': bar})

    else:
        courseData_objects = courseData.objects.values_list('course_code', flat=True).distinct().order_by('course_code')
        return render(request, 'yearWiseComparison.html', context={'courseData_objects': courseData_objects})
    
@login_required(login_url='/login/')
def courseWiseComparison(request):
    if(request.method == "POST"):
        course_code1 = request.POST['course_code1']
        course_code2 = request.POST['course_code2']
        semester = request.POST['semester']
        courseData_objects1 = courseData.objects.filter(
            course_code=course_code1, sem=semester)
        courseData_objects2 = courseData.objects.filter(
            course_code=course_code2, sem=semester)
        if(courseData_objects1.count() == 0 or courseData_objects2.count() == 0):
            messages.info(request, 'No data found for the given course code')
            return redirect('/plots/courseWiseComparison/')
        else:
            fig = go.Figure()
            fig1 = go.Figure()
            fig2 = go.Figure()

            fig.add_trace(go.Scatter(x=list(courseData_objects1.values_list('year', flat=True)), y=list(
                courseData_objects1.values_list('total', flat=True)), mode='lines+markers', name=course_code1))
            fig.add_trace(go.Scatter(x=list(courseData_objects2.values_list('year', flat=True)), y=list(
                courseData_objects2.values_list('total', flat=True)), mode='lines+markers', name=course_code2))
            fig.update_layout(title_text='Total Students vs Year',
                              xaxis_title='Year', yaxis_title='Total Students')
            fig = fig.to_html(
                full_html=False, default_height=500, default_width=700)

            course1_gradeAA = list(
                courseData_objects1.values_list('grade_AA', flat=True))
            course1_gradeBB = list(
                courseData_objects1.values_list('grade_BB', flat=True))
            course1_gradeCC = list(
                courseData_objects1.values_list('grade_CC', flat=True))
            course1_gradeDD = list(
                courseData_objects1.values_list('grade_DD', flat=True))
            fig1.add_trace(go.Bar(x=list(courseData_objects1.values_list(
                'year', flat=True)), y=course1_gradeAA, name='AA', marker_color='green'))
            fig1.add_trace(go.Bar(x=list(courseData_objects1.values_list(
                'year', flat=True)), y=course1_gradeBB, name='BB', marker_color='red'))
            fig1.add_trace(go.Bar(x=list(courseData_objects1.values_list(
                'year', flat=True)), y=course1_gradeCC, name='CC', marker_color='blue'))
            fig1.add_trace(go.Bar(x=list(courseData_objects1.values_list(
                'year', flat=True)), y=course1_gradeDD, name='DD', marker_color='yellow'))
            fig1.update_layout(barmode='stack', title_text='Student grades vs Year '+course_code1,
                               xaxis_title='Year', yaxis_title='grades')
            fig1 = fig1.to_html(
                full_html=False, default_height=500, default_width=700)

            course2_gradeAA = list(
                courseData_objects2.values_list('grade_AA', flat=True))
            course2_gradeBB = list(
                courseData_objects2.values_list('grade_BB', flat=True))
            course2_gradeCC = list(
                courseData_objects2.values_list('grade_CC', flat=True))
            course2_gradeDD = list(
                courseData_objects2.values_list('grade_DD', flat=True))
            fig2.add_trace(go.Bar(x=list(courseData_objects2.values_list(
                'year', flat=True)), y=course2_gradeAA, name='AA', marker_color='green'))
            fig2.add_trace(go.Bar(x=list(courseData_objects2.values_list(
                'year', flat=True)), y=course2_gradeBB, name='BB', marker_color='red'))
            fig2.add_trace(go.Bar(x=list(courseData_objects2.values_list(
                'year', flat=True)), y=course2_gradeCC, name='CC', marker_color='blue'))
            fig2.add_trace(go.Bar(x=list(courseData_objects2.values_list(
                'year', flat=True)), y=course2_gradeDD, name='DD', marker_color='yellow'))
            fig2.update_layout(barmode='stack', title_text='Student grades vs Year '+course_code2,
                               xaxis_title='Year', yaxis_title='grades')
            fig2 = fig2.to_html(
                full_html=False, default_height=500, default_width=700)

            return render(request, 'courseWiseComparison.html', context={'plot_div': fig, 'plot_div1': fig1, 'plot_div2': fig2})

    else:
        courseData_objects = courseData.objects.values_list(
            'course_code', flat=True).distinct().order_by('course_code')
        return render(request, 'courseWiseComparison.html', context={'courseData_objects': courseData_objects})


def individualCourseStat(request):
    if(request.method == "POST"):
        course_code = request.POST['course_code']
        semester = request.POST['semester']
        year = request.POST['year']
        courseData_objects = courseData.objects.filter(course_code=course_code, sem=semester, year=year)
        if(courseData_objects.count() == 0):
            messages.info(request, 'No data found for the given course code and semester')
            return redirect('/plots/individualCourseStat/')
        else:
            grades = ['AA',
                      'AP', 
                      'AB', 
                      'BB', 
                      'BC', 
                      'CC', 
                      'CD', 
                      'DD', 
                      'AU', 
                      'DX', 
                      'FF', 
                      'FR', 
                      'II', 
                      'NP', 
                      'PP', 
                      'S', 
                      'XX' ]
           
            marks = []
            for grade in grades:
                gr = courseData_objects.values_list('grade_'+grade, flat=True)
                marks.append(gr[0])

            fig = go.Figure()
            fig.add_trace(go.Bar(x=grades, y=marks, name="Total Students"))                    
            fig.update_layout(title_text='Students vs Grade', xaxis_title='Grades', yaxis_title='Students')
            fig = fig.to_html(full_html=False, default_height=500, default_width=700)
            
            pie = go.Figure()
            pie.add_trace(go.Pie(labels=grades, values=marks))
            pie.update_layout(title_text='Grade Distribution')
            pie = pie.to_html(full_html=False, default_height=500, default_width=700)

            return render(request, 'individualCourseStat.html', context={'line': fig, 'pie': pie})
    else:
        courseData_objects = courseData.objects.values_list(
            'course_code', flat=True).distinct().order_by('course_code')
        return render(request, 'individualCourseStat.html', context={'courseData_objects': courseData_objects})