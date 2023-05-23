/**
 * @file
 * @brief This is a C# program that retrieves coordinates using gRPC.
 */

using System;
using Grpc.Core;
using Coords;

namespace MyNamespace
{
    /**
     * @class Program
     * @brief Represents the main program class.
     */
    class Program
    {
        /**
         * @brief The entry point of the program.
         * @param args The command line arguments.
         */
        static void Main(string[] args)
        {
            // Create a channel to connect to the gRPC server
            Channel channel = new Channel("localhost:50055", ChannelCredentials.Insecure);

            // Create a client to communicate with the gRPC server
            var client = new CoordsComm.CoordsCommClient(channel);

            // Continuously retrieve coordinates from the server
            while (true)
            {
                // Send a request to the server to get the coordinates
                var reply = client.getCoords(new Empty());

                // Print the received coordinates
                Console.WriteLine("Coords received: " + reply);
            }
        }
    }
}

