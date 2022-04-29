pi@raspberrypi:/usr/local/lib $ cat prometheus_push.sh 
#!/bin/bash
#####

while true;

do
        curl 127.0.0.1:5000/metrics1 |curl --data-binary @- http://47.100.126.11:9091/metrics/job/temprature/instance/10.8.1.195  >> /dev/null 2>&1

        curl 127.0.0.1:5000/metrics2 |curl --data-binary @- http://47.100.126.11:9091/metrics/job/humidity/instance/10.8.1.195  >> /dev/null 2>&1

        sleep 60

done

