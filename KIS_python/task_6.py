def main(o_big: set):
    delta_big = {6 * o_small for o_small in o_big if -83 < o_small <= 37}
    a_big = {
        o_small * delta_small
        for o_small in o_big
        for delta_small in delta_big
        if o_small <= delta_small
    }
    m_big = {
        7 * delta_small - 9 * a_small
        for delta_small in delta_big
        for a_small in a_big
        if delta_small <= a_small
    }
    p_big = a_big.union(m_big)
    eta_1 = sum(m_small % 2 for m_small in m_big)
    eta_2 = sum(abs(p_small) for p_small in p_big)
    return eta_1 + eta_2

if __name__ == '__main__':
    print(main({-96, 36, 73, -52, -15, 18, 85, -69, 63, 95}))