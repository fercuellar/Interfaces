package main

import (
	"context"
	"fmt"
	pb "GO/gen/proto"
	"log"

	"google.golang.org/grpc"
)

func main() {
	conn, err := grpc.Dial("localhost:8080", grpc.WithInsecure())
	if err != nil {
		log.Println(err)
	}

	client := pb.NewTestApiClient(conn)

	resp, err := client.GetUser(context.Background(), &pb.UserRequest{Uuid: "Fernando"})
	if err != nil {
		log.Println(err)
	}
	fmt.Println(resp)
}
