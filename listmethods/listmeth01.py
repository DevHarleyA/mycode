#!/usr/bin/env python3

proto = ["ssh", "http", "https"]

print(proto)

print(proto[1])

# This line will ass d, n, and s
proto.extend("dns")

print(proto)
