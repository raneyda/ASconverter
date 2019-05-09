# ASconverter
Autonomous System Number converter

## What is an Autonomous System Number?

An Autonomous System (AS) number is assigned by a regional internet registry (RIR), such as [ARIN](ARIN.net) in the US.  These numbers are using to identify a source AS for BGP routing.  Typically an AS number is required when an end user is multihoming to more than one provider.

Historically AS numbers were in the range 0 - 65535 or (2^16) as AS numbers were only 2 bytes (16 bits).  As technology has progressed so has the number of end users requiring an AS numbers.  Similar to the the IPv4 exhuastion AS numbers were also on path to become exhuasted.  Because of this 4 byte AS numbers were introduced.  With the new AS numbers there was also a new notation.  This is called the asdot notation, as referenced in [RFC 5396](https://tools.ietf.org/html/rfc5396), and includes two 16 bit values separated by a dot.  The original notation is known as asplain and includes no dot because historically AS numbers were only 16 bits.

This program allows for the input of either notation and will return the alternate notation.  

## Why is this useful?

It might not be!  Modern routers will likely perform the conversion for you depending on what format you use to enter the AS number.  However; if you ever need to check that an AS number has been entered correctly you can use this tool for a quick conversion.

# References
Autonomous System (AS) Number Reservation for Documentation Use
https://tools.ietf.org/html/rfc5398

Reservation of Last Autonomous System (AS) Numbers
https://tools.ietf.org/html/rfc7300

Textual Representation of Autonomous System (AS) Numbers
https://tools.ietf.org/html/rfc5396

Guidelines for creation, selection, and registration
of an Autonomous System (AS)
https://tools.ietf.org/html/rfc1930

Autonomous System (AS) Reservation for Private Use
https://tools.ietf.org/html/rfc6996

BGP Support for Four-Octet Autonomous System (AS) Number Space
https://tools.ietf.org/html/rfc6793
