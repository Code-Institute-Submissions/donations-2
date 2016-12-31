# donations
Donations dashboard example

The dashboard linked to this file represents school donations broken down by different attributes. The dataset comes from DonorsChoose which is a 
non-profit organization which allow individuals to donate money directly to public school classroom projects. Public school teachers post classroom project requests on the platform, and individuals have the option to donate money directly to fund these project.

I have used one of the available datasets to build an interactive data visualization that represents school donations broken down by different attributes.

The tools i used for this dashboard include
  D3 - which renders the charts and graphs based on the data.
  Crossfilter - This JavaScript data manipulation library which enables two way binding.
  MongoDb - Our dastabase which is used to convert and present the data in JSON format.
  Flask - Used to serve the data from the server to the interface.
  
  I also created an additional 3 pie-charts along with a map of the United States which allows users of the dashboard to select different geographic areas via the map. 
  
 I first uploaded the data (contained in a csv file) to an instance of MongoDb which in turn converted to a Json format.
 
 Having done this, you can view the entire data collection using Mongo Management Studio. From there i choose six fields as the basis for the dashboard.
 
 I then used Python Flask to build the sewrver that interacts with MongoDb and renders the page that contained the charts.
 
 Within my index page i linked to a graph.js file which contained the logic and data binding for the dashboard elements. I also created a new graph.js file which injects the data from the python class into it.
 The data is filterted here usinmg crossfilter.js before its bound to the charts.
 
 In additioon to the bootstrap template, there is my own custom css file to help style the dashboard. 
 
 The "Start Tour" button provides a Dashboard tutorial which targets each Dashboard element with an explanation of its purpose.
 
 Finally using Jquery i added two buttons at the bottom of the dashboard allowing uswers to view more inmformation about the work DonorsChoose do and also provided a form if users wanted to register for the organization.
