𝐒𝐘𝐒𝐓𝐄𝐌 𝐃𝐄𝐒𝐈𝐆𝐍 𝐏𝐀𝐓𝐓𝐄𝐑𝐍𝐒 𝐅𝐎𝐑 𝐈𝐍𝐓𝐄𝐑𝐕𝐈𝐄𝐖𝐒

Some of the most common system design patterns will be very helpful in 𝖎𝖓𝖙𝖊𝖗𝖛𝖎𝖊𝖜𝖘 as these would come in handy for all kinds of system design problems.

- 𝗤𝗨𝗢𝗥𝗨𝗠
It is the minimum number of servers on which the operation must be performed successfully before declaring the operation's overall success.
𝙀𝙭𝙖𝙢𝙥𝙡𝙚: Cassandra: Each write request can be configured to be successful only if it is written to at least the majority of replica nodes.
 
-𝗙𝗔𝗨𝗟𝗧 𝗧𝗢𝗟𝗘𝗥𝗔𝗡𝗖𝗘
One server is elected as a leader who is responsible for data replications and acts as a pivot to coordinate work.
𝙀𝙭𝙖𝙢𝙥𝙡𝙚: Kafka: Each partition has a leader which is responsible for all the read/writes for that partition.

-𝗛𝗘𝗔𝗥𝗧𝗕𝗘𝗔𝗧
Every Server sends heartbeats at regular intervals to the central server to indicate that they are alive.
𝙀𝙭𝙖𝙢𝙥𝙡𝙚: GFS, HDFS

-𝗙𝗘𝗡𝗖𝗜𝗡𝗚
Putting a "Fence" around the previous leader to prevent it from doing any damage or causing any disruption.
𝙀𝙭𝙖𝙢𝙥𝙡𝙚: HDFS uses fencing to stop previous leader NameNode from accessing shared cluster resources.

-𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗜𝗢𝗡 𝗖𝗟𝗢𝗖𝗞
A monotonically increasing number indicates the generation of the server.
𝙀𝙭𝙖𝙢𝙥𝙡𝙚: Kafka, Cassandra

-𝗚𝗢𝗦𝗦𝗜𝗣 𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟
Every Node keeps track of state information about the other nodes in the cluster and gossip this information to one other random node every second.
𝙀𝙭𝙖𝙢𝙥𝙡𝙚: Dynamo and Cassandra use gossip protocol where nodes send some information to another known node in the cluster at random every sec.
