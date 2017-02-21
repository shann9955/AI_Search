def breadth_first_search(problem, candidates):
    if not candidates: return
    # make sure there is something in the candidate list

    k=len(candidates)

    # add children of current candidates unless goal is achieved
    for i in range(0,k):
        c = candidates.pop(0)   # pop from front
        node = c            # must exist
        print "node considered:", node
        if problem.goal(node): return c
        # base case

        succ = [s for s in problem.succ(node)]
        print "succ", succ
        for s in problem.succ(node):
            if s not in candidates:
                candidates.append(s)
        # 1-step extension

    return breadth_first_search(problem, candidates)
