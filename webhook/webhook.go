package main

import (
	"fmt"
	"net/http"
)

func webhookHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello World, my name is Daniela Cáceres!")
}

func main() {
	http.HandleFunc("/", webhookHandler)
	fmt.Println("Server listening on port 8080")
	http.ListenAndServe(":8080", nil)
}
