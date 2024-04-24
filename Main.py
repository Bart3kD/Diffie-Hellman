from Sockets import Client
from Sockets import Server
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-m", "--mode", dest="mode", type=str, required=True,
                        help="-m CLIENT to start a client, -m SERVER to start a server"
                        )
    parser.add_argument("-d", "--debug", dest="debug", type=str, required=False,
                        help="Use this to enable printing debug messages",
                        action="store_true"
                        )
    
    args = parser.parse_args()

    if args.debug:
        print(args)
    
    if args.mode.lower() == "client":
        server = "localhost"
        client = Client.ClientSocket(args.debug)
        client.start_client(server)
    
    elif args.mode.lower() == "server":
        Server.start_server(args.debug)