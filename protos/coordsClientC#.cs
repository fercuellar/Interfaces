using System;
using Grpc.Core;
using Coords;

namespace MyNamespace
{
    class Program
    {
        static void Main(string[] args)
        {
            Channel channel = new Channel("localhost:5005", ChannelCredentials.Insecure);
            var client = new CoordsComm.CoordsCommClient(channel);
            var reply = client.GetCoords(new Empty());
            Console.WriteLine("Coords received: " + reply);
            channel.ShutdownAsync().Wait();
        }
    }
}
