# Air Traffic Analysis using Hadoop

Air Traffic Analysis using Hadoop is a project that aims to analyze and process large volumes of air traffic data using Hadoop, MapReduce, Sqoop, SQL, and various other Hadoop features. The project focuses on extracting valuable insights from the data to aid in air traffic management and decision-making.
<br>
## Block Diagram 
![image](https://github.com/user-attachments/assets/f259246b-5604-4bd0-a160-995113190815)
<br>
![image](https://github.com/user-attachments/assets/115764b5-1731-4595-9e54-2a0587f85b10)
<br>


<br>
**Requirements**<br>


To run the Air Traffic Analysis using Hadoop project, you need the following:
<br>
1. Hardware Requirements:

- Hadoop Cluster: The cluster should have multiple nodes with adequate storage and processing capabilities.
- Processor: 16 Gb RAM is recommended (8gb is adequate).
- Memory: 512SSD minimum is recommended.
<br>
2. Software Requirements

- Hadoop: Install and configure Hadoop on the cluster nodes. Refer to the official Hadoop documentation for installation instructions specific to your environment.
- Sqoop: Install and configure Sqoop to import data from external sources into HDFS. Ensure that Sqoop is compatible with your data sources.
- Hive or Impala: Install and configure Hive or Impala for SQL-based querying and analysis on the processed data.
- Data Visualization Tools: Choose and install a suitable data visualization tool, such as Apache Zeppelin or Tableau, to create interactive visualizations and dashboards.

<br>
## Methodology


Here are the main three points of this methodology used in this project:

1.Data Collection and Preparation: Gathering, cleaning, transforming, and preparing the required data for big data analysis.

2.Analysis and Processing: Developing and testing MapReduce and Apache Spark jobs to process the data at scale, analyze it, and extract insights.

3.Visualization and Recommendation: Analyzing and visualizing the output data using tools such as Tableau, drawing insights, and making recommendations to address the business problem.


<br>
## Analysis through Apache Spark in Google Collab

This element involves using Apache Spark to perform analysis on the air traffic data. The analysis is done through writing and executing Spark jobs, which provide advanced data processing capabilities compared to traditional MapReduce. Google Collab is used as the environment for running Spark jobs, making it easier to work with and analyze big data.

![image](https://github.com/user-attachments/assets/91bc1652-a1e0-496f-9e8e-cf60f4eefda3)
<br>
![image](https://github.com/user-attachments/assets/9b4bf394-beba-45ed-a669-fce584a004b8)

## Running Map Reduce Jobs and Hive Commands:
This element involves breaking down the air traffic data into smaller chunks and distributing it across a Hadoop cluster. MapReduce jobs and Hive commands are then used to process the data, allowing for efficient analysis of large volumes of data. This feature is a key advantage of Hadoop, making it possible to analyze big data quickly and efficiently.

![image](https://github.com/user-attachments/assets/f4989ed4-d142-4e1c-a5cf-02292a916547)

**MAP REDUCE QUESTION** <br>
Question1: Which Terminal contains maximum numbers of passengers?<br>
Answer: In MapReduce Job, we wrote the logic code for obtaining the maximum number of passengers in a file named as “logic.py.3” and then we gave our dataset which in csv type file named as “AirTerminla.csv.2”. Both the files are uploaded in HDFS of Ambari Dashboard.<br>
<br>
Command: python logic.py.3 AirTerminal.csv.2<br>
Result: Terminal 3 receive maximum no. of passengers<br>
Output: <br>
MAP REDUCE JOB
![image](https://github.com/user-attachments/assets/b4c269a7-36cb-492f-a859-6cdd55312f13)
<br>CODE
![image](https://github.com/user-attachments/assets/70143df7-6be1-4201-b0b1-4acc2132bf42)
<br>APACHE HIVE
![image](https://github.com/user-attachments/assets/85f2fe2c-b416-43ca-95b6-0485c4d1c5e6)
<br>MYSQL
![image](https://github.com/user-attachments/assets/81090e1d-6ba0-4697-9eaa-9251e800cd10)





## Implementation of Multi Node Cluster using EC2 Instance.
The implementation of a multi-node cluster involves setting up a master node and multiple slave nodes using EC2 instances. The cluster provides distributed computing power, allowing for faster processing times and more efficient analysis of big data. Tools such as Putty terminal are used to manage the nodes and run jobs on the cluster. This element is crucial for handling large volumes of data and providing more computing power for complex analysis. The implementation process of setting up a multi-node cluster using EC2 instances and Putty typically involves the following steps:

<br>
<br>
1. Launch EC2 instances:
<br> Master and Slave Instances
![image](https://github.com/user-attachments/assets/d06d0675-9ef9-411c-9ffa-005c568b4a06)
<br>
If we take any Instance, say for example: MasterDemo Instance, this instance contains information like instance has an ID of "i-08100e81f696e4773" and is currently running with a state of "Running". Its public and private id is given and the subnet ID is "subnet-05ff247d5cd627ba8"[5]. The platform is "Amazon Linux (Inferred)" and the AMI ID is "ami-0889a44b331db0194". It also contains an AWS key also with keypair.
![image](https://github.com/user-attachments/assets/13206e6d-4d90-4985-8f3f-485da174cd60)
<br>

## Install Putty and Configure SSH key:
Install the Putty SSH client on your local computer that you will use to remotely access the EC2 instances[8]. Ensure that the EC2 instances are properly configured with the necessary security groups and rules to allow incoming SSH traffic from your local computer.
<br>
![image](https://github.com/user-attachments/assets/1f13ea48-1294-4fb2-b7e4-11078b71320e)

## Connect to Instances with Putty:
Use Putty to remotely access each EC2 instance by entering the instance's public IP address or DNS name, and providing your login credentials[2].
<br>
Master-Slave MultiNode Configuration
![image](https://github.com/user-attachments/assets/b682ef31-8b0d-4f7c-96e3-2fa9ef136f78)


## Sequence Diagram
![image](https://github.com/user-attachments/assets/986c6e36-60e2-4464-ab6c-64bf27f43a3c)


## Novelty in The Project:
<br>
One unique feature of this project is the use of a recent and relatively unexplored dataset, specifically the COVID air traffic dataset. Due to the recent pandemic, there is limited research on how air traffic has been affected, making this dataset an important and timely source of information. By applying Hadoop and other big data technologies to this dataset, this project aims to provide insights and analysis that have not been previously explored, contributing to a better understanding of the impact of COVID-19 on air traffic and the aviation industry as a whole[1]. This novel approach to analyzing this specific dataset provides an opportunity for new discoveries and insights that can inform decision-making and future research in this area.
<br>

Another unique feature of the project is the implementation of a multi-node cluster using EC2 instances. This enables distributed computing on a larger scale, providing more computing power and faster processing times. This is particularly useful when working with large datasets, such as the COVID air traffic dataset, which can be processed more efficiently using distributed computing. Overall, the project on air traffic analysis using Hadoop with MapReduce and Apache Spark has several unique features that make it a valuable contribution to the field of data analysis and provide useful insights for optimizing airport resources












**Installation**<br>
***

To set up the Air Traffic Analysis using Hadoop project, follow these steps:

1. Install Hadoop: Refer to the official Hadoop documentation for installation instructions specific to your environment.

2. Set up HDFS: Configure and start the Hadoop Distributed File System (HDFS) to store and manage your data.

3. Install and Configure Sqoop: Install Sqoop and configure it to connect to your desired data sources.

4. Install Hive or Impala: Install and configure Hive or Impala for SQL-based analysis on the processed data.

5. Install Data Visualization Tools: Install your chosen data visualization tool and configure it to connect to the Hadoop cluster.

6. Import Data: Use Sqoop to import the air traffic data into HDFS for analysis. Adjust the import settings according to your data source and requirements.

7. Implement MapReduce Jobs: Develop MapReduce jobs to process and analyze the air traffic data. Write the necessary mappers, reducers, and driver code to perform the desired computations.

8. Execute Analysis: Execute the MapReduce jobs using Hadoop to perform the data analysis. Monitor the progress and collect the output for further processing.

9. Perform SQL-Based Analysis: Utilize Hive or Impala to perform SQL-based analysis on the processed data. Write SQL queries to extract insights and explore the data in a relational manner.

**Usage**<br>
***

1. Ensure that the Hadoop cluster and its related services are up and running.

2. Import the air traffic data into HDFS using Sqoop.

3. Execute the developed MapReduce jobs to process and analyze the data. Monitor the Hadoop job status and collect the output.

4. Utilize Hive or Impala to perform SQL-based analysis on the processed data. Write SQL queries to extract insights and generate reports.

5. Visualize the analysis results using your chosen data visualization tool. Create interactive dashboards and charts to facilitate data exploration and decision-making.

