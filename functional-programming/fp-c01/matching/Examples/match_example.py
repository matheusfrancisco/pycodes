from match import Match


def main():
    with Match(3.14159) as m:
        m(42)                   >> (lambda _: 'The Answer')
        (m(41) | m(43))         >> (lambda matched: 'Matched value %s' % matched)
        m(lambda x: not x%2)    >> (lambda matched: '%d is even' % matched)
        m(int)                  >> (lambda matched : '%d is an integer' % matched)
        m(...)                  >> (lambda unmatched : '%s was not matched' % unmatched)
        print(m.result)
        # catch missing match patterns

    with Match((1, 2, 3)) as m:
        m((..., 4, ...))        >> (lambda t: 'Matched tuple %s' % repr(t))
        m(...)                  >> (lambda t: 'No match for tuple %s' % repr(t))
        print(m.result)

main()