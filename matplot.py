from matplotlib import pyplot
from matplotlib import style

style.use('ggplot')
#style.use('bmh')
#style.use('classic')
#style.use('dark_background')
#style.use('fivethirtyeight')
#style.use('seaborn')
#style.use('Solarize_Light2')
#style.use('seaborn-talk')
#style.use('seaborn-poster')
#style.use('seaborn-deep')

x = [5,6,7,3]
y = [1,10,13,5]

x1 = [i*3 for i in x]
y1 = [i*3 for i in y]

pyplot.plot(x,y,color='g',linewidth = 5,label = 'line 1')
pyplot.plot(x1,y1,color='c',linewidth = 10,label = 'line 2')

pyplot.title('my first plot in python')
pyplot.ylabel('this is the "y"')
pyplot.xlabel('this is the "x"')
pyplot.legend()

pyplot.show()

pyplot.scatter(x,y,color='g',linewidth = 5,label = 'line 1')
pyplot.scatter(x1,y1,color='c',linewidth = 10,label = 'line 2')

pyplot.legend()

pyplot.show()

pyplot.bar(x,y,color='g',linewidth = 5,label = 'line 1',align = 'center')
pyplot.bar(x1,y1,color='c',linewidth = 10,label = 'line 2',align='center')

pyplot.legend()
pyplot.xticks(list(range(max(x+x1)+1)))

pyplot.show()