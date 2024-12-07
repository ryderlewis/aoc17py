#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int 
run_machine(int64_t a) {
	int64_t b = 0;
	int64_t c = 0;
	int64_t d = 0;
	int64_t e = 0;
	int64_t f = 0;
	int64_t g = 0;
	int64_t h = 0;

line_01:
	b = 81;
line_02:
	c = b;
line_03:
	if (a != 0) goto line_05;
line_04:
	if (1 != 0) goto line_09;
line_05:
	b *= 100;
line_06:
	b -= -100000;
line_07:
	c = b;
line_08:
	c -= -17000;
line_09:
	f = 1;
line_10:
	d = 2;
line_11:
	e = 2;
line_12:
	g = d;
line_13:
	g *= e;
line_14:
	g -= b;
line_15:
	if (g != 0) goto line_17;
line_16:
	f = 0;
line_17:
	e -= -1;
line_18:
	g = e;
line_19:
	g -= b;
line_20:
	if (g != 0) goto line_12;
line_21:
	d -= -1;
line_22:
	g = d;
line_23:
	g -= b;
line_24:
	if (g != 0) goto line_11;
line_25:
	if (f != 0) goto line_27;
line_26:
	h -= -1;
line_27:
	g = b;
line_28:
	g -= c;
line_29:
	if (g != 0) goto line_31;
line_30:
	return h;
line_31:
	b -= -17;
line_32:
	printf("Got to 32: %lld %lld %lld %lld %lld %lld %lld %lld\n", a, b, c, d, e, f, g, h);
	if (1 != 0) goto line_09;

#if 0
01: a=1                 # implied in part 2
01: b=81                # set b 81
02: c=b                 # set c b
03: if a != 0; goto 05  # jnz a 2
04: goto 09             # jnz 1 5
05: b *= 100            # mul b 100
06: b += 100_000        # sub b -100000
07: c = b               # set c b
08: c += 17_000         # sub c -17000
09: f = 1               # set f 1
10: d = 2               # set d 2
11: e = 2               # set e 2
12: g = d               # set g d
13: g *= e              # mul g e
14: g -= b              # sub g b
15: if g != 0; goto 17  # jnz g 2
16: f = 0               # set f 0
17: e += 1              # sub e -1
18: g = e               # set g e
19: g -= b              # sub g b
20: if g != 0; goto 12  # jnz g -8
21: d += 1              # sub d -1
22: g = d               # set g d
23: g -= b              # sub g b
24: if g != 0; goto 11  # jnz g -13
25: if f != 0; goto 27  # jnz f 2
26: h += 1              # sub h -1
27: g = b               # set g b
28: g -= c              # sub g c
29: if g != 0; goto 31  # jnz g 2
30: return h            # jnz 1 3
31: b += 17             # sub b -17
32: goto 09             # jnz 1 -23
#endif

#if 0
Got to 32: 1 108117 125100 108100 108100 0 -17000 1
Got to 32: 1 108134 125100 108117 108117 0 -16983 2
Got to 32: 1 108151 125100 108134 108134 0 -16966 3
Got to 32: 1 108168 125100 108151 108151 0 -16949 4
Got to 32: 1 108185 125100 108168 108168 0 -16932 5
Got to 32: 1 108202 125100 108185 108185 0 -16915 6  #
Got to 32: 1 108219 125100 108202 108202 0 -16898 7


	int X = 995;
        a = 1;
        b = 108117 + X * 17;
	c = 125100;
	d = 108100 + X * 17;
	e = 108100 + X * 17;
	f = 0;
	g = -17000 + X * 17;
	h = X + 1;

	goto label_32;


label_01:
	a = 1;
	b = 81;
	c = b;

	if (a != 0) {
		goto label_05;
	}

	goto label_09;

label_05:
	b *= 100;
	b += 100000;
	c = b;
	c += 17000;

label_09:
	f = 1;
	d = 2;

label_11:
	e = 2;

label_12:
	g = d;
	g *= e;
	g -= b;
	if (g != 0) {
		goto label_17;
	}
	f = 0;

label_17:
	e += 1;
	g = e;
	g -= b;
	if (g != 0) {
		goto label_12;
	}

	d += 1;
	g = d;
	g -= b;

	// printf("Got to 24: %d %d %d %d %d %d %d %d\n", a, b, c, d, e, f, g, h);
	if (g != 0) {
		goto label_11;
	}

	if (f != 0) {
		goto label_27;
	}

	h += 1;

label_27:
	g = b;
	g -= c;
	if (g != 0) {
		goto label_31;
	}

	return h;

label_31:
	b += 17;
label_32:
	printf("Got to 32: %d %d %d %d %d %d %d %d\n", a, b, c, d, e, f, g, h);

	goto label_09;
#endif
}

int
main() {
	printf("h=%d\n", run_machine(1));
	return 0;
}

