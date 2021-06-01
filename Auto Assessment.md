*1. Please indicate the phases for Data Analysis Process?*

Data Analysis Process:

 - Question: know more about the problem you want to solve. 
 - Wrangle
   - Data  Acquisition: acquire the data you need to answer your question
   - Data Cleaning: investigate the data and cleaning up any problems that you find
 - Explore: get familiar with the data and build an intuition about it and finding patterns
 - Draw Conclusions: draw some conclusions or make some predictions. This phase includes statistics or machine learning. 
 - Communicate: communicate your findings to the people.

*2. What are the main components of a Hadoop Application?*

The core Hadoop project consists of a wat to store data, known as the Hadoop Distributed File System (HDFS), and a way 
to process that data with Map Reduce.
The key concept is that we split the data up and store it across a collection of machines known as a cluster. Then we 
process the data where it´s actually stored rather than retrieving the data from a central server. As the data is 
already on the cluster, we can process it in place. You can add more machines to the cluster as much as you need.

HDFS: data is stored in blocks in different nodes. Blocks have a unique name and are pretty big in size.


*3. What are the 2 parts that divide the Wrangling phase?*

  - Data  Acquisition: acquire the data you need to answer your question
  - Data Cleaning: investigate the data and cleaning up any problems that you find 

*4. Data locality feature in Hadoop means?*



*5. The phase that allows us to make predictions with the data is?*



*6. Which are the three modes in which Hadoop can be run?*



*7. What happens to job tracker when Namenode is down?*

Wiht HDFS, there are set of daemons, which is just a piece of code, running all the time, running on each of these 
machines. There were the data nodes and the name node. When you run a MapReduce job, you submit the job to what´s 
called the job tracker. That splits the work into mappers and reducers. Those mappers and reducers will run on the
other cluster nodes. Running the actual map and reduce tasks is handled by a daemon called the TaskTracker software
will run on each of the nodes. As the TaskTracker runs on each of the nodes, the Dadoop framework will be able to have
the map tasks work directly on the pieces of data that are stored on that machine. This will save network traffic.
Each Mapper processes a portion of the input data. That is known as the input split. And by default, Hadoop use an 
HDFS block as the input split for each Mapper. It will try to make sure that a Mapper works on data on the same machine.

*8. What is the basic difference between traditional RDBMS and Hadoop?*

Hadoop can store any kind of data. RDBMS only works with structured data.

*9. How would you transform unstructured data into structured data?*



*10. Replication causes data redundancy, then why is it pursued in HDFS?*

HDFS works with commodity hardware (systems with average configurations) that has high chances of getting crashed any 
time. Thus, to make the entire system highly fault-tolerant, HDFS replicates and stores data in different places. Any 
data on HDFS gets stored at least 3 different locations. So, even if one of them is corrupted and the other is 
unavailable for some time for any reason, then data can be accessed from the third one. Hence, there is no chance of 
losing the data. This replication factor helps us to attain the feature of Hadoop called Fault Tolerant.

Since the data is replicated thrice in HDFS, does it mean that any calculation done on one node will also be replicated 
on the other two?
No, calculations will be done only on the original data. The master node will know which node exactly has that 
particular data. In case, if one of the nodes is not responding, it is assumed to be failed. Only then, the required 
calculation will be done on the second replica.


*11. What is a Namenode?*

To know which blocks make up the original file. This is handled by a separate machine, running a daemon called the 
NameNode. The information stored in the NameNode is known as the Metadata.

*12. What is a Datanode?*

It´s a software or a daemon, or piece of software, running on each machine of the cluster 


*13. What are Problems with small files and HDFS?*

It is not performant to work with small piece of blocks. 

*14. Can Hadoop handle streaming data?*

Yes, there are some tools that allows you to work with streaming data.

*15. In Hadoop, HDFS federation means?*

Each namenome manages a specific namespace volume. HDFS Federation allows you tu say okay, for these different 
subdirecotires that we are gonna call a namespace volume within our HDFS file structure we can actually have 
separate name nodes that are responsible for each volume. And that way a given volume will know which name to talk to
for reading and writing data fields. So we can spread out the loead of name nodes if we need to.

*16. What are the scheduler options available in YARN?*



*17. What is a block in HDFS?*

A block is a piece of a file. Each file is divided in blocks and stored across the cluster.

*18. Explain how do ‘map’ and ‘reduce’ works.*

Mappers are just little programs that each deal with a relatively small amount of data, and work in parallel. We call 
that output the "Intermediate Records". Hadoop deals with all data in the form of key and value, so these records are 
actually keys and values.

Once the Mappers have finished, a phase of Map Reduce called the "Shuffle and Sort" takes place. The Shuffle is the 
movement of the intermediate records from the Mappers to the Reducers. Sort is the fact that the Reducers will organize
these sets of records into sorted order. 

Finally, each Reducer works on on set of records at a time. It gets the key and then a list of all the values, it 
processes those in some way and then it writes out the final results.

It is possible to sort the results if you only have one reducer or add another step to sort the results.

*19. What are the common input formats in Hadoop?*



*20. What is the use of jps command in Hadoop?*