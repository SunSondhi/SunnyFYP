import Ice
import sys
import Message

# Implement the MessageSender interface
class MessageSenderI(Message.MessageSender):
    def sendMessage(self, message, current=None):
        print("Received message:", message)

# Server class
class Server(Ice.Application):
    def run(self, argv):
        with self.communicator() as communicator:
            adapter = communicator.createObjectAdapterWithEndpoints("MessageAdapter", "default -p 10000")
            sender = MessageSenderI()
            adapter.add(sender, communicator.stringToIdentity("sender"))
            adapter.activate()
            print("Server started...")
            communicator.waitForShutdown()
        return 0

if __name__ == "__main__":
    app = Server()
    sys.exit(app.main(sys.argv))
