# Statistical-Data-Analysis-PPV-PPL

Given two datasets, namely, people.csv and ppv.csv. The first dataset
consists of 10000 vaccinees’ locations while the second dataset represents 100
vaccination centers’ locations. All the locations are given by the latitudes and longitudes.
My task is to assign vaccinees to vaccination centers, and I need to find the shortest distances.

__This is head of people.csv data:__

![](Graph%20Image/headpplcsv.png)

__This is head of ppv.csv data:__

![](Graph%20Image/headppvcsv.png)

## __Task 1:__ Is there any significant difference between the execution time for 2 computers?

Computer 1 is equipped with CPU AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx 2.10 GHz, 4.00 GB (3.45 GB usable) of RAM, SSD for storage device and AMD Radeon(TM) Vega 8 Graphics (512MB). 

Computer 2 is equipped with CPU Intel core i5-10500H CPU @ 2.50GHZ, 8.00 GB (7.83 GB usable) of RAM, SSD as storage device and NVIDIA GeForce GTX 1650 (4GB) graphics card.

__Table:__

![](Graph%20Image/2comptable.png)

__Result:__
![](Graph%20Image/Graph%201.PNG)

Both of the computers use Windows operating systems. The experiment is done in a similar environment where no background software was opened during the program execution to minimise noise. Computer 2 has more powerful hardware specifications stated compared to computer 1. Due to this, it is expected that computer 2 takes less time to execute the program. The result acquired proved the expected performance. 

According to the graph, computer 2 has the highest density of finishing the program's execution in 2.20 to 2.25 seconds. While computer 1 is most likely to complete the program's execution in 3.70 to 3.75 seconds. The distribution in the computer 2 graph is symmetric, skew-free, and has identical tails. However, computer 1 is a right skewed distribution because it has a quite long right tail, so it shows that the mean are greater than their medians. Due to the tail being skewed to the right, we can also refer to this distribution as being positively skewed. This finding leads us to the conclusion that computer 2 has a higher probability to finish running the program faster than computer 1.

## __Task 2:__ Is there any significant difference between the execution time for 3 different Python programs?

__Table:__

![](Graph%20Image/3diffmethodtable.png)

__Result:__

![](Graph%20Image/Graph%202.PNG)

The three algorithms used have their own significant differences between their execution times.

For the first algorithm, when the program starts, the program will record the current time and store it in a variable before executing any process. The data about the latitude and longitude of  people and PPV (“Pusat Pengagihan Vaksin” or Vaccine Distribution Centre) are retrieved from two csv files and stored in two different two-dimensional lists. Both of the 2 dimensional lists are then passed into a function to calculate the distance between the peoples’ and PPV’s location. The first distance between each person and the PPV and the PPV number is stored in a variable as the initial shortest distance. When a new distance is acquired and the value is smaller than the current shortest distance, the shortest distance and the nearest PPV number will be replaced. After all people with their nearest PPV number are obtained, the data will be saved in a new csv file. When all operations are done, the program will capture the end time and print the time taken to execute the program by subtracting the end time with the start time.


The second algorithm is derived from the same concept from algorithm 1. However, the data is replaced from using lists to using linked lists. Linked lists use a different concept from list where each node points to another node that creates a chain-style data list. We first declare a linked list class to store the data. Each node has a latitude value, a longitude value and a pointer that refers to the next node. When the program starts, the initial latitudes and longitudes data are retrieved. For the distance calculation process, for each person's and PPV’s point data in the linked list, the program will traverse from head to the specific node to get the latitude and longitude value. This requires more processing power which consumes more time to be executed. The people and PPV with the shortest distance then recorded in a csv file and the time is taken. 


The third algorithm is conceptually similar to the first two, however it is implemented using numpy array as the data structure and the Scikit-learn (Sklearn) package rather than the haversine package. The program will first calculate the total number of rows. Using the number of rows which is equivalent to the number of people and PPV, two numpy arrays with all the initial values in the array set to zero, are created. Using the data, the program will use the latitude and longitude of these two places to determine the distance between them and the shortest one will be stored.

From the graph, we can clearly see that method 1 requires the least amount of time to execute the program compared to method 2 and 3. All of these methods used different data structures to store the data. Method 1 uses lists, method 2 uses linked lists while method 3 uses numpy arrays. Furthermore, both method 1 and 2 uses haversine package while method 3 uses Sklearn package.

Since method 1 is made from the combination of the simplest data structure and package between those 3 methods, which are list and haversine package, it requires less time as the program requires less processing power. List requires a small amount of memory allocation to store the data. The haversine package is simpler compared to the Sklearn package, that is used in method 3, since it is built just to calculate distance between two points in spherical coordinates.

Different with method 1, method 2 uses linked lists which is slower than lists. This method still uses the haversine package. To get the coordinates data, the program needs to traverse through the linked list to get the specific data. Due to this, more processing time and power is required to perform the task.

Method 3 uses a different data structure and package than method 1 and 2. This method uses numpy arrays and the Sklearn package. Numpy array is faster than both list and linked list. However, due to the usage of the Sklearn package, this method takes the longest time to execute the program because the Sklearn package is complex. This package is created to be used in machine learning and data analysis. Besides, this algorithm has an extra process where it needs to count the number of people and PPV first before creating the array. Hence, more power is needed and more time is taken. Method 2 and 3 are almost similar in the time taken to execute the program because method 2 uses complex data structure with a simple package, while method 3 uses simple data structure with a complex package.
