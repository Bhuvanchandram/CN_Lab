set ns [new Simulator]
set tracefile [open sample.tr w]
$ns trace-all $tracefile
set namfile [open sample.nam w]
$ns namtrace-all $namfile

$ns color 1 "Blue"
$ns color 2 "Red"

proc Finish {} {
    global ns tracefile namfile
    $ns flush tracefile
    close $tracefile
    close $namfile
    exec nam sample.nam
    exec echo "The number of ping packets dropped are: " &
    exec grep "^d" prog2.tr | cut -d " " -f 5 | grep -c "ping" &
    exit 0
}

#Create 6 nodes
for {set i 0} {$i < 6} {incr i} {
    set n($i) [$ns node]
}

#Link the 6 nodes
for {set i 0} {$i < 6} {incr i}{
    $ns duplex-link $n($j) $n([expr ($j+1)]) 1Mb 10ms DropTail
}

Agent/Ping instproc recv {from rtt} {
    $self instvar node_
    puts "Node [$node_ id] received ping answer from $from with round trip time $rtt ms"
}

#Creating two ping agents
set p0 [new Agent/Ping]
$p0 set class_1
$ns attach-agent $n(0) $p(0)
set p1 [new Agent/Ping]
$p1 set class_ 1
$ns attach-agent $n(5) $p1
$ns connect $p0 $p1

$ns queue-limit $n(2) $n(3) 2
$ns duplex-link-op $n(2) $n(3) queuePos 0.5

set tcp0 [new Agent/TCP]
$tcp0 set class_ 2
$ns attach-agent $n(2) $tcp0
set sink0 [new Agent/TCPSink]
$ns attach-agent $n(4) $sink0
$ns connect $tcp0 $sink0

set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 500
$cbr0 set rate_ 1Mb
$cbr0 attach-agent $tcp0

$ns at 0.2 "$p0 send"
$ns at 0.4 "$p1 send"
$ns at 0.4 "$cbr0 start"
$ns at 0.8 "$p0 send"
$ns at 1.0 "$p1 send"
$ns at 1.2 "$cbr0 stop"
$ns at 1.4 "$p0 send"
$ns at 1.6 "$p1 send"
$ns at 1.8 "Finish"

$ns run