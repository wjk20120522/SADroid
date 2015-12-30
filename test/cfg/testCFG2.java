public void testCFG2(int a, int b, int c) {
    a += 5;
    b += a * 5;
    if (a < b) {
        if (b < c) {
            System.out.println("foo");
        } else {
            System.out.println("bar");
        }
    }
    a = 10;
    while (a < c) {
        a += c;
        do {
            b = a++;
            System.out.println("baz");
        } while (c < b);
        b++;
    }
    System.out.println("foobar");
    if (a >= 5 || b * c <= c + 10) {
        System.out.println("a = " + 5);
    }
    System.out.println("end");
}