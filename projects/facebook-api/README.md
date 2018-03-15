1. Describe your project in 1-4 sentences. 

I analyze the last 250 posts on CNN International Facebook page (https://www.facebook.com/cnninternational/) to find 5 most mentioned countries. Then I save data about basic knowledge of the 5 countries from Wikipedia and write them into 5 separate txt files. Also, I create a csv file saving country name, times of being mentioned and a Flickr image url where you can find a picture with a tag of that country¡¯s name.

2. Explain exactly what needs to be done to run your program.

First, install Wikipedia module (pip install Wikipedia).
Then, run CnnInternational.py.
You will see the files below after you run the code:
-A CSV file named cnn_word with three columns: country name, times and a Fliker image url where you can find a picture of that country.
-A txt file named imageurl containing 5 flickr url
-Five txt files containing basic information about 5 countries
If you have internet connection, your browser will automatically open and show you those images. 

3. List all the files you are turning in, with a brief description of each one. 

-cnnInternational.py: code file
-country.txt: contains names of countries that to compare and analyze the contents of posts
-README.txt: this file
-cnn_word.csv: saves country name, times of being mentioned and a Fliker image url where you can find a picture of that country.
-cnn.txt: caches data from Facebook
-imageurl.txt: caches data from flickr
-China.txt: caches data from Wikipedia
-Japan.txt: caches data from Wikipedia
-Italy.txt: caches data from Wikipedia
-Indonesia.txt: caches data from Wikipedia
-Jordan.txt: caches data from Wikipedia


4. Any Python packages/modules that must be installed in order to run your project.

--Wikipedia module


5. What API sources did you use? Provide links here and any other description necessary.

Facebook: https://developers.facebook.com/docs/graph-api/overview	
Wikipedia: https://wikipedia.readthedocs.io/en/latest/quickstart.html	
Flickr: https://www.flickr.com/services/api/

6. Approximate line numbers in Python file to find the following mechanics requirements:

- Sorting with a key function: 108
- Use of list comprehension OR map OR filter: 111

- Class definition beginning 1: 8
- Class definition beginning 2: 41
- Class definition beginning 3: 52

- Creating instance of first class: 124, 151
- Creating instance of second class: 138
- Creating instance of third class: 83

- Calling any method on any class instance): 83, 124, 138, 153
- Beginnings of function definitions outside classes: 86, 136
- Beginning of code that handles data caching/using cached data: 71, 116, 146
- Test cases: 160

7. Rationale for project: why did you do this project? Why did you find it interesting? Did it work out the way you expected?

I do this because I can quickly know which countries are the focus of the world now based on the posts of CNN Internatinonal.
I find it interesting because txt files containing basic information about those countries can help me know more about some strange countries. Also, the images on Flickr can give me a vividly impression of those countries.
It worked as I expected except the images found on Flickr are not all satisfying. 

