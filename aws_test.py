# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

def aws_echo(client, userdata, message):
	print("Received a new message: ")
	print(message.payload)
	print("from topic: ")
	print(message.topic)
	print("--------------\n\n")

# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("secondThing")
# For Websocket connection
# myMQTTClient = AWSIoTMQTTClient("secondThing", useWebsocket=True)
# Configurations
# For TLS mutual authentication
myMQTTClient.configureEndpoint("a28p4yj60z6xz.iot.us-west-2.amazonaws.com", 8883)
# For Websocket
# myMQTTClient.configureEndpoint("a28p4yj60z6xz.iot.us-west-2.amazonaws.com", 443)
myMQTTClient.configureCredentials("/aws/VeriSign-Class3-Public-Primary-Certification-Authority-G5.pem", "/aws/bad80c7e60-private.pem.key", "/aws/bad80c7e60-certificate.pem.crt")
# For Websocket, we only need to configure the root CA
# myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myMQTTClient.connect()
myMQTTClient.subscribe("mysubTopic", 1, aws_echo)

print("Starting ...")
while(True):
    x=1
