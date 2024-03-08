package main

import (
		"fmt"
		"net/http"
)


func main() {
		r, err := http.Get("https://google.com")
		if err != nil {
				fmt.Println("Error: ", err)
				return
		}
		fmt.Println("Response: ", r)
}
