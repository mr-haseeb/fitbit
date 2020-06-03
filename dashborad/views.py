from django.shortcuts import render,render_to_response
from bokeh.plotting import figure,output_file,show
from bokeh.embed import components





# Create your views here.
def home(request):
    return render(request, 'dashborad/base.html')



def charts(request):

	#Graph X & Y coordinates
	x=[1,2,3,4,5]
	y=[1,2,3,4,5]

	#Setup graph plot for displaying line graph
	plot=figure(title='Line Graph',x_axis_label='X-Axis',y_axis_label='Y-Axis',plot_width=400,plot_height=400)

	#plot Line
	plot.line(x,y,line_width=2)

	#Store Components
	script,div=components(plot)

	return render_to_response('dashborad/charts.html',{'script':script,'div':div})

