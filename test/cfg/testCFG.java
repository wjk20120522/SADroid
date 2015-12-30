public void testCFG() {
    int I = 1, J = 1, K = 1, L = 1;

    do {
        if (P) {
            J = I;
            if (Q)
                L = 2;
            else
                L = 3;
            K++;
        } else {
            K += 2;
        }
        System.out.println(I + "," + J + "," + K + "," + L);
        do {
            if (R)
                L += 4;
        } while (!S);
        I += 6;
    } while (!T);
}

