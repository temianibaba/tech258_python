# Application Programming Interfaces

## Fundamentals
An API is a messenger that takes requests and delivers it to a device or software and then returns a response.
APIs can be thought of like a waiter in a restaurant, they take an order from the user, relay the order to another separate software (a kitchen for the sake of the analogy) and then return something back to the user.<br>
An example of this could be searching for a flight using an online travel service that interacts with other airlines API. The travel service themselves do not have direct contact with the airlines database however the can still provide data using APIs.

## What makes them popular
Interoperability.
This is the ability of equipment, systems, apps or products from different vendors to operate together in a coordinated way without an end user's involvement.
APIs are popular because they work well with different pieces of software and languages without input from the user. They give a framework for software developers create new applications that use web services.

## Data transfer using APIs
![img.png](images%2Fimg.png)
This diagram depicts the data transfer between two applications. One application being on the users device and the second one being in a database.

## Rest API
Firstly, we need to know what REST stands for, REpresentational State Transfer. It's a style of developing web services that can easily communicate with one another. REST APIs conform to this style making it easier for different software to communicate with one another, it allows a secure exchange of data over the internet. RESTful APIs consist of HTTP Methods, status codes and response types.

### Guidelines
1. Client-Server Separation
2. Uniform Interface
3. Stateless
4. Layered System
5. Cacheable
6. Code on Demand


### HTTP
Hypertext Transfer Protocol, it is used to load webpages using hypertext links. If you and an S to the end it makes it secure, HTTPS is encrypted to keep people out of data transfer.<br>
Methods or verbs
  * Get - get something
  * Post - create a resource
  * Put - Replace a resource
  * Patch - Update a resource
  * Delete - Delete a resource

### Request structure
![img_1.png](images%2Fimg_1.png)
<br><ins>Example<ins><br>
![img_4.png](images%2Fimg_4.png)


### Response Structure
![img_2.png](images%2Fimg_2.png)
<br><ins>Example<ins><br>
![img_3.png](images%2Fimg_3.png)

### Two important guidelines

- ***Stateless vs Stateful***<br>
This refers to whether an application retains information about the current state of a user's interactions or if it treats each request as an independent, isolated transaction.<br>
![img_5.png](images%2Fimg_5.png)<br>
-***Caching***<br>
Caching is the process of storing copies of files in a cache, or temporary storage location, so that they can be accessed more quickly.
