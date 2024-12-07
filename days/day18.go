package main

import (
	"context"
	"fmt"
	"sync"
	"sync/atomic"
	"time"
)

func main() {
	m0 := Machine{
		txq: make(chan int64, 10_000),
	}
	m1 := Machine{
		p:   1,
		txq: make(chan int64, 10_000),
	}
	m0.rxq = m1.txq
	m1.rxq = m0.txq

	wg := sync.WaitGroup{}
	wg.Add(2)

	go func() {
		defer wg.Done()
		m0.Run()
	}()

	go func() {
		defer wg.Done()
		m1.Run()
	}()

	wg.Wait()
	fmt.Printf("Done: %v\n", m1.GetSendCount())
}

type Machine struct {
	a int64
	b int64
	f int64
	i int64
	p int64

	txq        chan int64
	rxq        <-chan int64
	sendCount  atomic.Uint64
	deadlocked atomic.Bool
	done       atomic.Bool
}

func (m *Machine) send(v int64) {
	m.txq <- v
	m.sendCount.Add(1)
}

func (m *Machine) GetDeadlocked() bool {
	return m.deadlocked.Load()
}

func (m *Machine) GetDone() bool {
	return m.done.Load()
}

func (m *Machine) GetSendCount() uint64 {
	return m.sendCount.Load()
}

func (m *Machine) recv(v *int64) error {
	ctx, cancel := context.WithTimeout(context.Background(), 1*time.Second)
	defer cancel()

	select {
	case x := <-m.rxq:
		*v = x
		return nil
	case <-ctx.Done():
		m.deadlocked.Store(true)
		return fmt.Errorf("deadlocked")
	}
}

func (m *Machine) Run() {
	m.deadlocked.Store(false)
	m.done.Store(false)
	defer m.done.Store(true)

	// 01: set i 31
	m.i = 31

	// 02: set a 1
	m.a = 1

	// 03: mul p 17
	m.p *= 17

	// 04: jgz p p
	if m.p > 0 {
		switch m.p {
		case 17:
			goto line21
		default:
			panic(fmt.Sprintf("unknown jump %d", m.p))
		}
	}

line05:
	// 05: mul a 2
	m.a *= 2

	// 06: add i -1
	m.i += -1

	// 07: jgz i -2
	if m.i > 0 {
		goto line05
	}

	// 08: add a -1
	m.a += -1

	// 09: set i 127
	m.i = 127

	// 10: set p 618
	m.p = 618

	// 11: mul p 8505
line11:
	m.p *= 8505

	// 12: mod p a
	m.p %= m.a

	// 13: mul p 129749
	m.p *= 129749

	// 14: add p 12345
	m.p += 12345

	// 15: mod p a
	m.p %= m.a

	// 16: set b p
	m.b = m.p

	// 17: mod b 10000
	m.b %= 10000

	// 18: snd b
	m.send(m.b)

	// 19: add i -1
	m.i += -1

	// 20: jgz i -9
	if m.i > 0 {
		goto line11
	}

line21:
	// 21: jgz a 3
	if m.a > 0 {
		goto line24
	}

	// 22: rcv b
line22:
	if err := m.recv(&m.b); err != nil {
		return
	}

	// 23: jgz b -1
	if m.b > 0 {
		goto line22
	}

line24:
	// 24: set f 0
	m.f = 0

	// 25: set i 126
	m.i = 126

	// 26: rcv a
	if err := m.recv(&m.a); err != nil {
		return
	}

line27:
	// 27: rcv b
	if err := m.recv(&m.b); err != nil {
		return
	}

	// 28: set p a
	m.p = m.a

	// 29: mul p -1
	m.p *= -1

	// 30: add p b
	m.p += m.b

	// 31: jgz p 4
	if m.p > 0 {
		goto line35
	}

	// 32: snd a
	m.send(m.a)

	// 33: set a b
	m.a = m.b

	// 34: jgz 1 3
	goto line37

line35:
	// 35: snd b
	m.send(m.b)

	// 36: set f 1
	m.f = 1

line37:
	// 37: add i -1
	m.i += -1

	// 38: jgz i -11
	if m.i > 0 {
		goto line27
	}

	// 39: snd a
	m.send(m.a)

	// 40: jgz f -16
	if m.f > 0 {
		goto line24
	}

	// 41: jgz a -19
	if m.a > 0 {
		goto line22
	}
}

/*
 */
