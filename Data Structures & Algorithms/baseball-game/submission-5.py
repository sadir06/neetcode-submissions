class Solution:
    def calPoints(self, ops: List[str]) -> int:
        operations = "+DC"
        store = []
        for op in ops:
            if op == "+":
                new_score = store[-2] + store[-1] # I'm assuming that we have atleast 2 values before adding
                store.append(new_score)
            elif op == "D":

                score = store[-1]
                store.append(score * 2)
            elif op == "C":
                store.pop()
            else:
                store.append(int(op))

        return sum(store)