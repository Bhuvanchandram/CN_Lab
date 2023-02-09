set ns [new Simulator]
set tracefile [open sample.tr w]
$ns trace-all $tracefile
set namfile [open sample.nam w]
$ns namtrace-all $namfile

set no [$ns node]
set n1 [$ns node]
set n2 [$ns node]

$no label "Source"
$n1 label "Sink"
$ns color 1 "Blue"

$ns duplex-link $n0 $n1 1.0Mb 10ms DropTail
$ns duplex-link $n1 $n2 1.0Mb 10ms DropTail

$ns duplex-link-op $n0 $n1  orient right 
$ns duplex-link-op $n1 $n2  orient right 

$ns queue-limit $n0 $n1 10
$ns queue0limit $n1 $n2 10

set tcp0 [newAgent/TCP]
$ns attach-agent $n0 $tcp0
set sink0 [newAgent/TCPSink]
$ns attach-agent $n2 $sink0
$ns connect $tcp0 $sink0



