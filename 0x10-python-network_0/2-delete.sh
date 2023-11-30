#!/bin/bash
#script that sends a DELETE request & displays the body of the response
curl -s "$1" -X DELETE
