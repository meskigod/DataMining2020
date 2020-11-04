#Assignment 2

#Exercise 1

#Read Total profit of all months and show it using a line plot Total profit data provided for each month. Generated line plot must include the following properties:

#X label name = Month Number
#Y label name = Total profit


plt.plot(data.total_profit)
plt.xlabel('Month Number')
plt.ylabel('Total Profit')

#Exercise 2
#Get Total profit of all months and show line plot with the following Style properties Generated line plot must include following Style properties:

#Line Style dotted and Line color should be red
#Show legend at the lower right location.
#X label name = Month Number
#Y label name = Sold units number
#Add a circle marker.
#Line marker color as read
#Line width should be 3

units_sold=plt.plot(data.total_profit, marker="o", linestyle='dotted', linewidth='3', color='red', label="first_legend")
plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.legend(loc='lower right')

#Exercise 3
#Read all product sales data and show it using a multiline plot Display the number of units sold per month for each product using multiline plots. (i.e., Separate Plotline for each product for each product).

months = data['month_number'].tolist()
facecream_sales=data['facecream'].tolist()
facewash_sales=data['facewash'].tolist()
toothpaste_sales=data['toothpaste'].tolist()
soap_sales=data['bathingsoap'].tolist()
shampoo_sales=data['shampoo'].tolist()
moisturizer_sales=data['moisturizer'].tolist()

plt.plot(months,facecream_sales,marker='o',label='Facecream Sales Data', linewidth=2)
plt.plot(months,facewash_sales,marker='o',label='Facewash Sales Data', linewidth=2)
plt.plot(months,toothpaste_sales,marker='o',label='Toothpaste Sales Data', linewidth=2)
plt.plot(months,soap_sales,marker='o',label='Soap Sales Data', linewidth=2)
plt.plot(months,shampoo_sales,marker='o',label='Shampoo Sales Data', linewidth=2)
plt.plot(months,moisturizer_sales,marker='o',label='Moisturizer Sales Data', linewidth=2)

plt.xlabel('Months')
plt.ylabel('Product Sales')
plt.title('Sales of the year')
plt.legend(loc='upper left', prop={"size":7.5})
plt.show()

#Exercise 4
#Read toothpaste sales data of each month and show it using a scatter plot Also, add a grid in the plot.

months=data['month_number'].tolist()
toothpaste_sales=data['toothpaste'].tolist()
plt.scatter(months,toothpaste_sales, color='red',label="toothpaste sales")

plt.grid()
plt.xlabel('Months')
plt.ylabel('Units sold')
plt.title('Toothpaste Sales')
plt.legend(loc='upper left')

plt.show()
#Exercise 5
#Read face cream and facewash product sales data and show it using the bar chart Bar chart should display the number of units sold per month for each product. Add a separate bar for each product in the same chart.

plt.bar([i-0.25 for i in months], facecream_sales, color='r', label='Facecream Sales', width=0.25, align='edge')
plt.bar([i+0.25 for i in months], facewash_sales, color='g', label='Facewash Sales', width=-0.25, align='edge')

plt.xlabel('Months')
plt.ylabel('Unit Sales')
plt.title('Facewash and Facecream Sales')
plt.legend(loc='upper right')
plt.xticks(months)
plt.grid(True, linewidth=1, linestyle="--")
plt.show()

#Exercise 6
#Calculate total sale data for last year for each product and show it using a Pie chart Note: In Pie chart display Number of units sold per year for each product in percentage.

Product_List =['Facecream', 'Facewash','Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']
Sales=[data['facecream'].sum(), data['facewash'].sum(), data['toothpaste'].sum(), data['bathingsoap'].sum(), data['shampoo'].sum(), data['moisturizer'].sum()]
plt.axis("equal")
plt.pie(Sales, labels=Product_List , autopct='%1.1f%%')
plt.legend(loc="lower right", prop={"size":7.5})
plt.title('Sales Data')
plt.show()


