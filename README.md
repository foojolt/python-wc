# python-wc
简单的wordcount python实现版本。

环境中运行
联系 hadoop 集群管理员，在hadoop客户端机器上，使用以下命令提交任务：

hadoop jar /opt/cloudera/parcels/CDH-5.4.8-1.cdh5.4.8.p0.4/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.4.8.jar -input wc/wc.txt -output out-wc1/ -mapper map.py -combiner reduce.py -reducer reduce.py -file map.py -file reduce.py

需要事先将wc.txt上传到hdfs上。命令中可以指定输入文件、输出文件夹（必须不存在）、mapper/reducer实现，最后的 -file 是指定需要上传的资源，会下载到每个执行机器上。

如果不知道streaming jar包在哪里（比如集群不是你安装的），你可以用下面的命令找到

find / -name *.jar | grep streaming
