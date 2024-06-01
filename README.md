Running Hadoop

This is running on my Windows 11 Machine

1. In Linux shell, make and enter a new directory, I used WSL
>mkdir running-hadoop
>cd running-hadoop

2. Make eu and wxw directories and enter wxw directory
>mkdir eu
>mkdir wxw
>cd wxw

3. Clone from GitHub
>git clone https://github.com/wxw-matt/docker-hadoop

4. Go back and enter the eu directory and clone from GitHub
>cd ..
>cd eu
>git clone https://github.com/big-data-europe/docker-hadoop

5. Enter newly created directory
>cd docker-hadoop

6. Test Docker
>docker run hello-world

7. Bring Docker containers up, this will take a bit of time
>docker-compose up -d

8. Verify that the docker containers are running
>docker ps

9.Enter the namenode container
>docker exec -it namenode /bin/bash

10. Create new directories inside
>mkdir app
>mkdir app/data
>mkdir app/res
>mkdir app/jars

11. Fetch data directly from the wxw-matt GitHub repo, and download to your local system
>jobs\>jar\>WordCount.jar

12. Open the Windows shell (I used Powershell), find the WordCount.jar file
>cd .\Downloads\

13. Copy to the open namenode container in the app/jars directory
>docker cp .\WordCount.jar namenode:/app/jars/WordCount.jar

14. Return the Linux shell and download the text data to be scanned
>cd /app/data
>curl https://www.gutenberg.org/cache/epub/1342/pg1342.txt -o austen.txt
>curl https://www.gutenberg.org/cache/epub/84/pg84.txt -o shelley.txt
>curl https://www.gutenberg.org/cache/epub/768/pg768.txt -o bronte.txt

15. You can verify that you have files of some size downloaded
>ls -al

16. Return to the highest directory
> cd /

17. Load data from the Linux file system into the Hadoop Distributed File System (HDFS)
>hdfs dfs -mkdir /test-1-input
>hdfs dfs -copyFromLocal -f /app/data/*.txt /test-1-input/

18. Run Hadoop/MapReduce
>hadoop jar jars/WordCount.jar WordCount /test-1-input /test-1-output

19. Copy results out
> hdfs dfs -copyToLocal /test-1-output /app/res/

20. See results
>head /app/res/test-1-output/part-r-00000
