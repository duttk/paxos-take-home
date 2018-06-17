# Take Home

Solutions to a take home challenge written in Python.

## Getting Started

To get started with these challenges, you can get a copy of the repo here
```
$ git clone https://github.com/duttk/take-home.git
$ cd take-home
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
The pip install might fail if setup tools version is < 36. 
To fix this, upgrade setuptools and try the pip install again.

```
$ pip install --upgrade setuptools
```

## Challenge 1

Publish a micro service with two enpoints
I have chosen to use hug(http://www.hug.rest/) for API development and tavern(https://taverntesting.github.io/) for automated testing.

To start the service, we need to install the dependencies and bringup the run server.
We need to first create a python virtual environment and use requirement.txt to install the dependencies.

```
$ cd challenge1
$ hug -p 8006 -f sha.py &
$ curl -X POST -H  "Content-Type:  application/json" -d '{"message":  "foo"}' localhost:8006/messages
$ curl localhost:8006/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae
$ curl localhost:8006/messages/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
$ curl localhost:8006/
```

### Testing

To test the API, we need the server running.
We can then run our automated test suite with pytest.

```
$ hug -p 8006 -f sha.py &
$ pytest test_sha.tavern.yaml
```

### Performance 

We should first identify and instrument the performance bottlenecks before diving into optimisation.
The performace bottleneck in this case is the single threaded nature of the web server.
In a production setting we should have the app served by gunicorn with multiple workers to reduce request-response latency.
Beyond this, we could have multiple servers behind a load balancer.

## Challenge 2

Find the best pair of items with prices equal or minimally under a sum
The solution I came up with for a sorted array was to have two pointers and to keep track of the difference between the target and the sum of the items.

1. The two pointers are initialised at start and end of the array.
2. If the difference exceeds the target, the right pointer is moved back
3. If the difference is less than the target, and the new difference is better than the old difference, we update our best pair. Else move the left pointer forward.


### Testing

We can test the solution as below
```
$ cd challenge2
$ ./find-pair prices.txt 2500
```

### Performance 

We have to exhaustively seach the sorted array for combinations of inputs that are minimally under the target.
Therefore the solution is O(n)

## Challenge 3

Return a combination of all numbers in the pattern with X's replaced with 0s and 1s.
Here a recursive approach works well.

1. We find all possible combinations for the first element of the array
2. We find all possible combinations for the rest of the elements.
3. We take all combinations of 1 and 2 to get all elements

The base case is reached when we only have 1 in our array. 
If this element is X, we return both 0 and 1, else, we return the element.

### Testing

We can test the solution as below
```
$ cd challenge3
$ ./myprogram 0X0X1
```

### Performance 

The worst we can do in this solution is when we set all elements in the pattern X
Therefore the solution is O(2^m). Where m is the number of X's in the array.

