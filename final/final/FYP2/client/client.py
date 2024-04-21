import Ice
import Message
import sys

class Client(Ice.Application):
    def run(self, argv):
        with self.communicator() as communicator:
            proxy = communicator.stringToProxy("sender:default -h 192.168.0.200 -p 10000")
            sender = Message.MessageSenderPrx.checkedCast(proxy)
            if not sender:
                raise RuntimeError("Invalid proxy")

            message = input("Enter message to send: ")
            sender.sendMessage(message)
            return 0

if __name__ == "__main__":
    app = Client()
    sys.exit(app.main(sys.argv))
