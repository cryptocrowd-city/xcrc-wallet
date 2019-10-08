# Masternode Commands

`systemctl start cryptocrowdd`
\- Starts the CRyptoCrowd Daemon

`systemctl stop cryptocrowdd`
\- Stops the CRyptoCrowd Daemon

`systemctl restart cryptocrowdd`
\- Restarts the CRyptoCrowd Daemon

`systemctl status cryptocrowdd`
\- Displays the status of the CRyptoCrowd Daemon

`cryptocrowd-cli masternode status`
\- Displays the status of the CRyptoCrowd masternode running on the VPS

`cryptocrowd-cli getinfo`
\- Displays general info about the masternode

`cryptocrowd-cli masternodecurrent`
\- Displays additional info about the masternode

`ps aux | grep cryptocrowd`
\- Shows if the cryptocrowdd process is running

`dmesg | egrep -i 'killed process'`
\- Lets you know whether cryptocrowdd was killed due to lack of memory

`nano ~/.cryptocrowd/cryptocrowd.conf`
\- Edits your cryptocrowd.conf file

`killall -9 cryptocrowdd`
\- Force quits cryptocrowdd (*USE WITH CAUTION*)

`cryptocrowd-cli getpeerinfo | grep synced_headers`
\- Displays synced headers

`cryptocrowd-cli getmasternodecount`
\- Displays count of all masternodes

`bash <( curl https://raw.githubusercontent.com/cryptocrowd-crypto/CRyptoCrowd-MN-Install/master/refresh_node.sh )`

Refreshes your node by clearing the chaindata

`bash <( curl https://raw.githubusercontent.com/cryptocrowd-crypto/CRyptoCrowd-MN-Install/master/update_node.sh )`

Updates your node to the newest version
