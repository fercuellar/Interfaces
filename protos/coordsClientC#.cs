using System;
using Grpc.Core;
using Coords;

namespace MyNamespace
{
    /// <summary>
    /// Clase principal del programa.
    /// </summary>
    class Program
    {
        /// <summary>
        /// Método de entrada del programa.
        /// </summary>
        /// <param name="args">Argumentos de línea de comandos.</param>
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
